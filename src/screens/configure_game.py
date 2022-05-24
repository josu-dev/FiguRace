import PySimpleGUI as sg
from src import constants as const
from src.handlers.theme import theme
from src.handlers.layout import Screen
from src import csg
from src.controllers import users_controller as users_ctr

SCREEN_NAME = '-CONFIGGAME-'


def _get_users() -> tuple:
    users = users_ctr.user_list
    if users:
        return tuple(users)
    else:
        return ('Sin Usuarios'),


def _is_empty() -> bool:
    users = users_ctr.user_list
    if users:
        return True
    else:
        return False


def _get_user() -> str:
    if _is_empty:
        return 'Sin usuarios'
    else:
        return users_ctr.current_user.nick,


def _title() -> sg.Text:
    return sg.Text('CONFIGURAR JUEGO', size=(800, 1),
                   background_color=theme.BG_BASE,
                   text_color='#EFEFEF',
                   key='-title-',
                   font=(theme.FONT_FAMILY, 45),
                   justification='left'
                   )


_btn_goto_game = sg.Button('Empezar ! ',
                           key=f'{const.GOTO_VIEW} -GAME-',
                           font=('System', 32),
                           auto_size_button=True,
                           button_color=(theme.TEXT_PRIMARY,
                                         theme.BG_BUTTON),
                           pad=2,
                           mouseover_colors=theme.BG_BUTTON_HOVER,
                           border_width=12)

_btn_back = sg.Button('<--',
                      key=f'{const.GOTO_VIEW} -MENU-',
                      border_width=12,
                      button_color=(
                          theme.TEXT_PRIMARY, theme.BG_BUTTON),
                      mouseover_colors=theme.BG_BASE,
                      font=('System', 32))


def _header():
    return [sg.Text('ELEGIR DIFICULTAD', pad=(200, 0),
                    background_color=theme.BG_BASE, font=('System', 24)),
            sg.Push(background_color=theme.BG_BASE),
            sg.Text('ELEGIR PERFIL', pad=(300, 0),
                    background_color=theme.BG_BASE, font=('System', 24)),
            ]


_cmb_difficulty = sg.Combo(('Fácil', 'Intermedio', 'Difícil', 'Personalizada'),
                           'Intermedio',
                           background_color='#8DC3E4',
                           pad=(200, 50),
                           font=('System', 24),
                           text_color=theme.BG_BASE,
                           readonly=True,
                           size=(15, 30),
                           key='-CHANGEDIFFICULT-')

_cmb_profile = sg.Combo(_get_users(),
                        _get_user(),
                        background_color='#8DC3E4',
                        pad=(150, 50),
                        font=('System', 24),
                        text_color=theme.BG_BASE,
                        readonly=True,
                        size=(15, 30),
                        key='-CHANGEPROFILE-')


def _combo_boxes():
    return [_cmb_difficulty, sg.Push(background_color=theme.BG_BASE), _cmb_profile, csg.horizontal_spacer((100, 0), background_color=theme.BG_BASE)]


def _build_text(text):
    result = sg.Multiline(text,
                          auto_size_text=True,
                          disabled=True,
                          font=('System', 20),
                          border_width=0,
                          text_color=theme.TEXT_ACCENT,
                          no_scrollbar=True,
                          background_color=theme.BG_BASE,
                          pad=((200, 10), (10, 10)),)

    return result


def _select_dataset() -> sg.Combo:
    return sg.Combo(('Spotify', 'Fifa', 'Lagos', 'Random'),
                    'Random',
                    background_color='#8DC3E4',
                    pad=((0, 260), (10, 10)),
                    font=('System', 24),
                    text_color=theme.BG_BASE,
                    readonly=True,
                    size=(15, 30),
                    key='-CHANGEDATA-')


def layout() -> list[list[sg.Element]]:
    layout = [
        [csg.vertical_spacer((0, 24), background_color=theme.BG_BASE)],
        _header(),
        _combo_boxes(),
        [_build_text('Tiempo por ronda : ')],
        [_build_text('Q de Características : ')],
        [_build_text('Rounds por juego : '), sg.Push(background_color=theme.BG_BASE), sg.Text('ELEGIR DATASET', pad=((0, 280), (10, 10)),
                                                                                              background_color=theme.BG_BASE, font=('System', 24)), ],
        [_build_text('Puntos añadidos : '), sg.Push(
            background_color=theme.BG_BASE), _select_dataset(), ],
        [_build_text('Puntos Restados : ')],
        [sg.VPush(background_color=theme.BG_BASE)],
        [_btn_back, sg.Push(background_color=theme.BG_BASE), _btn_goto_game],
    ]
    return layout


_configuration_layout = [
    [_title()],
    [sg.Column(layout(), background_color=theme.BG_BASE, expand_y=True,
               expand_x=True, justification='right')],


]

_screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'c',
}


def reset(*args):
    # Funcions
    pass


screen = Screen(
    SCREEN_NAME,
    _configuration_layout,
    _screen_config,
    reset
)
