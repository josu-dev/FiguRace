import PySimpleGUI as sg
from src import constants as const
from src.handlers.theme import theme
from src.handlers.layout import Screen
from src import csg

_font = ('System', 32)
_default_padding = 2
SCREEN_NAME = "-SCORE-"
MAIN_BACK_COLOR = '#112B3C'


def _title() -> sg.Text:
    return sg.Text(' S C O R E ', size=(800, 1),
                   background_color=theme.BG_BASE,
                   text_color='#EFEFEF',
                   key='-title-',
                   font=('System', 86),
                   justification='center',
                   pad=64,)


_btn_back = sg.Button('FINISH',
                      auto_size_button=True,
                      key=f'{const.GOTO_VIEW} -MENU-',
                      font=_font,
                      button_color=theme.BG_BUTTON,
                      pad=_default_padding,
                      mouseover_colors=theme.BG_BUTTON_HOVER,
                      border_width=12)


def layout() -> list[list[sg.Element]]:
    layout = [
        [sg.VPush(background_color=theme.BG_BASE)],
        [sg.Push(), sg.Text('PLACEHOLDER JUEGUITO'),
         sg.Push(), _btn_back],
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
    # Functions
    pass


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
