from typing import Callable, TypedDict
from random import shuffle

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
        self._max_tryes = len(card.hints) - self._settings.characteristics_shown
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
        self.reset()

    def reset(self) -> None:
        self._rounds = 0
        self._scores: list[int] = []

    def _new_round(self) -> None:
        self._scores.append(self._round.score)
        self._rounds += 1
        self._round.reset(self._cards.new_card)

    def registry_event(self, type: str, fn: ResponseFn) -> None:
        self._events[type].append(fn) # ignore all


    @property
    def dataset_type(self) -> str:
        return self._cards.current_type
    
    @property
    def max_rounds(self) -> int:
        return self._difficulty.rounds_per_game

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
        return str(self._difficulty.time_per_round) + ':00'

    def _is_run_end(self) -> None:
        if self._rounds == self.max_rounds:
            self.end_run()

    def new_answer(self, option: str) -> None:
        if self._round.win(option):
            self._new_round()
            for fn in self._events['win_round']:
                fn()
        elif self._round.loose:
            self._new_round()
            for fn in self._events['loose_round']:
                fn()
        else:
            for fn in self._events['bad_option']:
                fn()
        self._is_run_end()

    def end_round(self) -> None:
        self._round.end()
        self._new_round()
        self._is_run_end()

    def end_run(self) -> None:
        for _ in range(self.max_rounds - len(self._scores)):
            self._scores.append(0)
        for fn in self._events['end_run']:
            fn()
