import PySimpleGUI as sg
from handlers.layout import GOTO_VIEW, WindowLayoutController
from handlers import observer
from src.screens import base_screen

DEFAULT_TITLE = 'Figurace'

layout_controller = WindowLayoutController()


def window_set_up() -> sg.Window:
    # All screens in the aplication
    layout_controller.register(base_screen.screen)
    # layout_controller.register(menu.screen)
    # layout_controller.register(configuration.screen)
    # layout_controller.register(user.screen)

    observer.subscribe(GOTO_VIEW, layout_controller.goto_layout)
    window_layout = layout_controller.get_composed_layout()

    window = sg.Window(DEFAULT_TITLE, window_layout, finalize=True)
    return window
