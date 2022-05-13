from copy import copy
from dataclasses import dataclass
from typing import TypedDict

from src import file


class DifficultyJSON(TypedDict):
    time_per_round: int
    rounds_per_game: int
    points_correct_answer: int
    points_bad_answer: int
    caracteristics_shown: int


@dataclass
class Difficulty:
    time_per_round: int
    rounds_per_game: int
    points_correct_answer: int
    points_bad_answer: int
    caracteristics_shown: int

    def swap(self, new: 'Difficulty') -> None:
        self.time_per_round = new.time_per_round
        self.rounds_per_game = new.rounds_per_game
        self.points_correct_answer = new.points_correct_answer
        self.points_bad_answer = new.points_bad_answer
        self.caracteristics_shown = new.caracteristics_shown


class DifficultyController:
    def __init__(self, difficulties_path: str, default_difficulty: str = 'easy'):
        self._file_path = difficulties_path
        self._current_difficulty = default_difficulty
        raw_difficulties: dict[str, DifficultyJSON] = file.load_json(difficulties_path)
        self._difficulties = {
            name: Difficulty(**definition) for name, definition in raw_difficulties.items()
        }
        self._difficulty = copy(self._difficulties[self._current_difficulty])

    @property
    def difficulty(self):
        return self._difficulty

    @property
    def difficulty_name(self):
        return self._current_difficulty

    # Improve this method
    def update_difficulty(self, name: str = '', **values: int) -> None:
        if name == '' or name == 'custom':
            self._current_difficulty = 'custom'
            if 'time_per_round' in values:
                self._difficulty.time_per_round = values['time_per_round']
            if 'rounds_per_game' in values:
                self._difficulty.rounds_per_game = values['rounds_per_game']
            if 'points_correct_answer' in values:
                self._difficulty.points_correct_answer = values['points_correct_answer']
            if 'points_bad_answer' in values:
                self._difficulty.points_bad_answer = values['points_bad_answer']
            if 'caracteristics_shown' in values:
                self._difficulty.caracteristics_shown = values['caracteristics_shown']
            self._difficulties['custom'].swap(self._difficulty)
        else:
            self._difficulty.swap(self._difficulties[name])

    def difficulties(self) -> dict[str, Difficulty]:
        return {name: copy(definition) for name, definition in self._difficulties.items()}

    def _save_difficulties(self) -> None:
        file.save_json(
            self._file_path,
            self._difficulties,
            is_custom_class=True
        )

    def save(self) -> None:
        self._save_difficulties()
