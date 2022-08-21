'''Main menu of the application.'''
from typing import Any

import PySimpleGUI as sg

from .. import constants as const
from ..controllers import theme
from ..assets import menu, title
from . import _common, _csg


SCREEN_NAME = '-MENU-'
ICON_BUTTON_SIZE = (theme.scale(96), theme.scale(96))
TEXT_BUTTON_FONT = (theme.FONT_FAMILY, theme.H3_SIZE)


def text_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        size=(16, 1),
        font=TEXT_BUTTON_FONT,
        auto_size_button=True,
        button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
        pad=2,
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=theme.BD_ACCENT
    )


def icon_button(icon: Any, screen_name: str) -> sg.Button:
    return _common.image_button(
        icon,
        ICON_BUTTON_SIZE,
        border=theme.BD_ACCENT,
        key=f'{const.GOTO_SCREEN} {screen_name}'
    )


def menu_options() -> sg.Column:
    '''The layout with the options proportioned by the menu screen.

    Returns:
        A column correctly structured for use on the window.'''
    layout = [
        [_csg.vertical_spacer(theme.scale(16), theme.BG_BASE)],
        [text_button(
            'Iniciar Partida',
            f'{const.GOTO_SCREEN} -CONFIGURE-GAME-'
        )],
        [_csg.vertical_spacer(theme.scale(24), theme.BG_BASE)],
        [
            icon_button(menu.ic_profile, '-SELECT-USER-'),
            _csg.horizontal_spacer(theme.scale(16), theme.BG_BASE),
            icon_button(menu.ic_setting, '-CONFIGURE-USER-'),
            _csg.horizontal_spacer(theme.scale(16), theme.BG_BASE),
            icon_button(menu.ic_score, '-RANKING-'),
        ],
        [_csg.vertical_spacer(theme.scale(16), theme.BG_BASE)],
        [text_button(
            'Configurar tema',
            key=f'{const.GOTO_SCREEN} -CONFIGURE-THEME-',
        )],
        [_csg.vertical_spacer(theme.scale(24), theme.BG_BASE)],
        [text_button(
            'Salir',
            key=const.EXIT_APPLICATION,
        )],
    ]
    return sg.Column(
        layout,
        background_color=theme.BG_BASE,
        element_justification='center',
        expand_y=True,
    )


screen_layout = [
    [sg.VPush(theme.BG_BASE)],
    [sg.Image(
        data=title.source,
        size=(theme.scale(1080), theme.scale(128)),
        subsample=title.size//theme.scale(800),
        background_color=theme.BG_BASE,
        pad=theme.scale(48)
    )],
    [menu_options()],
    [sg.VPush(theme.BG_BASE)],
]

screen_config = {
    'element_justification': 'center',
    'background_color': theme.BG_BASE,
}


def screen_reset() -> None:
    pass
