from random import shuffle
from typing import Callable, TypedDict

from .. import constants
from . import observer
from .card import Card, CardController
from .difficulty import Difficulty, DifficultyController
from .run_event import EventNames, EventStates

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
    
    @property
    def correct_option(self) -> str:
        return self._card.correct_answer

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
    def __init__(self, cards_ctr: CardController, difficulty_ctr: DifficultyController) -> None:
        self._cards = cards_ctr
        self._difficulty_ctr = difficulty_ctr
        self._round = Round(self._cards.new_card, difficulty_ctr.difficulty)
        self._events_fn: RunEvent = {
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
            'total_tryes': 0
        }
        self._new_round()
        observer.post_event(
            constants.RUN_EVENT,
            {
                'name': EventNames.START,
                'rounds': self.max_rounds,
            }
        )

    def _new_round(self) -> None:
        if self._rounds > -1:
            self._scores.append(self._round.score)
        self._rounds += 1
        self._round.reset(self._cards.new_card)
        self._stats['total_rounds'] += 1

    def registry_event(self, type: str, fn: ResponseFn) -> None:
        self._events_fn[type].append(fn)  # type: ignore

    @property
    def stats(self) -> dict[str, int]:
        return self._stats

    @property
    def dataset_type(self) -> str:
        return self._cards.type

    @property
    def max_rounds(self) -> int:
        return self._difficulty_ctr.difficulty.rounds_per_game

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

    def _is_run_end(self) -> None:
        if self._rounds == self.max_rounds:
            self.end_run()

    def _force_loose(self) -> None:
        self._new_round()
        self._stats['rounds_loosed'] += 1
        self._stats['rounds_complete'] += 1
        for fn in self._events_fn['loose_round']:
            fn()

    def new_answer(self, option: str) -> None:
        self._stats['total_tryes'] += 1
        if self._round.win(option):
            self._new_round()
            self._stats['rounds_winned'] += 1
            self._stats['rounds_complete'] += 1
            observer.post_event(
                constants.RUN_EVENT,
                {
                    'name': EventNames.INTENT,
                    'rounds': self.max_rounds,
                    'state': EventStates.OK,
                    'user_answer': option,
                    'correct_answer': self._round.correct_option
                }
            )
            for fn in self._events_fn['win_round']:
                fn()
        elif self._round.loose:
            self._force_loose()
            observer.post_event(
                constants.RUN_EVENT,
                {
                    'name': EventNames.INTENT,
                    'rounds': self.max_rounds,
                    'state' : EventStates.ERROR,
                    'user_answer': option,
                    'correct_answer': self._round.correct_option
                }
            )
        else:
            observer.post_event(
                constants.RUN_EVENT,
                {
                    'name': EventNames.INTENT,
                    'rounds': self.max_rounds,
                    'state' : EventStates.ERROR,
                    'user_answer': option,
                    'correct_answer': self._round.correct_option
                }
            )
            for fn in self._events_fn['bad_option']:
                fn()
        self._is_run_end()

    def end_round(self) -> None:
        self._stats['rounds_skiped'] += 1
        self._round.end()
        self._new_round()
        self._is_run_end()

    def end_run(self) -> None:
        self._stats['total_points'] = sum(self._scores)
        self._stats['total_rounds'] = self.max_rounds
        for _ in range(self.max_rounds - len(self._scores)):
            self._scores.append(0)
        for fn in self._events_fn['end_run']:
            fn()
        
        observer.post_event(
            constants.RUN_EVENT,
            {
                'name': EventNames.END,
                'rounds': self.max_rounds,
                'state' : EventStates.ERROR,
            }
        )
