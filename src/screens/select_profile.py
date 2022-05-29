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
                         disabled=True
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

_select_profile_layout = [
    [_current_user],
    [_user_list]
]


screen_layout = [
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
                  pad=theme.scale(40)
                  )
    ],
    [
        csg.CenteredElement(
            _play_button,
            horizontal_only=True,
            background_color=theme.BG_BASE
        )
    ],
    [
        common.navigation_button('Crear', '-CREATE-USER-',)
    ]
]


def confirm():
    _play_button.update(disabled=False)
    _current_user.update(f'Selecionado: {_user_list.get()[0]}', font=(
        theme.FONT_FAMILY, theme.H3_SIZE))
    users_ctr.current_user = _user_list.get()[0]


observer.subscribe('-ENABLE-', confirm)


def update_user_list():
    _user_list.update(values=users_ctr.users_transform(lambda user: user.nick))


def reset_select_user():
    _play_button.update(disabled=True)
    _current_user.update('Seleccionado: ')


def reset():
    update_user_list()
    reset_select_user()


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
