from os import remove
import PySimpleGUI as sg

from src import constants as const, csg, common
from src.controllers import theme, users_controller as users_ctr
from src.handlers import observer
from src.handlers.screen import Screen


SCREEN_NAME = '-SELECT-PROFILE-'
EVENT_CREATE_PROFILE = '-CREATE-PROFILE-'
EVENT_REMOVE_PROFILE = '-REMOVE-PROFILE-'
EVENT_EDIT_PROFILE = '-EDIT-PROFILE-'
EVENT_ADD_PROFILE = '-ADD-PROFILE-'
LOAD_USER_FIELD = '-LOAD-FIELD-'


_play_button = sg.Button('-<-Jugar->-',
                         key=f'{const.GOTO_VIEW} -MENU-',
                         border_width=theme.BD_ACCENT,
                         button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                         mouseover_colors=theme.BG_BUTTON_HOVER,
                         font=(theme.FONT_FAMILY, theme.T1_SIZE),
                         disabled=True,
                         pad=(theme.scale(100), theme.scale(50))
                         )

_current_user = sg.Text('Seleccionado:',
                        background_color=theme.BG_BASE,
                        font=(theme.FONT_FAMILY, theme.H3_SIZE),
                        size=(24, 1)
                        )

_user_list = sg.Listbox(values=users_ctr.users_transform(lambda user: user.nick),
                        expand_y=True,
                        size=(25, 10),
                        background_color=theme.BG_BASE,
                        no_scrollbar=True,
                        highlight_background_color=theme.BG_PRIMARY,
                        text_color=theme.TEXT_PRIMARY,
                        highlight_text_color=theme.TEXT_PRIMARY,
                        font=(theme.FONT_FAMILY, theme.H3_SIZE),
                        enable_events=True,
                        key='-ENABLE-',
                        )

_remove_button = sg.Button(
    button_text='Eliminar',
    key='-REMOVE-PROFILE-',
    border_width=theme.BD_ACCENT,
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    mouseover_colors=theme.BG_BUTTON_HOVER,
    font=(theme.FONT_FAMILY, theme.T1_SIZE),
    disabled=True,
    pad=theme.scale(30),
    enable_events=True
)


_select_profile_layout = [
    [_current_user],
    [_user_list]
]

_edit_button = common.navigation_button(
    'Editar',
    '-CONFIGURATION-',
    border=theme.BD_ACCENT,
    padding=(theme.scale(30),)*2
)

_button_layout = [
    [
        common.navigation_button(
            'Crear',
            '-CREATE-USER-',
            border=theme.BD_ACCENT,
            padding=(theme.scale(30),)*2,
        )
    ],
    [
        _edit_button
    ],
    [
        _remove_button
    ]

]

_play_layout = [
    [_play_button]
]
screen_layout = [
    [
        common.screen_title('Seleccionar perfiles', alignment='center')
    ],
    [
        csg.horizontal_spacer(width=theme.scale(
            500),
            background_color=theme.BG_BASE
        ),
        sg.Column(_select_profile_layout,
                  background_color=theme.BG_BASE,
                  element_justification='center',
                  justification='left',
                  expand_y=True,
                  pad=theme.scale(40)
                  ),
        csg.horizontal_spacer(width=theme.scale(
            200),
            background_color=theme.BG_BASE
        ),
        sg.Column(
            _button_layout,
            justification='center',
            element_justification='center',
            background_color=theme.BG_BASE)
    ],
    [sg.Column(
        _play_layout,
        justification='center',
        expand_x=True,
        element_justification='center',
        background_color=theme.BG_BASE
    )
    ],
]


def confirm():
    _play_button.update(disabled=False)
    _remove_button.update(disabled=False)
    _edit_button.update(disabled=False)
    _current_user.update(f'Selecionado: {_user_list.get()[0]}', font=(
        theme.FONT_FAMILY, theme.H3_SIZE))
    users_ctr.current_user = _user_list.get()[0]


observer.subscribe('-ENABLE-', confirm)


def update_user_list():
    _user_list.update(values=users_ctr.users_transform(lambda user: user.nick))


def reset_select_user():
    _play_button.update(disabled=True)
    _remove_button.update(disabled=True)
    _edit_button.update(disabled=True)
    _current_user.update('Seleccionado: ')


def reset():
    update_user_list()
    reset_select_user()


def remove():
    users_ctr.remove(_user_list.get()[0])
    reset()


observer.subscribe('-REMOVE-PROFILE-', remove)

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'rigth'
}

screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
