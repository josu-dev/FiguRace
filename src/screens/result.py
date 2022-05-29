from typing import Any

import PySimpleGUI as sg

from src import constants, csg, common
from src.controllers import theme, users_controller as users_ctr
from src.handlers.screen import Screen
from src.handlers.user import User


SCREEN_NAME = '-RESULT-'


def create_summary() -> sg.Column:
    return sg.Column([[]])


def refresh_summary() -> None:
    pass


def create_nav_buttons() -> sg.Column:
    padding = (theme.scale(16),theme.scale(16))
    return csg.HorizontalList(
            background_color=theme.BG_BASE,
            element_justification='center'
        ).add(
            [
                common.navigation_button('Menu Principal', '-MENU-', padding=padding),
                common.navigation_button('Volver a Jugar', '-GAME-', padding=padding),
                common.navigation_button('Nuevo Juego', '-CONFIGURE-GAME-', padding=padding),
            ]
        ).pack()


screen_layout = [
    [common.screen_title('resultado', True)],
    [create_summary()],
    [csg.vertical_spacer(theme.scale(32), background_color=theme.BG_BASE)],
    [create_nav_buttons()]
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}


def reset():
    refresh_summary()


screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
