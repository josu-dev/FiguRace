import PySimpleGUI as sg
from src import constants as const
from src.handlers.layout import Screen
from src.handlers import observer
from src.screens.profile import select_profile, create_profile
from src.screens import menu
from src.handlers.theme import theme
SCREEN_NAME = '-PROFILE-'
_screen_main_title = sg.Text('PERFIL', size=500,
                             background_color=theme.BG_BASE,
                             font=(theme.FONT_FAMILY, 45),
                             text_color=theme.TEXT_ACCENT,
                             pad=0)

_profile_layout = [
    [
        sg.VPush(background_color=theme.BG_BASE)
    ],
    [
        sg.Button('Crear Perfil',
                  key=f'{const.GOTO_VIEW} {create_profile.SCREEN_NAME}',
                  border_width=20,
                  size=(15, 1),
                  button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                  mouseover_colors=theme.BG_BUTTON_HOVER,
                  font=(theme.FONT_FAMILY, 30), pad=7)
    ],

    [
        sg.Button('Seleccionar Perfil',
                  key=f'{const.GOTO_VIEW} {select_profile.SCREEN_NAME}',
                  border_width=20,
                  size=(15, 1),
                  button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                  mouseover_colors=theme.BG_BUTTON_HOVER,
                  font=(theme.FONT_FAMILY, 30), pad=7)
    ],
    [
        sg.VPush(background_color=theme.BG_BASE)
    ]
]

_turn = sg.Button('<--', key=f'{const.GOTO_VIEW} {menu.SCREEN_NAME}',
                  border_width=15,
                  size=(7, 0),
                  button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                  mouseover_colors=theme.BG_BUTTON_HOVER,
                  font=(theme.FONT_FAMILY, 20), pad=20)

_screen_layout = [
    [
        _screen_main_title
    ],
    [
        sg.Column(_profile_layout,
                  background_color=theme.BG_BASE,
                  expand_y=True, expand_x=True,
                  element_justification='c')
    ],
    [
        _turn
    ]
]

# TRATAR DE HACER RESPONSIVE LA VENTANA

# _relative_size =


def function_to_execute_on_event() -> None:
    # This function calls updates on database, updates elements of ui, or do other stuff
    pass

# observer.subscribe('-EVENT-TYPE-EVENT-EMITTER-', function_to_execute_on_event)


def reset(*args):
    # Funcions
    pass


_screen_config = {
    'background_color': theme.BG_BASE
}
screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
