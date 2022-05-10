import json
from typing import Any, Optional, TypedDict
from os import path

print(__file__)
SRC_PATH = path.join(path.dirname(__file__),'..')
STORAGE_PATH = path.join(SRC_PATH, 'storage')
DEFAULT_SETTINGS = path.join(path.dirname(__file__),'..','settings.json')

def load_settings() -> Any:

    return None

RGBStr = str

class ThemeDefinition(TypedDict):
    BACKGROUND : RGBStr
    TEXT : RGBStr
    INPUT : RGBStr
    TEXT_INPUT : RGBStr
    SCROLL : RGBStr
    BUTTON : tuple[RGBStr,RGBStr]
    PROGRESS : tuple[RGBStr,RGBStr]
    BORDER : int
    SLIDER_DEPTH : int
    PROGRESS_DEPTH : int

    # ACCENT1 : Optional[RGBStr]
    # ACCENT2 : Optional[RGBStr]
    # ACCENT3 : Optional[RGBStr]

    # COLOR_LIST : Optional[list[RGBStr]]
    # BG_LIST : Optional[list[RGBStr]]
    # FG_LIST : Optional[list[RGBStr]]
    # BD_COLOR : Optional[RGBStr]
    # FONT_FAMILY : Optional[str]



class AppDefinition(TypedDict):
    name: str
    full_screen: bool
    starting_page: str

def load_theme() -> ThemeDefinition:
    theme_path = path.join(STORAGE_PATH, 'theme.json')
    with open(theme_path, mode='r', encoding='utf-8') as file:
        theme = json.load(file)
        return theme

def load_app() -> AppDefinition:
    app_path = path.join(STORAGE_PATH, 'app.json')
    with open(app_path, mode='r', encoding='utf-8') as file:
        return json.load(file)

print(load_app())
