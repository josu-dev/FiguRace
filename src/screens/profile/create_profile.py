import PySimpleGUI as sg
from src import constants as const
from src.handlers.layout import Screen
from src.handlers import observer
from src.handlers.theme import theme
SCREEN_NAME = '-CREATE-PROFILE-'

_screen_main_title = sg.Text('CREAR PERFIL',
                             size=500,
                             background_color=theme.BG_BASE,
                             font=(theme.FONT_FAMILY, 45),
                             pad=0,
                             text_color=theme.TEXT_ACCENT)

_create_profile_layout = [
    [
        sg.Text('Nick', size=(4, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, 45), pad=(5, 35)),
        sg.Input(size=(20, 15),
                 do_not_clear=False,
                 background_color=theme.BG_BASE,
                 font=(theme.FONT_FAMILY, 30),
                 text_color='white')
    ],
    [
        sg.Text('Edad', size=(4, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, 45), pad=(5, 35)),
        sg.Input(size=(20, 10),
                 do_not_clear=False,
                 background_color=theme.BG_BASE,
                 font=('System', 30),
                 text_color='white')
    ],
    [
        sg.Text('Género', size=(7, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, 45), pad=(5, 20)),
        sg.Combo(('Femenino', 'Masculino', 'Indefinido', 'Otro'),
                 'Femenino',
                 background_color='#8DC3E4',
                 font=('System', 30),
                 readonly=True,
                 text_color=theme.BG_BASE)
    ],
    [
        sg.Button('Guardar', key='-SAVE-',
                  border_width=15, size=(15, 1),
                  button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                  mouseover_colors=theme.BG_BUTTON_HOVER,
                  font=(theme.FONT_FAMILY, 20),
                  pad=(10, 5))
    ]
]

_turn = sg.Button('<--',
                  key=f'{const.GOTO_VIEW } -PROFILE-',
                  border_width=15,
                  size=(7, 0),
                  button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                  mouseover_colors=theme.BG_BUTTON_HOVER,
                  font=(theme.FONT_FAMILY, 20),
                  pad=20)

_screen_layout = [
    [
        _screen_main_title
    ],
    [
        sg.Column(_create_profile_layout,
                  background_color=theme.BG_BASE,
                  expand_x=True,
                  element_justification='c',
                  vertical_alignment='center',
                  expand_y=True
                  )
    ],
    [

        _turn
    ]
]
_screen_config = {
    'background_color': theme.BG_BASE
}


def function_to_execute_on_event() -> None:
    # This function calls updates on database, updates elements of ui, or do other stuff
    pass

# observer.subscribe('-EVENT-TYPE-EVENT-EMITTER-', function_to_execute_on_event)


def reset(*args):
    # Funcions
    pass


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
