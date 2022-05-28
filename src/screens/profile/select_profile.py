import PySimpleGUI as sg

from src import constants as const, csg, common

from src.controllers import theme, users_controller as users_ctr
from src.handlers import observer
from src.handlers.layout import Screen
from src.assets.users import *

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
                        sbar_width=theme.BD_ACCENT,
                        font=(theme.FONT_FAMILY, theme.H3_SIZE),
                        enable_events=True,
                        key='-ENABLE-',
                        )

_select_profile_layout = [
    [_user_list],
    [_current_user]
]

_add_user_button = sg.Button('Añadir',
                             button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                             mouseover_colors=theme.BG_BUTTON_HOVER,
                             font=(theme.FONT_FAMILY, theme.T1_SIZE),
                             pad=theme.scale(40),
                             disabled=True,
                             key=EVENT_ADD_PROFILE,
                             border_width=theme.BD_ACCENT
                             )

_input_nick = sg.Input(size=(20, 1),
                       background_color=theme.BG_BASE,
                       font=(theme.FONT_FAMILY, theme.H2_SIZE),
                       text_color=theme.TEXT_ACCENT,
                       border_width=theme.BD_PRIMARY,
                       key=f'{LOAD_USER_FIELD} 0',
                       enable_events=True
                       )

_input_age = sg.Input(size=(20, 1),
                      background_color=theme.BG_BASE,
                      font=(theme.FONT_FAMILY, theme.H2_SIZE),
                      text_color=theme.TEXT_ACCENT,
                      border_width=theme.BD_PRIMARY,
                      key=f'{LOAD_USER_FIELD} 1',
                      enable_events=True
                      )

_input_gender = sg.Input(size=(20, 1),
                         background_color=theme.BG_BASE,
                         font=(theme.FONT_FAMILY, theme.H2_SIZE),
                         text_color=theme.TEXT_ACCENT,
                         border_width=theme.BD_PRIMARY,
                         key=f'{LOAD_USER_FIELD} 2',
                         enable_events=True
                         )

_create_layout = [
    [
        sg.Text('    ! Nuevo perfil ¡',
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
        _input_nick
    ],
    [
        sg.Text('Edad',
                size=(6, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H2_SIZE),
                pad=theme.scale(25)
                ),
        _input_age
    ],
    [
        sg.Text('Género', size=(6, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H2_SIZE),
                pad=theme.scale(25)),
        _input_gender
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
        csg.CenteredElement(_play_button,
                            horizontal_only=True,
                            background_color=theme.BG_BASE
                            )
    ]
]


def confirm():
    _play_button.update(disabled=False)
    _current_user.update(f'Selecionado: {_user_list.get()[0]}', font=(
        theme.FONT_FAMILY, theme.H3_SIZE))
    users_ctr.current_user = _user_list.get()[0]

observer.subscribe('-ENABLE-', confirm)


def validate_nick():
    nick = _input_nick.get()
    if nick == '' or nick in users_ctr.users_transform(lambda user: user.nick):
        _input_nick.update(background_color='red')
        return False
    _input_nick.update(background_color=theme.BG_BASE)
    return True


def validate_age():
    age = _input_age.get()
    try:
        age = int(age)
        if age <= 0 or age > 100:
            raise ValueError
    except ValueError:
        _input_age.update(background_color='Red')
        return False
    _input_age.update(background_color=theme.BG_BASE)
    return True

def validate_gender ():
    gender = _input_gender.get() 
    if gender == '':
        _input_gender.update(background_color='red')
        return False
    _input_gender.update(background_color=theme.BG_BASE)
    return True

state = [False,False,False]

def validate_all(index):
    match index:
        case '0':state[0]=validate_nick()
        case '1':state[1]=validate_age()
        case '2':state[2]=validate_gender()
    disable = sum(state) != 3
    _add_user_button.update(disabled=disable)


observer.subscribe(LOAD_USER_FIELD, validate_all)

def update_user_list ():
    _user_list.update(values=users_ctr.users_transform(lambda user: user.nick))

def reset_formulary():
    _input_nick.update('')
    _input_age.update('')
    _input_gender.update('')
    _add_user_button.update(disabled=True)
    for i in range(len(state)):
        state[i]=False

def reset_select_user ():
    _play_button.update(disabled=True)
    _current_user.update('Seleccionado: ')

def save_data():
    users_ctr.add(_input_nick.get(),
                  int(_input_age.get()),
                  _input_gender.get()
                  )
    reset_formulary()
    update_user_list()

observer.subscribe(EVENT_ADD_PROFILE, save_data)


def reset():
    reset_formulary()
    update_user_list()
    reset_select_user()
    
_screen_config = {
    'background_color': theme.BG_BASE,
}

screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
