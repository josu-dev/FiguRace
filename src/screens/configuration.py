import PySimpleGUI as sg
from src import constants as const
from src.handlers.theme import theme
from src.handlers.layout import Screen


SCREEN_NAME = "-CONFIGURATION-"
default_padding = 16

# Vertical Space


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=theme.BG_BASE)

# Horizontal Space


def _h_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding)


def _title() -> sg.Text:
    return sg.Text('C O N F I G U R A C I Ó N ', auto_size_text=True, background_color=theme.BG_BASE, text_color=theme.TEXT_ACCENT, key='-title-', font=('System', 76), justification='center', pad=64)


def _build_text(text, unit, combo, lines):
    result = [sg.Multiline(text,
                           disabled=True,
                           font=('System', 25),
                           size=(16, lines),
                           text_color=theme.TEXT_ACCENT,
                           no_scrollbar=True,
                           background_color=theme.BG_BASE,
                           pad=default_padding,
                           border_width=12,
                           justification='center'),
              sg.Text(unit, background_color=theme.BG_BASE),

              combo, ]
    return result


    # TODO parameters to the other screens
    # TODO db.loadConfigurations(time_per_game,rounds_per_game,points_added,point_substracted,features_per_level)
_time_per_game = 60
_rounds_per_game = 5
_points_added = 10
_points_substracted = 10
_features_per_level = 3


_cmb_time_per_game = sg.Combo(
    ('15', '30', '60', '90', '180', '300'),
    _time_per_game,
    background_color='#8DC3E4',
    text_color=theme.BG_BASE,
    font=('System', 24),
    size=(5, 40),
    readonly=True,
    key='-TIME-',)

_cmb_features_per_level = sg.Combo(('1', '2', '3', '4', '5'),
                                   _features_per_level,
                                   background_color='#8DC3E4',
                                   text_color=theme.BG_BASE,
                                   font=('System', 24),
                                   readonly=True,
                                   size=(5, 30),
                                   key='-CARXLEVEL-', )

_cmb_rounds_per_game = sg.Combo(('3', '5', '8', '10', '20'),
                                _rounds_per_game,
                                background_color='#8DC3E4',
                                text_color=theme.BG_BASE,
                                font=('System', 24),
                                readonly=True,
                                size=(5, 24),
                                key='-QROUNDS-',)

_cmb_plus_points = sg.Combo(('1', '5', '10', '25', '50'),
                            _points_added,
                            background_color='#8DC3E4',
                            text_color=theme.BG_BASE,
                            font=('System', 24),
                            readonly=True,
                            size=(5, 24),
                            key='-+QXANSWER-',)

_cmb_sub_points = sg.Combo(('1', '5', '10', '25', '50'),
                           _points_substracted,
                           background_color='#8DC3E4',
                           font=('System', 24),
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
                      font=('System', 25))

_btn_save = sg.Button('Guardar', size=(16, 1),
                      key='-SAVE-',
                      font=('System', 25),
                      button_color=(theme.TEXT_ACCENT, theme.BG_BASE),
                      pad=default_padding,
                      mouseover_colors=theme.BG_BASE,
                      border_width=12)


def _menu_options() -> list[list]:
    config_layout = [
        [_h_spacer((50, 0)),
         *_build_text('Tiempo de partida', 'Segundos:',
                      _cmb_time_per_game, 1),

         sg.Push(),

         *_build_text('  Caracteristicas \n  por nivel', 'Cantidad: ',
                      _cmb_features_per_level, 2)
         ],

        [_h_spacer((50, 0)),
         *_build_text('Rounds por juego', 'Cantidad: ',
                      _cmb_rounds_per_game, 1),

         sg.Push(),

         *_build_text('Puntos añadidos', 'Cantidad: ',
                      _cmb_plus_points, 1),

         ],
        [_h_spacer((50, 0)),
            *_build_text('Puntos restados', 'Cantidad: ',
                         _cmb_sub_points, 1),

         sg.Push()],

        [sg.Push(),
         _v_spacer((0, 350)),
            _btn_exit,

            _btn_save,
            sg.Push(), ]]

    return config_layout


_configuration_layout = [
    [_title()],
    [sg.Column(_menu_options(), background_color=theme.BG_BASE, expand_x=True)],
]

_screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'c'
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
