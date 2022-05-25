from dataclasses import dataclass
from typing import TypedDict

from src import file


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


class ThemeController:
    def __init__(self, themes_path: str, default_theme_name: str):
        raw_themes: dict[str, ThemeJSON] = file.load_json(themes_path)
        self._themes = {
            name: Theme(**definition) for name, definition in raw_themes.items()
        }
        self._current_theme = default_theme_name
        self._theme = self._themes[self._current_theme]

    @property
    def theme(self):
        return self._theme

    @property
    def theme_name(self):
        return self._current_theme

    @property
    def theme_list(self):
        return [name for name in self._themes]
