from cgitb import enable
from pickle import FALSE
from typing import Any
from xml.sax.handler import feature_external_ges
import PySimpleGUI as sg
from src import constants as const
from src.handlers.layout import Screen
from src.handlers import observer
from src.screens import menu
from src.controllers import theme
from src.assets.users import *
from src import csg, common
from src.controllers import users_controller as users_ctr
from src.assets.wallpaper import image as wall


SCREEN_NAME = '-SELECT-PROFILE-'
EVENT_CREATE_PROFILE = '-CREATE-PROFILE-'
EVENT_REMOVE_PROFILE = '-REMOVE-PROFILE-'
EVENT_EDIT_PROFILE = '-EDIT-PROFILE-'
EVENT_SAVE_PROFILE = '-SAVE-PROFILE-'

_confirm_button = sg.Button('-<-Jugar->-',
                            key=f'{const.GOTO_VIEW} {menu.SCREEN_NAME}',
                            border_width=theme.BD_ACCENT,
                            button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                            mouseover_colors=theme.BG_BUTTON_HOVER,
                            font=(theme.FONT_FAMILY, theme.T1_SIZE),
                            disabled=True
                            )

_current_user = sg.Text('Seleccionado:',
                        # background_color='RED',
                        background_color=theme.BG_BASE,
                        font=(theme.FONT_FAMILY, theme.H3_SIZE),
                        size=(24, 1)
                        )

_user_list = sg.Listbox(values=users_ctr.users_transform(lambda user: user.nick),
                        expand_y=True,
                        size=(25, 0),
                        # background_color='RED',
                        background_color=theme.BG_BASE,
                        no_scrollbar=True,
                        highlight_background_color=theme.BG_PRIMARY,
                        text_color=theme.TEXT_PRIMARY,
                        highlight_text_color=theme.TEXT_PRIMARY,
                        sbar_width=theme.BD_ACCENT,
                        font=(theme.FONT_FAMILY, theme.H3_SIZE),
                        enable_events=True,
                        key='-ENABLE-'
                        )

_select_profile_layout = [
    [_user_list],
    [_current_user]
]

_add_user_button = sg.Button('Añadir',
                             key=EVENT_SAVE_PROFILE,
                             button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                             mouseover_colors=theme.BG_BUTTON_HOVER,
                             font=(theme.FONT_FAMILY, theme.T1_SIZE),
                             pad=theme.scale(40),
                             disabled=True)

_create_layout = [
    [
        sg.Text('    ! Nuevo perfil !',
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H2_SIZE),
                pad=theme.scale(10)
                )
    ],
    [
        sg.Text('Nick',
                size=(6, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H2_SIZE),
                pad=theme.scale(25)
                ),
        sg.Input(size=(20, 1),
                 background_color=theme.BG_BASE,
                 font=(theme.FONT_FAMILY, theme.H2_SIZE),
                 text_color=theme.TEXT_ACCENT,
                 border_width=theme.BD_PRIMARY
                 )
    ],
    [
        sg.Text('Edad',
                size=(6, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H2_SIZE),
                pad=theme.scale(25)
                ),
        sg.Input(size=(20, 1),
                 background_color=theme.BG_BASE,
                 font=(theme.FONT_FAMILY, theme.H2_SIZE),
                 text_color=theme.TEXT_ACCENT,
                 border_width=theme.BD_PRIMARY
                 )
    ],
    [
        sg.Text('Género', size=(6, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H2_SIZE),
                pad=theme.scale(25)),

        sg.Input(size=(20, 1),
                 background_color=theme.BG_BASE,
                 font=(theme.FONT_FAMILY, theme.H2_SIZE),
                 text_color=theme.TEXT_ACCENT,
                 border_width=theme.BD_PRIMARY
                 )
    ],
    [
        _add_user_button
    ],
]


_screen_layout = [
    [
        common.screen_title('Seleccionar perfiles', alignment='center')
    ],

    [
        sg.Column(_select_profile_layout,
                  background_color=theme.BG_BASE,
                  element_justification='center',
                  justification='left',
                  expand_y=True,
                  expand_x=True,
                  pad=theme.scale(10)
                  ),
        sg.Column(_create_layout,
                  background_color=theme.BG_BASE,
                  element_justification='center',
                  justification='rigth',
                  pad=theme.scale(10)
                  #   expand_y=True,
                  #   expand_x=True,
                  )
    ],
    [
        csg.CenteredElement(_confirm_button,
                            horizontal_only=True,
                            background_color=theme.BG_BASE
                            )
    ]
]


def confirm():
    _confirm_button.update(disabled=False)
    _current_user.update(f'Selecionado: {_user_list.get()[0]}',font=(theme.FONT_FAMILY,theme.H3_SIZE))


observer.subscribe('-ENABLE-', confirm)


def reset(*args):
    pass


_screen_config = {
    'background_color': theme.BG_BASE,
}

screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
