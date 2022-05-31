import PySimpleGUI as sg

from src import constants as const, common, csg
from src.controllers import theme
from src.handlers.screen import Screen
from src.assets.menu import ic_profile, ic_setting, ic_score
from src.assets import title


SCREEN_NAME = "-MENU-"
_default_padding = 2
ICON_BUTTON_SIZE = (theme.scale(96), theme.scale(96))
TEXT_BUTTON_FONT = (theme.FONT_FAMILY, theme.H3_SIZE)


def menu_options() -> sg.Column:
    layout = [
        [csg.vertical_spacer(theme.scale(24), background_color=theme.BG_BASE)],
        [sg.Button(
            'Iniciar Partida',
            key=f'{const.GOTO_VIEW} -CONFIGURE-GAME-',
            size=(16, 1),
            font=TEXT_BUTTON_FONT,
            auto_size_button=True,
            button_color=(theme.TEXT_BUTTON,
                          theme.BG_BUTTON),
            pad=_default_padding,
            mouseover_colors=theme.BG_BUTTON_HOVER,
            border_width=theme.BD_ACCENT
        )],
        [csg.vertical_spacer(theme.scale(24), background_color=theme.BG_BASE)],
        [
            common.image_button(
                ic_profile,
                ICON_BUTTON_SIZE,
                border=theme.BD_ACCENT,
                key=f'{const.GOTO_VIEW} -SELECT-PROFILE-'
            ),
            csg.horizontal_spacer(
                theme.scale(16), background_color=theme.BG_BASE
            ),
            common.image_button(
                ic_setting,
                ICON_BUTTON_SIZE,
                border=theme.BD_ACCENT,
                key=f'{const.GOTO_VIEW} -CONFIGURATION-'
            ),
            csg.horizontal_spacer(
                theme.scale(16), background_color=theme.BG_BASE
            ),
            common.image_button(
                ic_score,
                ICON_BUTTON_SIZE,
                border=theme.BD_ACCENT,
                key=f'{const.GOTO_VIEW} -RANKING-'
            )
        ],
        [csg.vertical_spacer(theme.scale(24), background_color=theme.BG_BASE)],
        [sg.Button(
            'Salir',
            key=const.EXIT_APLICATION,
            size=(16, 1),
            font=TEXT_BUTTON_FONT,
            auto_size_button=True,
            button_color=(theme.TEXT_BUTTON,
                          theme.BG_BUTTON),
            pad=_default_padding,
            mouseover_colors=theme.BG_BUTTON_HOVER,
            border_width=theme.BD_ACCENT
        )],
    ]
    return sg.Column(
        layout,
        background_color=theme.BG_BASE,
        element_justification='center',
        expand_y=True,
    )


def reset():
    pass


screen_layout = [
    [sg.VPush(theme.BG_BASE)],
    [sg.Image(
        data=title.source,
        size=(theme.scale(1080), theme.scale(128)),
        subsample=title.size//theme.scale(800),
        background_color=theme.BG_BASE,
        pad=theme.scale(48)
    )],
    [menu_options()],
    [sg.VPush(theme.BG_BASE)],
]

screen_config = {
    'element_justification': 'center',
    'background_color': theme.BG_BASE,
}


screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
