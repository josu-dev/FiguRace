import PySimpleGUI as sg
from src import constants as const
from src.controllers import theme
from src.handlers.layout import Screen
from src import csg
# from src.controllers import cards_controller as cards_ctr
_font = ('System', 32)
_default_padding = 2
SCREEN_NAME = "-GAME-"
MAIN_BACK_COLOR = '#112B3C'


def _title() -> sg.Text:
    return sg.Text(' G A M E ', size=(800, 1),
                   background_color=theme.BG_BASE,
                   text_color='#EFEFEF',
                   key='-title-',
                   font=('System', 86),
                   justification='center',
                   pad=64,)


_btn_back = sg.Button('<-- Volver',
                      auto_size_button=True,
                      key=f'{const.GOTO_VIEW} -MENU-',
                      font=_font,
                      button_color=(theme.TEXT_PRIMARY,
                                    theme.BG_BUTTON),
                      pad=_default_padding,
                      mouseover_colors=theme.BG_BUTTON_HOVER,
                      border_width=12)
_btn_score = sg.Button('Score -->',
                       auto_size_button=True,
                       key=f'{const.GOTO_VIEW} -SCORE-',
                       font=_font,
                       button_color=(theme.TEXT_PRIMARY,
                                     theme.BG_BUTTON),
                       pad=_default_padding,
                       mouseover_colors=theme.BG_BUTTON_HOVER,
                       border_width=12)


def layout() -> list[list[sg.Element]]:
    layout = [
        [sg.VPush(background_color=theme.BG_BASE)],
        [_btn_back, sg.Push(), sg.Text(),
         sg.Push(), _btn_score],
    ]
    return layout


# All the stuff inside your window.
_screen_layout = [
    [_title(), ],
    [sg.Column(layout(), background_color=theme.BG_BASE, expand_x=True, expand_y=True,
               element_justification='left')],
]

_screen_config = {
    'background_color': theme.BG_BASE,
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
