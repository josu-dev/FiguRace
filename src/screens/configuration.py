import PySimpleGUI as sg
from src import constants as const
from src.controllers import theme
from src.handlers.layout import Screen
from src import csg, common
from src.handlers import observer
from src.controllers import difficulty_controller as difficulty_ctr

SCREEN_NAME = "-CONFIGURATION-"
default_padding = 8
_font = ('System', theme.H3_SIZE)


def build_text(text, unit, combo, lines) -> list:
    result = [sg.Multiline(text,
                           disabled=True,
                           font=_font,
                           size=(16, lines),
                           text_color=theme.TEXT_ACCENT,
                           no_scrollbar=True,
                           background_color=theme.BG_BASE,
                           border_width=12,
                           justification='center'),
              sg.Text(unit, background_color=theme.BG_BASE),

              combo, ]
    return result


_cmb_time_per_game = sg.Combo(
    ('15', '30', '60', '90', '180', '300'),
    difficulty_ctr.difficulty.time_per_round,
    background_color='#8DC3E4',
    text_color=theme.BG_BASE,
    font=_font,
    size=(5, 40),
    readonly=True,
    key='-TIME-',)

_cmb_features_per_level = sg.Combo(('1', '2', '3', '4', '5'),
                                   difficulty_ctr.difficulty.characteristics_shown,
                                   background_color='#8DC3E4',
                                   text_color=theme.BG_BASE,
                                   font=_font,
                                   readonly=True,
                                   size=(5, 30),
                                   key='-CARXLEVEL-', )

_cmb_rounds_per_game = sg.Combo(('3', '5', '8', '10', '20'),
                                difficulty_ctr.difficulty.rounds_per_game,
                                background_color='#8DC3E4',
                                text_color=theme.BG_BASE,
                                font=_font,
                                readonly=True,
                                size=(5, 24),
                                key='-QROUNDS-',)

_cmb_plus_points = sg.Combo(('1', '5', '10', '25', '50'),
                            difficulty_ctr.difficulty.points_correct_answer,
                            background_color='#8DC3E4',
                            text_color=theme.BG_BASE,
                            font=_font,
                            readonly=True,
                            size=(5, 24),
                            key='-+QXANSWER-',)

_cmb_sub_points = sg.Combo(('1', '5', '10', '25', '50'),
                           difficulty_ctr.difficulty.points_bad_answer,
                           background_color='#8DC3E4',
                           font=_font,
                           text_color=theme.BG_BASE,
                           readonly=True,
                           size=(5, 30),
                           key='--QXANSWER-',)

_btn_exit = sg.Button('<--',
                      key=f'{const.GOTO_VIEW} -MENU-',
                      border_width=12,
                      size=(16, 1),
                      button_color=(
                          theme.TEXT_ACCENT, theme.BG_BASE),
                      mouseover_colors=theme.BG_BASE,
                      font=_font)

_btn_save = sg.Button('Guardar', size=(16, 1),
                      key='-SAVE-DIFF-CUSTOM-',
                      font=_font,
                      button_color=(theme.TEXT_ACCENT, theme.BG_BASE),
                      pad=default_padding,
                      mouseover_colors=theme.BG_BASE,
                      border_width=12)


def menu_options() -> list[list]:
    config_layout = [
        [csg.horizontal_spacer((50, 0), background_color=theme.BG_BASE),
         *build_text('Tiempo de partida', 'Segundos:',
                     _cmb_time_per_game, 1),

         sg.Push(),

         *build_text('  Caracteristicas \n  por nivel', 'Cantidad: ',
                     _cmb_features_per_level, 2)
         ],

        [csg.horizontal_spacer((50, 0), background_color=theme.BG_BASE),
         *build_text('Rounds por juego', 'Cantidad: ',
                     _cmb_rounds_per_game, 1),

         sg.Push(),

         *build_text('Puntos añadidos', 'Cantidad: ',
                     _cmb_plus_points, 1),

         ],
        [csg.horizontal_spacer((50, 0), background_color=theme.BG_BASE),
            *build_text('Puntos restados', 'Cantidad: ',
                        _cmb_sub_points, 1),

         sg.Push()],

        [sg.Push(),
         csg.vertical_spacer((0, 350), background_color=theme.BG_BASE),
            _btn_exit,

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
    [csg.vertical_spacer((0, int(theme.height/12)),
                         background_color=theme.BG_BASE)],
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
