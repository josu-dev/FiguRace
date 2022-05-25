from random import shuffle
import PySimpleGUI as sg
from src import constants as const
from src.controllers import theme
from src.handlers.layout import Screen
from src import csg
from src.controllers import users_controller as users_ctr
from src.handlers.user import User
from src.controllers import settings_controller as sett_ctr
from src.handlers import observer
from src.controllers import cards_controller as cards_ctr
SCREEN_NAME = '-CONFIGGAME-'


def _get_name(user: User) -> tuple[str]:
    return user.nick


def _get_users() -> tuple:
    users = users_ctr.user_list
    if users:
        return users_ctr.users_transform(_get_name)
    else:
        return ('Sin Usuarios'),


def _get_user() -> str:
    users = users_ctr.user_list
    if users:
        return users_ctr.current_user.nick
    else:
        return 'Sin usuarios'


def _title() -> sg.Text:
    return sg.Text('CONFIGURAR JUEGO', size=(800, 1),
                   background_color=theme.BG_BASE,
                   text_color='#EFEFEF',
                   key='-title-',
                   font=(theme.FONT_FAMILY, 45),
                   justification='left'
                   )


_cmb_difficulty = sg.Combo(('Fácil', 'Intermedio', 'Difícil', 'Insano', 'Personalizada'),
                           'Intermedio',
                           background_color='#8DC3E4',
                           pad=(200, 50),
                           font=('System', 24),
                           text_color=theme.BG_BASE,
                           readonly=True,
                           size=(15, 30),
                           enable_events=True,
                           key='-CHANGEDIFFICULT-')

_cmb_profile = sg.Combo(_get_users(),
                        _get_user(),
                        background_color='#8DC3E4',
                        pad=(150, 50),
                        font=('System', 24),
                        text_color=theme.BG_BASE,
                        readonly=True,
                        size=(15, 30),
                        key=f'{const.USER_CHANGE} ')


def _combo_boxes():
    return [_cmb_difficulty, sg.Push(background_color=theme.BG_BASE), _cmb_profile, csg.horizontal_spacer((100, 0), background_color=theme.BG_BASE)]


_btn_goto_game = sg.Button('Empezar ! ',
                           key=f'{const.GOTO_VIEW} -GAME-',
                           font=('System', 32),
                           auto_size_button=True,
                           button_color=(theme.TEXT_BUTTON,
                                         theme.BG_BUTTON),
                           pad=2,
                           mouseover_colors=theme.BG_BUTTON_HOVER,
                           border_width=12)

_btn_back = sg.Button('<--',
                      key=f'{const.GOTO_VIEW} -MENU-',
                      border_width=12,
                      button_color=(theme.TEXT_BUTTON,
                                    theme.BG_BUTTON),
                      mouseover_colors=theme.BG_BUTTON_HOVER,
                      font=('System', 32))


def _header():
    return [sg.Text('ELEGIR DIFICULTAD', pad=(200, 0),
                    background_color=theme.BG_BASE, font=('System', 24)),
            sg.Push(background_color=theme.BG_BASE),
            sg.Text('ELEGIR PERFIL', pad=(300, 0),
                    background_color=theme.BG_BASE, font=('System', 24)),
            ]


_difficulty_info = sg.Multiline(f"Tiempo por ronda : {sett_ctr.difficulty.time_per_round}\
            Q de Características : {sett_ctr.difficulty.caracteristics_shown}\
            Rounds por juego : {sett_ctr.difficulty.rounds_per_game}\
            Puntos añadidos : {sett_ctr.difficulty.points_correct_answer}\
            Puntos Restados : {sett_ctr.difficulty.points_bad_answer}",
                                auto_size_text=True,
                                disabled=True,
                                size=(20, 5),
                                font=('System', 20),
                                border_width=0,
                                text_color=theme.TEXT_ACCENT,
                                no_scrollbar=True,
                                background_color=theme.BG_BASE,
                                key='-DIFFCAR-',
                                pad=((200, 10), (10, 10)),)


def _build_text():
    return [_difficulty_info]


_cmb_dataset = sg.Combo(tuple(cards_ctr.types) + ('Random',),
                        'Random',
                        background_color='#8DC3E4',
                        pad=((0, 260), (10, 10)),
                        font=('System', 24),
                        text_color=theme.BG_BASE,
                        readonly=True,
                        enable_events=True,
                        size=(15, 30),
                        key='-CHANGE-DATA-')


def _select_dataset() -> sg.Combo:
    return _cmb_dataset


def layout() -> list[list[sg.Element]]:
    layout = [
        [csg.vertical_spacer((0, 24), background_color=theme.BG_BASE)],
        _header(),
        _combo_boxes(),
        _build_text(),
        [sg.Push(background_color=theme.BG_BASE), sg.Text('ELEGIR DATASET', pad=((0, 280), (10, 10)),
                                                          background_color=theme.BG_BASE, font=('System', 24)), ],
        [sg.Push(background_color=theme.BG_BASE), _select_dataset(), ],
        [sg.VPush(background_color=theme.BG_BASE)],
        [_btn_back, sg.Push(background_color=theme.BG_BASE), _btn_goto_game],
    ]
    return layout


def _refresh_info():
    sett_ctr.difficulty_controller.update_difficulty(
        const.DIFFICULTY_TO_EN[_cmb_difficulty.get()])
    _difficulty_info.update(f"Tiempo por ronda : {sett_ctr.difficulty.time_per_round}\
            Q de Características : {sett_ctr.difficulty.caracteristics_shown}\
            Rounds por juego : {sett_ctr.difficulty.rounds_per_game}\
            Puntos añadidos : {sett_ctr.difficulty.points_correct_answer}\
            Puntos Restados : {sett_ctr.difficulty.points_bad_answer}")


def _check_user():
    if(_cmb_profile.get() == 'Sin usuarios'):
        return True
    return False


def _change_difficult():
    sett_ctr.difficulty_controller.update_difficulty(
        const.DIFFICULTY_TO_EN[_cmb_difficulty.get()])
    _refresh_info()


def _change_user():
    users_ctr.current_user = _cmb_profile.get()
    sett_ctr.setting.default_user = _cmb_profile.get()


def _change_dataset():
    dataset = _cmb_dataset.get()
    if dataset == 'Random':
        shuffled = cards_ctr.types
        shuffle(shuffled)
        dataset = shuffled[0]
    cards_ctr.set_type(dataset)


_configuration_layout = [
    [_title()],
    [sg.Column(layout(), background_color=theme.BG_BASE, expand_y=True,
               expand_x=True, justification='right')],
]

_screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'c',
}


def reset():
    _btn_goto_game.update(disabled=_check_user())
    _refresh_info()
    pass


observer.subscribe(
    '-CHANGEDIFFICULT-',
    _change_difficult,
)
observer.subscribe(
    const.USER_CHANGE,
    _change_user,
)
observer.subscribe(
    '-CHANGE-DATA-',
    _change_dataset,
)

screen = Screen(
    SCREEN_NAME,
    _configuration_layout,
    _screen_config,
    reset
)
