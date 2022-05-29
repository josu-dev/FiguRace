from random import shuffle

import PySimpleGUI as sg

from src import constants as const, csg, common
from src.controllers import theme, cards_controller as cards_ctr, difficulty_controller as difficulty_ctr
from src.handlers import observer
from src.handlers.screen import Screen


SCREEN_NAME = '-CONFIGURE-GAME-'


_text_font = ('System', theme.H3_SIZE)
_padding = theme.width // 4


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


_cmb_dataset = sg.Combo(('Lagos Argentina', 'Spotify', 'FIFA 21', 'Random'),
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


def build_text() -> list:
    return [csg.horizontal_spacer(_padding,
                                  background_color=theme.BG_BASE),
            _difficulty_info]


def layout() -> list[list[sg.Element]]:
    layout = [
        [csg.vertical_spacer(theme.scale(24), background_color=theme.BG_BASE)],
        header(),
        combo_boxes(),
        build_text(),
        [sg.VPush(background_color=theme.BG_BASE)],
        [common.goback_button('<--'),
         sg.Push(background_color=theme.BG_BASE), common.navigation_button(
             'Empezar !', screen_name='-GAME-')
         ],
    ]
    return layout


def refresh_info() -> None:
    difficulty_ctr.set_difficulty(
        const.DIFFICULTY_TO_EN[_cmb_difficulty.get()])
    _difficulty_info.update(f"Tiempo por ronda : {difficulty_ctr.difficulty.time_per_round}\
            Q de Características : {difficulty_ctr.difficulty.characteristics_shown}\
            Rounds por juego : {difficulty_ctr.difficulty.rounds_per_game}\
            Puntos añadidos : {difficulty_ctr.difficulty.points_correct_answer}\
            Puntos Restados : {difficulty_ctr.difficulty.points_bad_answer}")


def change_difficult() -> None:
    difficulty_ctr.set_difficulty(
        const.DIFFICULTY_TO_EN[_cmb_difficulty.get()])
    refresh_info()


def change_dataset() -> None:
    dataset = _cmb_dataset.get()
    if dataset == 'Random':
        shuffled = cards_ctr.types
        shuffle(shuffled)
        dataset = shuffled[0]
    else:
        dataset = const.DATASET_TO_EN[dataset]
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
