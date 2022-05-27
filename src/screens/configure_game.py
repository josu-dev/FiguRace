from random import shuffle
import PySimpleGUI as sg
from src import constants as const, csg, common
from src.controllers import theme
from src.handlers.layout import Screen
from src.controllers import users_controller as users_ctr
from src.handlers.user import User
from src.controllers import difficulty_controller as difficulty_ctr
from src.handlers import observer
from src.controllers import cards_controller as cards_ctr
SCREEN_NAME = '-CONFIGGAME-'

_text_font = ('System', int(theme.H3_SIZE))
_h2_font = ('System', int(theme.H2_SIZE))
_padding = int(theme.width / 4)


def get_name(user: User) -> tuple[str]:
    return user.nick


def get_users() -> tuple:
    users = users_ctr.user_list
    if users:
        return users_ctr.users_transform(get_name)
    else:
        return ('Sin Usuarios'),


def get_user() -> str:
    users = users_ctr.user_list
    if users:
        return users_ctr.current_user.nick
    else:
        return 'Sin usuarios'


_cmb_difficulty = sg.Combo(('Fácil', 'Intermedio', 'Difícil', 'Insano', 'Personalizada'),
                           'Intermedio',
                           background_color='#8DC3E4',
                           font=_text_font,
                           text_color=theme.BG_BASE,
                           readonly=True,
                           size=(15, 30),
                           enable_events=True,
                           pad=((50, 0), (50, 0)),
                           key='-CHANGE-DIFFICULT-')


_cmb_dataset = sg.Combo(tuple(cards_ctr.types) + ('Random',),
                        'Random',
                        background_color='#8DC3E4',
                        pad=((50, 0), (50, 0)),
                        font=_text_font,
                        text_color=theme.BG_BASE,
                        readonly=True,
                        enable_events=True,
                        size=(15, 30),
                        key='-CHANGE-DATA-')


def combo_boxes() -> list:
    return [csg.horizontal_spacer(_padding, background_color=theme.BG_BASE),
            _cmb_difficulty,
            sg.Push(background_color=theme.BG_BASE),
            _cmb_dataset,
            csg.horizontal_spacer(_padding, background_color=theme.BG_BASE)]


_btn_goto_game = sg.Button('Empezar ! ',
                           key=f'{const.GOTO_VIEW} -GAME-',
                           font=_h2_font,
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
                      font=_h2_font)


def header() -> list:
    return [csg.horizontal_spacer(_padding,
                                  background_color=theme.BG_BASE),
            sg.Text('ELEGIR DIFICULTAD', pad=((50, 0), (50, 0)),
                    background_color=theme.BG_BASE, font=_text_font),
            sg.Push(background_color=theme.BG_BASE),
            sg.Text('ELEGIR DATASET', pad=((50, 0), (50, 0)),
                    background_color=theme.BG_BASE, font=_text_font),
            csg.horizontal_spacer(_padding,
                                  background_color=theme.BG_BASE)
            ]


_difficulty_info = sg.Multiline(f"Tiempo por ronda : {difficulty_ctr.difficulty.time_per_round}\
            Q de Características : {difficulty_ctr.difficulty.characteristics_shown}\
            Rounds por juego : {difficulty_ctr.difficulty.rounds_per_game}\
            Puntos añadidos : {difficulty_ctr.difficulty.points_correct_answer}\
            Puntos Restados : {difficulty_ctr.difficulty.points_bad_answer}",
                                auto_size_text=True,
                                disabled=True,
                                size=(20, 5),
                                font=_text_font,
                                border_width=0,
                                text_color=theme.TEXT_ACCENT,
                                no_scrollbar=True,
                                background_color=theme.BG_BASE,
                                key='-DIFFCAR-',
                                pad=((50, 0), (50, 0)))


def build_text():
    return [csg.horizontal_spacer(_padding,
                                  background_color=theme.BG_BASE),
            _difficulty_info]


def layout() -> list[list[sg.Element]]:
    layout = [
        [csg.vertical_spacer((0, 24), background_color=theme.BG_BASE)],
        header(),
        combo_boxes(),
        build_text(),
        [sg.VPush(background_color=theme.BG_BASE)],
        [_btn_back, sg.Push(background_color=theme.BG_BASE), _btn_goto_game],
    ]
    return layout


def refresh_info():
    difficulty_ctr.update_difficulty(
        const.DIFFICULTY_TO_EN[_cmb_difficulty.get()])
    _difficulty_info.update(f"Tiempo por ronda : {difficulty_ctr.difficulty.time_per_round}\
            Q de Características : {difficulty_ctr.difficulty.characteristics_shown}\
            Rounds por juego : {difficulty_ctr.difficulty.rounds_per_game}\
            Puntos añadidos : {difficulty_ctr.difficulty.points_correct_answer}\
            Puntos Restados : {difficulty_ctr.difficulty.points_bad_answer}")


def change_difficult():
    difficulty_ctr.update_difficulty(
        const.DIFFICULTY_TO_EN[_cmb_difficulty.get()])
    refresh_info()


def change_user():
    pass


def change_dataset():
    dataset = _cmb_dataset.get()
    if dataset == 'Random':
        shuffled = cards_ctr.types
        shuffle(shuffled)
        dataset = shuffled[0]
    cards_ctr.set_type(dataset)


def reset():
    refresh_info()
    pass


_configuration_layout = [
    [common.screen_title('CONFIGURAR JUEGO',
                         alignment='left', padding=int(theme.height/64))],
    [sg.Column(layout(), background_color=theme.BG_BASE, expand_y=True,
               expand_x=True, justification='right')],
]

_screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'c',
}


observer.subscribe(
    '-CHANGE-DIFFICULT-',
    change_difficult,
)

observer.subscribe(
    '-CHANGE-DATA-',
    change_dataset,
)

screen = Screen(
    SCREEN_NAME,
    _configuration_layout,
    _screen_config,
    reset
)
