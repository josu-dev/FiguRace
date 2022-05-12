import PySimpleGUI as sg
from src import constants as const
from src.handlers.theme import theme
from src.handlers.layout import Screen

SCREEN_NAME = "-MENU-"
_default_padding = 2
_font = ('System', 32)


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=theme.BG_BASE)


def _title() -> sg.Text:
    return sg.Text('F  I  G  U  R  A  C  E', size=(800, 1), background_color=theme.BG_BASE, text_color='#EFEFEF', key='-title-', font=('Sketch 3D', 86), justification='center', pad=64)


_btn_start_game_ = sg.Button('Iniciar Juego',
                             key='-GAME-',
                             size=(18, 1),
                             font=_font,
                             auto_size_button=True,
                             button_color=(theme.TEXT_PRIMARY,
                                           theme.BG_BUTTON),
                             pad=_default_padding,
                             mouseover_colors=theme.BG_BUTTON_HOVER,
                             border_width=12)

_btn_options = sg.Button('Configuración', size=(18, 1),
                         key=f'{const.GOTO_VIEW} -CONFIGURATION-',
                         auto_size_button=True,
                         font=_font,
                         button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
                         pad=_default_padding,
                         mouseover_colors=theme.BG_BUTTON_HOVER,
                         border_width=12)

_btn_profile = sg.Button('Perfil', size=(18, 1),
                         key=f'{const.GOTO_VIEW} -PROFILE-',
                         auto_size_button=True,
                         font=_font,
                         button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
                         pad=_default_padding,
                         mouseover_colors=theme.BG_BUTTON_HOVER,
                         border_width=12)


def _menu_options() -> list[list]:
    layout = [
        [_v_spacer((0, 12))],
        [_btn_start_game_],
        [_v_spacer((0, 12))],
        [_btn_options],
        [_v_spacer((0, 12))],
        [_btn_profile],
        [_v_spacer((0, 12))],
        [sg.Button('Salir', size=(18, 1),
                   auto_size_button=True,
                   key=const.EXIT_APLICATION,
                   font=_font,
                   button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
                   pad=_default_padding,
                   mouseover_colors=theme.BG_BUTTON_HOVER,
                   border_width=12)]
    ]
    return layout


# All the stuff inside your window.
_screen_layout = [
    [_title()],
    [sg.Column(_menu_options(), background_color=theme.BG_BASE,)],
]

_screen_config = {
    'element_justification': 'c',
    'background_color': theme.BG_BASE,
}


def reset(*args):
    # Funcions
    pass


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
