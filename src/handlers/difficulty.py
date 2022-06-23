from copy import copy
from dataclasses import dataclass
from typing import Any

from .. import constants, default
from . import observer, file


@dataclass
class Difficulty:
    '''Class that contains a difficulty configuration.'''
    time_per_round: int
    rounds_per_game: int
    points_correct_answer: int
    points_bad_answer: int
    characteristics_shown: int

    def swap(self, new: 'Difficulty') -> None:
        '''Updates self from another difficulty.
        
        Args:
            new: a Difficulty instance '''
        self.time_per_round = new.time_per_round
        self.rounds_per_game = new.rounds_per_game
        self.points_correct_answer = new.points_correct_answer
        self.points_bad_answer = new.points_bad_answer
        self.characteristics_shown = new.characteristics_shown

    def jsonify(self) -> dict[str, int]:
        return {
            'time_per_round': self.time_per_round,
            'rounds_per_game': self.rounds_per_game,
            'points_correct_answer': self.points_correct_answer,
            'points_bad_answer': self.points_bad_answer,
            'characteristics_shown': self.characteristics_shown
        }


class DifficultyController:
    def __init__(self, difficulties_path: str, difficulty: str = default.DIFFICULTY_TYPE) -> None:
        self._file_path = difficulties_path
        self._current_difficulty = difficulty
        raw_difficulties: dict[str, dict[str, int]] = file.load_json(
            difficulties_path, default.DIFFICULTIES
        )
        self._difficulties = {
            name: Difficulty(**definition) for name, definition in raw_difficulties.items()
        }
        self._difficulty = copy(self._difficulties[self._current_difficulty])
        observer.subscribe(constants.USER_CHANGE, self._new_user)

    @property
    def difficulty(self) -> Difficulty:
        return self._difficulty

    @property
    def difficulty_name(self) -> str:
        return self._current_difficulty

    def update_difficulty(
        self, time_per_round: int | None = None,
        rounds_per_game: int | None = None, points_correct_answer: int | None = None,
        points_bad_answer: int | None = None, characteristics_shown: int | None = None,
    ) -> None:
        if time_per_round is not None:
            self._difficulties['custom'].time_per_round = time_per_round
        if rounds_per_game is not None:
            self._difficulties['custom'].rounds_per_game = rounds_per_game
        if points_correct_answer is not None:
            self._difficulties['custom'].points_correct_answer = points_correct_answer
        if points_bad_answer is not None:
            if points_bad_answer > 0:
                points_bad_answer *= -1
            self._difficulties['custom'].points_bad_answer = points_bad_answer
        if characteristics_shown is not None:
            self._difficulties['custom'].characteristics_shown = characteristics_shown
        self.set_difficulty('custom')

    def set_difficulty(self, type: str) -> None:
        self._current_difficulty = type
        self._difficulty.swap(self._difficulties[type])
        observer.post_event(constants.UPDATE_DIFFICULTY_TYPE, type)

    def difficulties(self) -> dict[str, Difficulty]:
        return {name: copy(definition) for name, definition in self._difficulties.items()}

    def _new_user(self, user: Any) -> None:
        self._difficulties['custom'] = user.custom_difficulty
        self.set_difficulty(user.preferred_difficulty)

    def save(self) -> None:
        file.save_json(
            self._file_path,
            self._difficulties,
            is_custom_class=True
        )
