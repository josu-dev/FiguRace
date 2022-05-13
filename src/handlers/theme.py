from copy import copy
from dataclasses import dataclass
from typing import TypedDict

from src import constants as const, file


class ThemeJSON(TypedDict):
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


@dataclass
class Theme:
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

    def swap(self, new: 'Theme'):
        self.BG_BASE = new.BG_BASE                      # type: ignore
        self.BG_PRIMARY = new.BG_PRIMARY                # type: ignore
        self.BG_SECONDARY = new.BG_SECONDARY            # type: ignore
        self.BG_BUTTON = new.BG_BUTTON                  # type: ignore
        self.BG_BUTTON_HOVER = new.BG_BUTTON_HOVER      # type: ignore

        self.TEXT_ACCENT = new.TEXT_ACCENT              # type:ignore
        self.TEXT_PRIMARY = new.TEXT_PRIMARY            # type:ignore
        self.TEXT_SECONDARY = new.TEXT_SECONDARY        # type:ignore
        self.TEXT_BUTTON = new.TEXT_BUTTON              # type:ignore
        self.TEXT_BUTTON_HOVER = new.TEXT_BUTTON_HOVER  # type:ignore

        self.BD_ACCENT = new.BD_ACCENT                  # type:ignore
        self.BD_PRIMARY = new.BD_PRIMARY                # type:ignore
        self.BD_SECONDARY = new.BD_SECONDARY            # type:ignore
        self.FONT_FAMILY = new.FONT_FAMILY              # type:ignore


class ThemeController:
    def __init__(self, themes_path: str, default_theme_name: str):
        raw_themes: dict[str, ThemeJSON] = file.load_json(themes_path)
        self._themes = {
            name: Theme(**definition) for name, definition in raw_themes.items()
        }
        self._current_theme = default_theme_name
        self._theme = copy(self._themes[self._current_theme])

    @property
    def theme(self):
        return self._theme

    @property
    def theme_name(self):
        return self._current_theme

    @property
    def theme_list(self):
        return [name for name in self._themes.keys()]

    def set_theme(self, name: str) -> None:
        if name not in self._themes.keys():
            raise Exception(f'{name} not is a valid theme')
        self._current_theme = name
        self._theme.swap(self._themes[name])


_theme_controller = ThemeController(const.PATH_THEME, 'Blue-Like')
theme = _theme_controller.theme
