import PySimpleGUI as sg

from src import constants, csg, common

from src.controllers import theme
from src.handlers import observer
from src.handlers.layout import Screen

from src.assets.wallpaper import image

SCREEN_NAME = '-PRESENTATION-'

screen_layout = [
    [sg.Image(data=image.source,
              size=(1366,768),
              subsample=(1366//1366))
              ]
]


def reset() -> None: pass


screen_config = {
    'background_color': 'Red',
    'element_justification': 'center',
}

screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
