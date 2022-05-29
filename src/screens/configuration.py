import PySimpleGUI as sg

from src import constants as const, csg, common
from src.controllers import theme, difficulty_controller as difficulty_ctr
from src.handlers import observer
from src.handlers.screen import Screen


SCREEN_NAME = "-CONFIGURATION-"
default_padding = 8
_font = (theme.FONT_FAMILY_TEXT, theme.T2_SIZE)
_padding = theme.width // 4


def build_text(text, unit, combo) -> list:
    result = [
        csg.horizontal_spacer(theme.width//6,
                              background_color=theme.BG_BASE),
        sg.Multiline(text,
                     disabled=True,
                     justification='left',
                     size=(30, 1),
                     font=_font,
                     text_color=theme.TEXT_ACCENT,
                     no_scrollbar=True,
                     background_color=theme.BG_BASE,
                     border_width=0,),
        csg.horizontal_spacer(theme.width//6,
                              background_color=theme.BG_BASE),
        sg.Text(unit, background_color=theme.BG_BASE),
        combo, ]
    return result


_cmb_time_per_game = sg.Combo(
    ('15', '30', '60', '90', '180', '300'),
    difficulty_ctr.difficulty.time_per_round,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    size=(3, 1),
    readonly=True,
    key='-TIME-',)

_cmb_features_per_level = sg.Combo(
    ('1', '2', '3', '4', '5'),
    difficulty_ctr.difficulty.characteristics_shown,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-CARXLEVEL-')

_cmb_rounds_per_game = sg.Combo(
    ('3', '5', '8', '10', '20'),
    difficulty_ctr.difficulty.rounds_per_game,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-QROUNDS-')

_cmb_plus_points = sg.Combo(
    ('1', '5', '10', '25', '50'),
    difficulty_ctr.difficulty.points_correct_answer,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-+QXANSWER-')

_cmb_sub_points = sg.Combo(
    ('-1', '-5', '-10', '-25', '-50'),
    difficulty_ctr.difficulty.points_bad_answer,
    background_color=theme.BG_BUTTON,
    font=_font,
    text_color=theme.BG_BASE,
    readonly=True,
    size=(3, 1),
    key='--QXANSWER-')


_btn_save = sg.Button(
    'Guardar', size=(16, 1),
    key='-SAVE-DIFF-CUSTOM-',
    font=('System', theme.H3_SIZE),
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    pad=default_padding,
    mouseover_colors=theme.BG_BUTTON_HOVER,
    border_width=theme.BD_PRIMARY)


def header() -> list:
    return [csg.horizontal_spacer(_padding,
                                  background_color=theme.BG_BASE),
            sg.Text('CONFIGURAR DIFICULTAD', pad=((50, 0), (50, 0)),
                    background_color=theme.BG_BASE, font=('System', theme.H3_SIZE)),
            sg.Push(background_color=theme.BG_BASE),
            sg.Text('EDITAR USUARIO', pad=((50, 0), (50, 0)),
                    background_color=theme.BG_BASE, font=('System', theme.H3_SIZE)),
            csg.horizontal_spacer(_padding,
                                  background_color=theme.BG_BASE)
            ]


def text_spacer() -> list:
    return [csg.vertical_spacer(theme.height//64, background_color=theme.BG_BASE)]


def menu_options() -> list[list]:
    config_layout = [
        header(),
        [csg.vertical_spacer(
            theme.height//16, background_color=theme.BG_BASE)],

        build_text('Tiempo de partida', 'Segundos:', _cmb_time_per_game),
        text_spacer(),

        build_text('Caracteristicas por nivel',
                   'Cantidad:  ', _cmb_features_per_level),
        text_spacer(),

        build_text('Rounds por juego', 'Cantidad:  ', _cmb_rounds_per_game),
        text_spacer(),

        build_text('Puntos añadidos ', 'Cantidad:  ', _cmb_plus_points),
        text_spacer(),

        build_text('Puntos restados', 'Cantidad:  ', _cmb_sub_points),
        text_spacer(),

        [sg.Push(),
         csg.vertical_spacer(theme.scale(350), background_color=theme.BG_BASE),
            common.navigation_button('<--', screen_name='-MENU-'),
            _btn_save,
            sg.Push(), ]]

    return config_layout


def save_settings() -> None:
    changes = {
        'time_per_round': int(_cmb_time_per_game.get()),
        'rounds_per_game': int(_cmb_rounds_per_game.get()),
        'points_correct_answer': int(_cmb_plus_points.get()),
        'points_bad_answer':  int(_cmb_sub_points.get()),
        'characteristics_shown': int(_cmb_features_per_level.get())
    }
    difficulty_ctr.update_difficulty(**changes)


def reset():
    pass


_configuration_layout = [
    [common.screen_title('Configuración', spaced=True,
                         alignment='center')],
    [sg.Column(menu_options(), background_color=theme.BG_BASE, expand_x=True)],
]

_screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'c'
}


observer.subscribe(
    '-SAVE-DIFF-CUSTOM-',
    save_settings,
)
screen = Screen(
    SCREEN_NAME,
    _configuration_layout,
    _screen_config,
    reset
)
