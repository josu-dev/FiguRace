import PySimpleGUI as sg
from src.handlers.layout import Screen
from src.handlers import observer
from src.screens.profile import profile
from src.handlers import layout
SCREEN_NAME = '-CREATE-PROFILE-'
BACK_GROUND_COLOR = '#112B3C'
BUTTON_COLOR = '#6FC5FF'
BUTTON_HOVER_COLOR = '#5A9ECC'
TEXT_BUTTON_COLOR = '#243F50'
TITLE_COLOR = '#2D8BC5'
TEXT_FONT = ('System', 45)

_screen_main_title = sg.Text(SCREEN_NAME, size=500,
                             background_color=BACK_GROUND_COLOR,
                             font=('Segoe Script', 45),
                             text_color=TITLE_COLOR,
                             pad=0)

_create_profile_layout = [
    [
        sg.Text('Nick', size=(4, 1),
                background_color=BACK_GROUND_COLOR,
                font=TEXT_FONT, pad=(5, 35)),
        sg.Input(size=(20, 15),
                 do_not_clear=False,
                 background_color=BACK_GROUND_COLOR,
                 font=('System', 30),
                 text_color='white')
    ],
    [
        sg.Text('Age', size=(4, 1),
                background_color=BACK_GROUND_COLOR,
                font=TEXT_FONT, pad=(5, 35)),
        sg.Input(size=(20, 10),
                 do_not_clear=False,
                 background_color=BACK_GROUND_COLOR,
                 font=('System', 30),
                 text_color='white')
    ],
    [
        sg.Text('Gender', size=(7, 1),
                background_color=BACK_GROUND_COLOR,
                font=TEXT_FONT, pad=(5, 20)),
        sg.Combo(('Female', 'Male', 'Undefined', 'Other'),
                 'Female',
                 background_color='#8DC3E4',
                 font=('System', 30),
                 readonly=True,
                 text_color=BACK_GROUND_COLOR)
    ],
    [
        sg.Button('Save', key='-SAVE-',
                  border_width=15, size=(15, 1),
                  button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR),
                  mouseover_colors=BUTTON_HOVER_COLOR,
                  font=('System', 20),
                  pad=(10, 5))
    ]
]

_turn = sg.Button('<--',
                  key= f'{layout.GOTO_VIEW } -PROFILE-',
                  border_width=15,
                  size=(7, 0),
                  button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR),
                  mouseover_colors=BUTTON_HOVER_COLOR,
                  font=('System', 20),
                  pad=20)

_screen_layout = [
    [
        _screen_main_title
    ],
    [
        sg.Column(_create_profile_layout,
                  background_color=BACK_GROUND_COLOR,
                  expand_x=True,
                  element_justification='c')
    ],
    [
        _turn
    ]
]


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
                       _screen_layout,
                       background_color=BACK_GROUND_COLOR,
                       resizable=True).finalize()
    window.Maximize()
    while True:
        events, values = window.read()
        if events in ('-BACK-'):
            print('back page...')
            break
        if events == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == '__main__':
    main()
