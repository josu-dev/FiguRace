import PySimpleGUI as sg
from src.handlers.layout import GOTO_VIEW, WindowLayoutController
from src.handlers import observer
from src.screens import base_screen, menu
from src.screens.profile import profile, select_profile, create_profile
from src.screens import configuration
EXIT_APLICATION = '-EXIT-APP-'
BACK_GROUND_COLOR = '#112B3C'
DEFAULT_TITLE = 'Figurace'
DEFAULT_INITIAL_SCREEN = menu.screen.key

layout_controller = WindowLayoutController()


def window_set_up() -> sg.Window:
    # All screens in the aplication
    layout_controller.register(base_screen.screen)
    layout_controller.register(profile.screen)
    layout_controller.register(select_profile.screen)
    layout_controller.register(create_profile.screen)
    layout_controller.register(menu.screen)
    layout_controller.register(configuration.screen)
    # layout_controller.register(user.screen)

    observer.subscribe(GOTO_VIEW, layout_controller.goto_layout)
    window_layout = layout_controller.get_composed_layout()

    window = sg.Window(DEFAULT_TITLE,
                       window_layout,
                       finalize=True,
                       element_justification='c',
                       background_color=BACK_GROUND_COLOR
                       )
    window.Maximize()

    layout_controller.init(DEFAULT_INITIAL_SCREEN)
    return window
