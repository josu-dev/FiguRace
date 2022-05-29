import PySimpleGUI as sg

from src import constants, csg
from src.controllers import theme
from src.handlers.screen import Screen
from src.assets import icon, title_name


SCREEN_NAME = '-INTRODUCTION-'
SECONDS = 5


_icon = sg.Image(
        key='-ICON-',
        data=title_name.source,
        background_color='black',
        size=(theme.scale(1920),theme.scale(128)),
        subsample=title_name.size//theme.scale(1080))

_black = sg.Button(
                  key=f'{constants.GOTO_VIEW} -SELECT-PROFILE-',
                  visible=True,
                  button_color='Black',
                  enable_events=True,
                  expand_y=True,
                  expand_x=True,
                  size=(10,10),
                  border_width=0,
                  image_data=icon.source,
                  image_size=(theme.scale(300),theme.scale(300)),
                  image_subsample=(icon.size // theme.scale(300))
                  )

screen_layout = [
    [
        csg.CenteredElement(_icon, background_color='black',)
    ],
    [
        _black
    ]
]

def reset() -> None:
    pass


screen_config = {
    'background_color': 'Black',
    'element_justification': 'center',
}

screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
