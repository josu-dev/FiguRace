"""
    Introduction and 1st Screen of the App.
"""

import PySimpleGUI as sg

from src import constants, csg
from src.controllers import theme
from src.handlers import observer
from src.handlers.screen import Screen
from src.assets import title


SCREEN_NAME = '-INTRODUCTION-'
SECONDS = 3
BACKGROUND_COLOR = '#000000'


def create_icon() -> sg.Image:
    return sg.Image(
        data=title.source,
        background_color=BACKGROUND_COLOR,
        size=(theme.width, theme.scale(256)),
        subsample=title.size//theme.width
    )


def disable_screen() -> None:
    observer.unsubscribe(constants.TIME_OUT, disable_screen)
    observer.post_event(constants.UPDATE_TIMEOUT, None)
    observer.post_event(constants.GOTO_VIEW, '-SELECT-PROFILE-')


screen_layout = [
    [csg.CenteredElement(create_icon(), background_color=BACKGROUND_COLOR)],
]

screen_config = {
    'background_color': BACKGROUND_COLOR,
    'element_justification': 'center',
}


def reset() -> None:
    observer.subscribe(constants.TIME_OUT, disable_screen)
    observer.post_event(constants.UPDATE_TIMEOUT, SECONDS)


screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
