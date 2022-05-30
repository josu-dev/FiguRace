import PySimpleGUI as sg

from src import constants
from src.controllers import theme
from src.assets import app_icon

from . import observer
from .screen import Screen, ScreenController


screen_controller = ScreenController()


def set_up(screens: list[Screen], title: str, initial_screen: str, fullscreen: bool = True) -> sg.Window:
    for screen in screens:
        screen_controller.register(screen)

    observer.subscribe(constants.GOTO_VIEW, screen_controller.goto_layout)
    window_layout = screen_controller.composed_layout

    window = sg.Window(
        title,
        window_layout,
        icon=app_icon.source,
        finalize=True,
        element_justification='c',
        resizable=True,
        background_color=theme.BG_BASE,
        margins=(0, 0)
    )

    if fullscreen:
        window.maximize()

    screen_controller.init(initial_screen)
    return window
