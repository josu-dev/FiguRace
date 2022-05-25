from random import shuffle

from .card import Card, CardController
from .difficulty import Difficulty, DifficultyController


ROUNDS_QUANTITY = 10


class Round:
    def __init__(self, card: Card, difficulty: Difficulty) -> None:
        self._settings = difficulty
        self.reset(card)

    def reset(self, card: Card) -> None:
        self._card = card
        self._tryes = 0
        self._max_tryes = len(card.hints) - self._settings.caracteristics_shown
        self._hints_quantity = self._settings.caracteristics_shown
        self._hints = self._card.hints[0:self._hints_quantity]

    @property
    def hints(self) -> list[str]:
        return self._hints

    @property
    def options(self) -> list[str]:
        options = [*self._card.bad_anwers, self._card.correct_answer]
        shuffle(options)
        return options

    def _add_hint(self) -> None:
        if self._hints_quantity < len(self._card.hints):
            self._hints = self._card.hints[0:self._hints_quantity]

    def win(self, option: str) -> bool:
        if option == self._card.correct_answer:
            return True
        self._tryes += 1
        self._add_hint()
        return False

    @property
    def loose(self) -> bool:
        return self._tryes == self._max_tryes


class RunController:
    ROUNDS_QUANTITY = ROUNDS_QUANTITY

    def __init__(self, cards_ctr: CardController, difficulty_ctr: DifficultyController):
        self._cards = cards_ctr
        self._round = Round(self._cards.new_card, difficulty_ctr.difficulty)
        self._answers = 0
        self._rounds = 0

    # @property
    # def win(self) -> bool:
    #     return

    # def accert(self, option: str) -> bool:
    #     self._answers += 1
    #     if option == self._card.correct_answer:
    #         return True
    #     if self._answers == self._max_answers:
    #         return False

    # def refresh() -> None:
    #     pass

    # def reset() -> None:
    #     pass
