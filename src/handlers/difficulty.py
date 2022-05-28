from copy import copy
from dataclasses import dataclass
from typing import Any, TypedDict

from src import constants, file

from . import observer


DEFAULT_TYPE = 'normal'
UPDATE_DIFFICULTY_TYPE = '-UPDATE-DIFFICULTY-TYPE-'


class DifficultyJSON(TypedDict):
    time_per_round: int
    rounds_per_game: int
    points_correct_answer: int
    points_bad_answer: int
    characteristics_shown: int


def default() -> DifficultyJSON:
    return {
        'time_per_round': 50,
        'rounds_per_game': 10,
        'points_correct_answer': 12,
        'points_bad_answer': -2,
        'characteristics_shown': 3
    }


@dataclass
class Difficulty:
    time_per_round: int
    rounds_per_game: int
    points_correct_answer: int
    points_bad_answer: int
    characteristics_shown: int

    def swap(self, new: 'Difficulty') -> None:
        self.time_per_round = new.time_per_round
        self.rounds_per_game = new.rounds_per_game
        self.points_correct_answer = new.points_correct_answer
        self.points_bad_answer = new.points_bad_answer
        self.characteristics_shown = new.characteristics_shown

    def to_json(self) -> DifficultyJSON:
        return {
            'time_per_round': self.time_per_round,
            'rounds_per_game': self.rounds_per_game,
            'points_correct_answer': self.points_correct_answer,
            'points_bad_answer': self.points_bad_answer,
            'characteristics_shown': self.characteristics_shown
        }


class DifficultyController:
    def __init__(self, difficulties_path: str ,difficulty: str = DEFAULT_TYPE):
        self._file_path = difficulties_path
        self._current_difficulty = difficulty
        raw_difficulties: dict[str, DifficultyJSON] = file.load_json(
            difficulties_path)
        self._difficulties = {
            name: Difficulty(**definition) for name, definition in raw_difficulties.items()
        }
        self._difficulty = copy(self._difficulties[self._current_difficulty])
        observer.subscribe(constants.USER_CHANGE, self._new_user)

    @property
    def difficulty(self):
        return self._difficulty

    @property
    def difficulty_name(self):
        return self._current_difficulty

    def update_difficulty(
        self, time_per_round: int | None = None,
        rounds_per_game: int | None = None, points_correct_answer: int | None = None,
        points_bad_answer: int | None = None, characteristics_shown: int | None = None,
    ) -> None:
        if time_per_round:
            self._difficulties['custom'].time_per_round = time_per_round
        if rounds_per_game:
            self._difficulties['custom'].rounds_per_game = rounds_per_game
        if points_correct_answer:
            self._difficulties['custom'].points_correct_answer = points_correct_answer
        if points_bad_answer:
            self._difficulties['custom'].points_bad_answer = points_bad_answer
        if characteristics_shown:
            self._difficulties['custom'].characteristics_shown = characteristics_shown
        self.set_difficulty('custom')

    def set_difficulty(self, type: str) -> None:
        self._current_difficulty = type
        self._difficulty.swap(self._difficulties[type])
        observer.post_event(UPDATE_DIFFICULTY_TYPE, type)

    def difficulties(self) -> dict[str, Difficulty]:
        return {name: copy(definition) for name, definition in self._difficulties.items()}

    def _new_user(self, user:Any) -> None:
        self._difficulties['custom'] = user.custom_difficulty
        self.set_difficulty(user.preferred_difficulty)

    def _save_difficulties(self) -> None:
        file.save_json(
            self._file_path,
            self._difficulties,
            is_custom_class=True
        )

    def save(self) -> None:
        self._save_difficulties()
