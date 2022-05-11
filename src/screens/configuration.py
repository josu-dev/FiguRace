import PySimpleGUI as sg
from src import constants as const
from src.handlers.theme import theme
from src.handlers.layout import Screen
SCREEN_NAME = "-CONFIGURATION-"

# Vertical Space


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=theme.BG_BASE)

# Horizontal Space


def _h_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding)


def _title() -> sg.Text:
    return sg.Text('C O N F I G U R A T I O N S', size=(800, 1), background_color=theme.BG_BASE, text_color=theme.TEXT_ACCENT, key='-title-', font=('System', 76), justification='center', pad=64)


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


def _menu_options():
    default_padding = 16
    config_layout = [
        [_h_spacer((50, 0)),
         sg.Multiline('Time per game ',
                      disabled=True,
                      font=('System', 25),
                      size=(16, 1),
                      text_color=theme.TEXT_ACCENT,
                      no_scrollbar=True,
                      background_color=theme.BG_BASE,
                      pad=default_padding,
                      border_width=12,
                      justification='center'),

         sg.Text('Seconds ', background_color=theme.BG_BASE),
         _cmb_time_per_game,


         sg.Push(),

         sg.Multiline('Features per level', size=(16, 1),
                      font=('System', 25),
                      disabled=True,
                      text_color=theme.TEXT_ACCENT,
                      no_scrollbar=True,
                      background_color=theme.BG_BASE,
                      pad=default_padding,
                      border_width=12),
         sg.Text('Amount  ', background_color=theme.BG_BASE),

         _cmb_features_per_level

         ],

        [_h_spacer((50, 0)),
         sg.Multiline('Rounds per game',
                      text_color=theme.TEXT_ACCENT,
                      size=(16, 1),
                      disabled=True,
                      font=('System', 25),
                      background_color=theme.BG_BASE,
                      pad=default_padding,
                      no_scrollbar=True,
                      border_width=12),
         sg.Text('Rounds   ', background_color=theme.BG_BASE),
         _cmb_rounds_per_game,
         sg.Push(),
         sg.Multiline('Points added',
                      text_color=theme.TEXT_ACCENT,
                      no_scrollbar=True,
                      auto_size_text=True,
                      size=(16, 1),
                      disabled=True,
                      background_color=theme.BG_BASE,
                      font=('System', 25),
                      pad=default_padding,
                      border_width=12),
         sg.Text('Correct  ', background_color=theme.BG_BASE),
         _cmb_plus_points,
         ],
        [_h_spacer((50, 0)),
            sg.Multiline('Points substracted',
                         text_color=theme.TEXT_ACCENT,
                         no_scrollbar=True,
                         auto_size_text=True,
                         size=(16, 1),
                         disabled=True,
                         background_color=theme.BG_BASE,
                         font=('System', 25),
                         pad=default_padding,
                         border_width=12),
         sg.Text('Wrong    ', background_color=theme.BG_BASE),
         _cmb_sub_points,
         sg.Push()],

        [sg.Push(),
         _v_spacer((0, 350)),
            sg.Button('<--',
                      key=f'{const.GOTO_VIEW} -MENU-',
                      border_width=12,
                      size=(16, 1),
                      button_color=(
                          theme.TEXT_ACCENT, theme.BG_BASE),
                      mouseover_colors=theme.BG_BASE,
                      font=('System', 25)),

            sg.Button('Save Changes', size=(16, 1),
                      key='-SAVE-',
                      font=('System', 25),
                      button_color=(theme.TEXT_ACCENT, theme.BG_BASE),
                      pad=default_padding,
                      mouseover_colors=theme.BG_BASE,
                      border_width=12),
            sg.Push(), ]]

    return config_layout


_screen_layout = [
    [_title()],
    [sg.Column(_menu_options())],
]

_screen_config = {
    'background_color':theme.BG_BASE
}

def reset(*args):
    # Funcions
    pass


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)

if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Figurace -' + SCREEN_NAME, _configuration_layout,
                       background_color=theme.BG_BASE).Finalize()
    window.Maximize()

    while True:     # Event Loop
        event, values = window.read()

        if event in ('-SAVE-',):  # SAVE CONFIG
            # TODO SAVE DATA
            # db.saveConfigurations()
            print('Saving time per game ' + values['-TIME-'])
            print('Saving Features per level ' + values['-CARXLEVEL-'])
            print('Saving Rounds per game ' + values['-QROUNDS-'])
            print('Saving Points added ' + values['-+QXANSWER-'])
            print('Saving Points substracted ' + values['--QXANSWER-'])

        if event in (sg.WIN_CLOSED, ):  # WIN CLOSED BY OS
            break
    window.close()
