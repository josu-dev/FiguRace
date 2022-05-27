from typing import Any

import PySimpleGUI as sg

from src import file


SCREEN_SIZE = sg.Window.get_screen_size()

RESPONSIVE_TABLE = {
    2160: 2.0,
    1440: 1.3,
    1080: 1.0,
    720: 0.7,
    480: 0.4
}

for width in RESPONSIVE_TABLE:
    if SCREEN_SIZE[1] >= width:
        screen_factor = RESPONSIVE_TABLE[width]
        break
else:
    screen_factor = 0.2


def apply_scale(value: int) -> int:
    return round(value * screen_factor)


class Theme:
    def __init__(self, definition: dict[str, Any]):
        self.BG_BASE = definition['BG_BASE']
        self.BG_PRIMARY = definition['BG_PRIMARY']
        self.BG_SECONDARY = definition['BG_SECONDARY']

        self.BG_BUTTON = definition['BG_BUTTON']
        self.BG_BUTTON_HOVER = definition['BG_BUTTON_HOVER']

        self.TEXT_ACCENT = definition['F_C_ACCENT']
        self.TEXT_PRIMARY = definition['F_C_PRIMARY']
        self.TEXT_SECONDARY = definition['F_C_SECONDARY']

        self.TEXT_BUTTON = definition['F_C_BUTTON']
        self.TEXT_BUTTON_HOVER = definition['F_C_BUTTON_HOVER']

        self.BD_ACCENT = apply_scale(definition['BD_ACCENT'])
        self.BD_PRIMARY = apply_scale(definition['BD_PRIMARY'])
        self.BD_SECONDARY = apply_scale(definition['BD_SECONDARY'])
        self.BD_DELIMITER = apply_scale(definition['BD_DELIMITER'])

        self.FONT_FAMILY = definition['F_F_UI']
        self.FONT_FAMILY_TEXT = definition['F_F_CONTENT']

        self.H1_SIZE = apply_scale(definition['F_SIZE_H1'])
        self.H2_SIZE = apply_scale(definition['F_SIZE_H2'])
        self.H3_SIZE = apply_scale(definition['F_SIZE_H3'])
        self.T1_SIZE = apply_scale(definition['F_SIZE_T1'])
        self.T2_SIZE = apply_scale(definition['F_SIZE_T2'])
        self.T3_SIZE = apply_scale(definition['F_SIZE_T3'])

    @property
    def height(self):
        return SCREEN_SIZE[0]

    @property
    def width(self):
        return SCREEN_SIZE[1]


class ThemeController:
    def __init__(self, themes_path: str, default_theme_name: str):
        self._raw_themes: dict[str, Any] = file.load_json(themes_path)
        self._current_theme = default_theme_name
        self._theme = Theme(self._raw_themes[self._current_theme])

    @property
    def theme(self):
        return self._theme

    @property
    def theme_name(self):
        return self._current_theme

    @property
    def theme_list(self):
        return [name for name in self._raw_themes]
    
    def scale(self, value : int) -> int:
        return apply_scale(value)
