import PySimpleGUI as sg

from src import constants as const, common, csg

from src.controllers import theme
from src.handlers.layout import Screen
from src.assets.menu import ic_profile, ic_exit, ic_config


SCREEN_NAME = "-MENU-"
_default_padding = 2
_font = ('System', theme.H2_SIZE)
_scale = theme.scale(135)
_icon_size = (_scale, _scale)


def _menu_options() -> list[list[sg.Element]]:
    layout = [
        [csg.vertical_spacer((0, 24), background_color=theme.BG_BASE)],
        [sg.Button('Iniciar Juego',
                   key=f'{const.GOTO_VIEW} -CONFIGURE-GAME-',
                   size=(18, 1),
                   font=_font,
                   auto_size_button=True,
                   button_color=(theme.TEXT_BUTTON,
                                 theme.BG_BUTTON),
                   pad=_default_padding,
                   mouseover_colors=theme.BG_BUTTON_HOVER,
                   border_width=theme.BD_ACCENT)],
        [csg.vertical_spacer((0, 24), background_color=theme.BG_BASE)],
        [
            common.image_button(
                ic_config,
                _icon_size,
                border=theme.BD_ACCENT,
                key=f'{const.GOTO_VIEW} -CONFIGURATION-'
            ),
            csg.horizontal_spacer(
                (40, 0), background_color=theme.BG_BASE),
            common.image_button(
                ic_profile,
                _icon_size,
                border=theme.BD_ACCENT,
                key=f'{const.GOTO_VIEW} -SELECT-PROFILE-'
            ),
            csg.horizontal_spacer((40, 0), background_color=theme.BG_BASE),
            common.image_button(
                ic_exit,
                _icon_size,
                border=theme.BD_ACCENT,
                key=const.EXIT_APLICATION
            )]
    ]
    return layout


def reset():
    # Funcions
    pass


# All the stuff inside your window.
_screen_layout = [
    [common.screen_title('f  i  g  u  r  a  c  e', size=theme.H1_SIZE)],
    [sg.Column(_menu_options(), background_color=theme.BG_BASE, expand_y=True,
               element_justification='c')],
]

_screen_config = {
    'element_justification': 'c',
    'background_color': theme.BG_BASE,
}


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
