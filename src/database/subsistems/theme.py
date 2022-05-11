import json
from os import path
from typing import TypedDict

from database.paths import DATA_PATH

RGBStr = str


class ThemeDefinition(TypedDict):
    BACKGROUND: RGBStr
    TEXT: RGBStr
    INPUT: RGBStr
    TEXT_INPUT: RGBStr
    SCROLL: RGBStr
    BUTTON: tuple[RGBStr, RGBStr]
    PROGRESS: tuple[RGBStr, RGBStr]
    BORDER: int
    SLIDER_DEPTH: int
    PROGRESS_DEPTH: int

    # ACCENT1 : Optional[RGBStr]
    # ACCENT2 : Optional[RGBStr]
    # ACCENT3 : Optional[RGBStr]

    # COLOR_LIST : Optional[list[RGBStr]]
    # BG_LIST : Optional[list[RGBStr]]
    # FG_LIST : Optional[list[RGBStr]]
    # BD_COLOR : Optional[RGBStr]
    # FONT_FAMILY : Optional[str]


def load_theme() -> ThemeDefinition:
    theme_path = path.join(DATA_PATH, 'theme.json')
    with open(theme_path, mode='r', encoding='utf-8') as file:
        theme = json.load(file)
        return theme


class Theme:
    def __init__(self):
        theme_settings = load_theme()
        self.BACKGROUND = theme_settings['BACKGROUND']
        self.TEXT = theme_settings['TEXT']
        self.INPUT = theme_settings['INPUT']
        self.TEXT_INPUT = theme_settings['TEXT_INPUT']
        self.SCROLL = theme_settings['SCROLL']
        self.BUTTON = theme_settings['BUTTON']
        self.PROGRESS = theme_settings['PROGRESS']
        self.BORDER = theme_settings['BORDER']
        self.SLIDER_DEPTH = theme_settings['SLIDER_DEPTH']
        self.PROGRESS_DEPTH = theme_settings['PROGRESS_DEPTH']
