import json

from copy import copy
from os import path
from typing import TypedDict

from src import SRC_PATH


class ThemeDefinition(TypedDict):
    BG_BASE: str
    BG_PRIMARY: str
    BG_SECONDARY: str
    BG_BUTTON: str
    BG_BUTTON_HOVER: str

    TEXT_ACCENT: str
    TEXT_PRIMARY: str
    TEXT_SECONDARY: str
    TEXT_BUTTON: str
    TEXT_BUTTON_HOVER: str

    BD_ACCENT: int
    BD_PRIMARY: int
    BD_SECONDARY: int
    FONT_FAMILY: str


class Theme:
    def __init__(self, definition: ThemeDefinition):
        self.BG_BASE = definition['BG_BASE']
        self.BG_PRIMARY = definition['BG_PRIMARY']
        self.BG_SECONDARY = definition['BG_SECONDARY']
        self.BG_BUTTON = definition['BG_BUTTON']
        self.BG_BUTTON_HOVER = definition['BG_BUTTON_HOVER']

        self.TEXT_ACCENT = definition['TEXT_ACCENT']
        self.TEXT_PRIMARY = definition['TEXT_PRIMARY']
        self.TEXT_SECONDARY = definition['TEXT_SECONDARY']
        self.TEXT_BUTTON = definition['TEXT_BUTTON']
        self.TEXT_BUTTON_HOVER = definition['TEXT_BUTTON_HOVER']

        self.BD_ACCENT = definition['BD_ACCENT'],
        self.BD_PRIMARY = definition['BD_PRIMARY'],
        self.BD_SECONDARY = definition['BD_SECONDARY'],
        self.FONT_FAMILY = definition['FONT_FAMILY']


class ThemeController:
    def __init__(self, src_path: str, default_theme_name: str):
        raw_themes = self._load_themes(src_path)
        self._themes = {
            name: Theme(definition) for name, definition in raw_themes.items()
        }
        self._current_theme = default_theme_name
        self._theme = copy(self._themes[self._current_theme])

    def _load_themes(self, src_path: str) -> dict[str, ThemeDefinition]:
        file_path = path.join(src_path, 'database', 'data', 'theme.json')
        with open(file_path, mode='r', encoding='utf-8') as file:
            theme = json.load(file)
            return theme

    @staticmethod
    def _interchange(base: Theme, new: Theme):
        base.BG_BASE = new.BG_BASE
        base.BG_PRIMARY = new.BG_PRIMARY
        base.BG_SECONDARY = new.BG_SECONDARY
        base.BG_BUTTON = new.BG_BUTTON
        base.BG_BUTTON_HOVER = new.BG_BUTTON_HOVER

        base.TEXT_ACCENT = new.TEXT_ACCENT
        base.TEXT_PRIMARY = new.TEXT_PRIMARY
        base.TEXT_SECONDARY = new.TEXT_SECONDARY
        base.TEXT_BUTTON = new.TEXT_BUTTON
        base.TEXT_BUTTON_HOVER = new.TEXT_BUTTON_HOVER

        base.BD_ACCENT = new.BD_ACCENT
        base.BD_PRIMARY = new.BD_PRIMARY
        base.BD_SECONDARY = new.BD_SECONDARY
        base.FONT_FAMILY = new.FONT_FAMILY

    @property
    def theme(self):
        return self._theme
    
    @property
    def theme_name(self):
        return self._current_theme

    @property
    def theme_list(self):
        return [name for name in self._themes.keys()]

    def set_theme(self, name: str):
        if name not in self._themes.keys():
            raise Exception(f'{name} not is a valid theme')
        self._current_theme = name
        self._interchange(self._theme, self._themes[name])


_theme_controller = ThemeController(SRC_PATH, 'Blue-Like')
theme = _theme_controller.theme
