"""
    Introduction and 1st Screen of the App.
"""

import PySimpleGUI as sg

from src import constants, csg
from src.controllers import theme
from src.handlers import observer
from src.handlers.screen import Screen
from src.assets import animated_intro


SCREEN_NAME = '-INTRODUCTION-'
SHADOW_FRAMES = 31
FRAMES = 17
TIME_BETWEEN_FRAMES = 47
BACKGROUND_COLOR = '#000000'
count = FRAMES + SHADOW_FRAMES


image = sg.Image(
    data=animated_intro.source,
    background_color=BACKGROUND_COLOR,
    size=(theme.width, theme.height),
    subsample=animated_intro.size//theme.width
)


def animation_loop() -> None:
    global count
    count -= 1
    if count == 0:
        observer.unsubscribe(constants.TIME_OUT, animation_loop)
        observer.subscribe(constants.TIME_OUT, disable_screen)
    elif count >= SHADOW_FRAMES:
        image.update_animation(animated_intro.source, TIME_BETWEEN_FRAMES)


def disable_screen() -> None:
    observer.unsubscribe(constants.TIME_OUT, disable_screen)
    observer.post_event(constants.UPDATE_TIMEOUT, None)
    observer.post_event(constants.GOTO_VIEW, '-SELECT-PROFILE-')


screen_layout = [
    [csg.CenteredElement(image, background_color=BACKGROUND_COLOR)],
]

screen_config = {
    'background_color': BACKGROUND_COLOR,
    'element_justification': 'center',
}


def reset() -> None:
    global count
    count = FRAMES + SHADOW_FRAMES
    observer.subscribe(constants.TIME_OUT, animation_loop)
    observer.post_event(constants.UPDATE_TIMEOUT, TIME_BETWEEN_FRAMES)


screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
