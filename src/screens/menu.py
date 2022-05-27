import PySimpleGUI as sg
from src import constants as const, common, csg
from src.controllers import theme
from src.handlers.layout import Screen
from src.assets.menu import ic_profile, ic_exit, ic_config
from src.controllers import settings_controller as settings_ctr


SCREEN_NAME = "-MENU-"
_default_padding = 2
_font = ('System', 32)


_btn_start_game_ = sg.Button('Iniciar Juego',
                             key=f'{const.GOTO_VIEW} -CONFIGGAME-',
                             size=(18, 1),
                             font=_font,
                             auto_size_button=True,
                             button_color=(theme.TEXT_BUTTON,
                                           theme.BG_BUTTON),
                             pad=_default_padding,
                             mouseover_colors=theme.BG_BUTTON_HOVER,
                             border_width=12)
_btn_options = sg.Button(image_data=ic_config.source,
                         key=f'{const.GOTO_VIEW} -CONFIGURATION-',
                         auto_size_button=True,
                         font=_font,
                         button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
                         pad=_default_padding,
                         mouseover_colors=theme.BG_BUTTON_HOVER,
                         border_width=12)
_btn_profile = sg.Button(image_data=ic_profile.source,
                         key=f'{const.GOTO_VIEW} -SELECT-PROFILE-',
                         auto_size_button=True,
                         font=_font,
                         button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
                         pad=_default_padding,
                         mouseover_colors=theme.BG_BUTTON_HOVER,
                         border_width=12)
_btn_exit = sg.Button(auto_size_button=True,
                      key=const.EXIT_APLICATION,
                      font=_font,
                      button_color=theme.BG_BUTTON,
                      image_data=ic_exit.source,
                      pad=_default_padding,
                      mouseover_colors=theme.BG_BUTTON_HOVER,
                      border_width=12)


def _menu_options() -> list[list[sg.Element]]:
    layout = [
        [csg.vertical_spacer((0, 24), background_color=theme.BG_BASE)],
        [_btn_start_game_],
        [csg.vertical_spacer((0, 24), background_color=theme.BG_BASE)],
        [_btn_options, csg.horizontal_spacer((40, 0), background_color=theme.BG_BASE), _btn_profile,
         csg.horizontal_spacer((40, 0), background_color=theme.BG_BASE), _btn_exit]
    ]
    return layout


def reset():
    # Funcions
    pass


# All the stuff inside your window.
_screen_layout = [
    [common.screen_title('f  i  g  u  r  a  c  e',size=theme.H1_SIZE)],
    [sg.Column(_menu_options(), background_color=theme.BG_BASE, expand_y=True,
               element_justification='c')],
]

_screen_config = {
    'element_justification': 'c',
    'background_color': theme.BG_BASE,
}


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
