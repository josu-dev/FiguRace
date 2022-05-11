import PySimpleGUI as sg
from src.handlers.layout import Screen
from src.handlers import observer

SCREEN_NAME = 'PROFILE'
BACK_GROUND_COLOR = '#112B3C'
BUTTON_COLOR = '#6FC5FF'
TEXT_BUTTON_COLOR = '#243F50'
TITLE_COLOR = '#2D8BC5'
TEXT_FONT = ('System', 30)

_screen_main_title = sg.Text(SCREEN_NAME, size=500,
                             background_color=BACK_GROUND_COLOR,
                             font=('Segoe Script', 45),
                             text_color=TITLE_COLOR,
                             pad=0)

_profile_layout = [
    [
        sg.VPush(background_color=BACK_GROUND_COLOR)
    ],
    [
        sg.Button('Create Profile',
                  key='-CREATE-',
                  border_width=20,
                  size=(15, 1),
                  button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR),
                  mouseover_colors=BACK_GROUND_COLOR,
                  font=TEXT_FONT, pad=7)
    ],

    [
        sg.Button('Select Profile',
                  key='-SELECT-',
                  border_width=20,
                  size=(15, 1),
                  button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR),
                  mouseover_colors=BACK_GROUND_COLOR,
                  font=TEXT_FONT, pad=7)
    ],
    [
        sg.VPush(background_color=BACK_GROUND_COLOR)
    ]
]

_turn = sg.Button('<--', key='-BACK-', border_width=15,
                  size=(7, 0),
                  button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR),
                  mouseover_colors=BACK_GROUND_COLOR,
                  font=('System', 20), pad=20)

_screen_layout = [
    [
        _screen_main_title
    ],
    [
        sg.Column(_profile_layout,
                  background_color=BACK_GROUND_COLOR,
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


def reset():
    # Funcions
    pass

# screen = Screen(
#     SCREEN_NAME,
#     _screen_layout,
#     reset
# )


def main() -> None:
    window = sg.Window('Figurace - ' + SCREEN_NAME,
                       _screen_layout, background_color=BACK_GROUND_COLOR,
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
        if events in ('-BACK-'):
            # TODO back to menu
            print('Back page...')
            break
        if events == sg.WIN_CLOSED:
            break
    window.close()

if __name__ == '__main__':
    main()
