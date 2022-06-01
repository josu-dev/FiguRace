from typing import Callable, TypedDict
from random import shuffle

from src import constants

from . import observer
from .card import Card, CardController
from .difficulty import Difficulty, DifficultyController


ResponseFn = Callable[..., None]


class RunEvent(TypedDict):
    end_run: list[ResponseFn]
    win_round: list[ResponseFn]
    loose_round: list[ResponseFn]
    bad_option: list[ResponseFn]


class Round:
    def __init__(self, card: Card, difficulty: Difficulty) -> None:
        self._settings = difficulty
        self.reset(card)

    def reset(self, card: Card) -> None:
        self._card = card
        self._tryes = 0
        self._max_tryes = len(card.hints) - 1
        self._hints_quantity = self._settings.characteristics_shown
        self._hints = self._card.hints[0:self._hints_quantity]
        self._score = 0

    @property
    def hints(self) -> list[str]:
        return self._hints

    @property
    def options(self) -> list[str]:
        options = [*self._card.bad_anwers, self._card.correct_answer]
        shuffle(options)
        return options

    def _add_hint(self) -> None:
        self._hints_quantity += 1
        if self._hints_quantity < len(self._card.hints):
            self._hints = self._card.hints[0:self._hints_quantity]

    def win(self, option: str) -> bool:
        if option == self._card.correct_answer:
            self._score += self._settings.points_correct_answer
            return True
        self._score += self._settings.points_bad_answer
        self._tryes += 1
        self._add_hint()
        return False

    @property
    def loose(self) -> bool:
        return self._tryes == self._max_tryes

    @property
    def score(self) -> int:
        return self._score

    def end(self) -> None:
        self._score = 0


class RunController:
    def __init__(self, cards_ctr: CardController, difficulty_ctr: DifficultyController):
        self._cards = cards_ctr
        self._difficulty = difficulty_ctr.difficulty
        self._round = Round(self._cards.new_card, difficulty_ctr.difficulty)
        self._events: RunEvent = {
            'end_run': [],
            'win_round': [],
            'loose_round': [],
            'bad_option': []
        }

    def reset(self) -> None:
        self._rounds = -1
        self._scores: list[int] = []
        self._stats = {
            'total_points': 0,
            'total_rounds': 0,
            'rounds_complete': 0,
            'rounds_skiped': 0,
            'rounds_winned': 0,
            'rounds_loosed': 0,
            'total_time': 0,
            'average_time': 0,
            'total_tryes': 0
        }
        self._time = 0
        self._new_round()
        observer.subscribe(constants.TIME_OUT, self._update_time)
        observer.post_event(constants.UPDATE_TIMEOUT, 1)

    def _new_round(self) -> None:
        if self._rounds > -1:
            self._scores.append(self._round.score)
        self._rounds += 1
        self._round.reset(self._cards.new_card)
        self._stats['total_rounds'] += 1
        self._stats['total_time'] += self._difficulty.time_per_round - self._time
        self._time = self._difficulty.time_per_round

    def registry_event(self, type: str, fn: ResponseFn) -> None:
        self._events[type].append(fn)

    @property
    def stats(self) -> dict[str, int]:
        return self._stats

    @property
    def dataset_type(self) -> str:
        return self._cards.current_type

    @property
    def max_rounds(self) -> int:
        return self._difficulty.rounds_per_game

    @property
    def score(self) -> list[int]:
        return self._scores

    @property
    def hints_types(self) -> list[str]:
        return self._cards.characteristics

    @property
    def hints(self) -> list[str]:
        return self._round.hints

    @property
    def options(self) -> list[str]:
        return self._round.options

    # Implement timer on round
    @property
    def time(self) -> str:
        return str(self._time) + ':00'

    def _update_time(self) -> None:
        self._time -= 1
        if self._time < 0:
            self._force_loose()

    def _is_run_end(self) -> None:
        if self._rounds == self.max_rounds:
            self.end_run()

    def _force_loose(self) -> None:
        self._new_round()
        self._stats['rounds_loosed'] += 1
        self._stats['rounds_complete'] += 1
        for fn in self._events['loose_round']:
            fn()

    def new_answer(self, option: str) -> None:
        self._stats['total_tryes'] += 1
        if self._round.win(option):
            self._new_round()
            self._stats['rounds_winned'] += 1
            self._stats['rounds_complete'] += 1
            for fn in self._events['win_round']:
                fn()
        elif self._round.loose:
            self._force_loose()
        else:
            for fn in self._events['bad_option']:
                fn()
        self._is_run_end()

    def end_round(self) -> None:
        self._stats['rounds_skiped'] += 1
        self._round.end()
        self._new_round()
        self._is_run_end()

    def end_run(self) -> None:
        observer.post_event(constants.UPDATE_TIMEOUT, None)
        observer.unsubscribe(constants.TIME_OUT, self._update_time)
        self._stats['total_points'] = sum(self._scores)
        self._stats['total_rounds'] = self.max_rounds
        self._stats['average_time'] = self._stats['total_time'] // self._stats['total_rounds']
        for _ in range(self.max_rounds - len(self._scores)):
            self._scores.append(0)
        for fn in self._events['end_run']:
            fn()
