import PySimpleGUI as sg
from src.handlers.layout import Screen
from src.handlers import observer, layout
from src.screens.profile import select_profile, create_profile
from src.screens import menu
SCREEN_NAME = '-PROFILE-'
BACKGROUND_COLOR = '#112B3C'
BUTTON_COLOR = '#6FC5FF'
TEXT_BUTTON_COLOR = '#243F50'
TITLE_COLOR = '#2D8BC5'
TEXT_FONT = ('System', 30)
BUTTON_HOVER_COLOR = '#5A9ECC'
_screen_main_title = sg.Text(SCREEN_NAME, size=500,
                             background_color=BACKGROUND_COLOR,
                             font=('Segoe Script', 45),
                             text_color=TITLE_COLOR,
                             pad=0)
_profile_layout = [
    [
        sg.VPush(background_color=BACKGROUND_COLOR)
    ],
    [
        sg.Button('Create Profile',
                  key=f'{layout.GOTO_VIEW} {create_profile.SCREEN_NAME}',
                  border_width=20,
                  size=(15, 1),
                  button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR),
                  mouseover_colors=BUTTON_HOVER_COLOR,
                  font=TEXT_FONT, pad=7)
    ],

    [
        sg.Button('Select Profile',
                  key=f'{layout.GOTO_VIEW} {select_profile.SCREEN_NAME}',
                  border_width=20,
                  size=(15, 1),
                  button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR),
                  mouseover_colors=BUTTON_HOVER_COLOR,
                  font=TEXT_FONT, pad=7)
    ],
    [
        sg.VPush(background_color=BACKGROUND_COLOR)
    ]
]

_turn = sg.Button('<--', key=f'{layout.GOTO_VIEW} {menu.SCREEN_NAME}',
                  border_width=15,
                  size=(7, 0),
                  button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR),
                  mouseover_colors=BUTTON_HOVER_COLOR,
                  font=('System', 20), pad=20)

_screen_layout = [
    [
        _screen_main_title
    ],
    [
        sg.Column(_profile_layout,
                  background_color=BACKGROUND_COLOR,
                  expand_y=True, expand_x=True,
                  element_justification='c')
    ],
    [
        _turn
    ]
]

# TRATAR DE HACER RESPONSIVE LA VENTANA

# _relative_size =


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
    reset
)


def main() -> None:
    window = sg.Window('Figurace - ' + SCREEN_NAME,
                       _screen_layout, background_color=BACKGROUND_COLOR,
                       resizable=True).finalize()
    window.Maximize()
    while True:
        events, values = window.read()
        if events in ('-CREATE-'):
            # TODO go to Crate profile page
            print('Go to Creator profile page')
        if events in ('-SELECT-'):
            # TODO go to profiles page
            print('Go to profiles page')
        if events == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == '__main__':
    main()
