import PySimpleGUI as sg
from src import constants as const

from .layout import Screen, WindowLayoutController
from . import observer
from .theme import theme


layout_controller = WindowLayoutController()


def set_up(screens : list[Screen], title:str, initial_screen:str, fullscreen: bool=True) -> sg.Window:
    for screen in screens:
        layout_controller.register(screen)

    observer.subscribe(const.GOTO_VIEW, layout_controller.goto_layout)
    window_layout = layout_controller.get_composed_layout()

    window = sg.Window(
        title,
        window_layout,
        finalize=True,
        element_justification='c',
        resizable=True,
        background_color=theme.BG_BASE,
        margins=(0, 0)
    )

    if fullscreen:
        window.maximize()

    layout_controller.init(initial_screen)
    return window
