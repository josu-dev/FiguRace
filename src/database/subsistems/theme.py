import json
from os import path
from typing import TypedDict

from database.paths import DATA_PATH

RGBStr = str


class ThemeDefinition(TypedDict):
    BG_BASE : str
    BG_PRIMARY : str
    BG_SECONDARY : str
    BG_BUTTON : str
    BG_BUTTON_HOVER : str

    TEXT_ACCENT : str
    TEXT_PRIMARY : str
    TEXT_SECONDARY : str
    TEXT_BUTTON : str
    TEXT_BUTTON_HOVER : str
    
    BD_ACCENT : int
    BD_PRIMARY : int
    BD_SECONDARY : int
    FONT_FAMILY : str


def load_theme() -> ThemeDefinition:
    theme_path = path.join(DATA_PATH, 'theme.json')
    with open(theme_path, mode='r', encoding='utf-8') as file:
        theme = json.load(file)
        return theme


class Theme:
    def __init__(self):
        theme_settings = load_theme()
        self.BG_BASE= theme_settings['BG_BASE']
        self.BG_PRIMARY= theme_settings['BG_PRIMARY']
        self.BG_SECONDARY= theme_settings['BG_SECONDARY']
        self.BG_BUTTON= theme_settings['BG_BUTTON']
        self.BG_BUTTON_HOVER= theme_settings['BG_BUTTON_HOVER']

        self.TEXT_ACCENT= theme_settings['TEXT_ACCENT']
        self.TEXT_PRIMARY= theme_settings['TEXT_PRIMARY']
        self.TEXT_SECONDARY= theme_settings['TEXT_SECONDARY']
        self.TEXT_BUTTON= theme_settings['TEXT_BUTTON']
        self.TEXT_BUTTON_HOVER= theme_settings['TEXT_BUTTON_HOVER']
        
        self.BD_ACCENT= theme_settings['BD_ACCENT'],
        self.BD_PRIMARY= theme_settings['BD_PRIMARY'],
        self.BD_SECONDARY= theme_settings['BD_SECONDARY'],
        self.FONT_FAMILY= theme_settings['FONT_FAMILY']
