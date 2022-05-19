from copy import copy
from dataclasses import dataclass
from typing import TypedDict

from src import file
from .difficulty import DifficultyController

class SettingsJSON(TypedDict):
    title : str
    full_screen: bool
    starting_page: str
    theme: str
    difficulty : str

@dataclass
class Settings:
    title : str
    full_screen: bool
    starting_page: str
    theme: str
    difficulty : str

class SettingsController:
    def __init__(self, settings_path: str, difficulties_path: str):
        self._file_path = settings_path
        raw_settings: dict[str, SettingsJSON] = file.load_json(settings_path)
        self._settings = {
            name: Settings(**definition) for name, definition in raw_settings.items()
        }
        if 'custom' not in self._settings:
            self._settings['custom'] = copy(self._settings['default'])
        self._setting = self._settings['custom']
        self._difficulty_controller = DifficultyController(difficulties_path, self._setting.difficulty)

    @property
    def setting(self):
        return self._setting

    @property
    def difficulty(self):
        return self._difficulty_controller.difficulty

    @property
    def difficulty_controller(self):
        return self._difficulty_controller

    def _save_settings(self) -> None:
        file.save_json(
            self._file_path,
            self._settings,
            is_custom_class = True
        )
        self._difficulty_controller.save()

    def save(self) -> None:
        self._setting.difficulty = self._difficulty_controller.difficulty_name
        self._save_settings()