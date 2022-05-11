import PySimpleGUI as sg
from src.handlers.layout import Screen
from src.handlers import layout

SCREEN_NAME = "MENU"
MAIN_BACK_COLOR = '#112B3C'
BUTTON_COLOR = '#6FC5FF'
TEXT_COLOR = '#112B3C'
ON_HOVER_COLOR = '#5A9ECC'
default_padding = 2
font = ('System', 32)


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=MAIN_BACK_COLOR)


def _title():
    return sg.Text('F  I  G  U  R  A  C  E', size=(800, 1), background_color=MAIN_BACK_COLOR, text_color='#EFEFEF', key='-title-', font=('Sketch 3D', 86), justification='center', pad=64)


_btn_start_game_ = sg.Button('Start Game',
                             key='-START-',
                             size=(18, 1),
                             font=font,
                             auto_size_button=True,
                             button_color=(TEXT_COLOR, BUTTON_COLOR),
                             pad=default_padding,
                             mouseover_colors=ON_HOVER_COLOR,
                             border_width=12)

_btn_options = sg.Button('Options', size=(18, 1),
                         key='-OPTIONS-',
                         auto_size_button=True,
                         font=font,
                         button_color=(TEXT_COLOR, BUTTON_COLOR),
                         pad=default_padding,
                         mouseover_colors=ON_HOVER_COLOR,
                         border_width=12)

_btn_profile = sg.Button('Profile', size=(18, 1),
                         key=f'{layout.GOTO_VIEW} -PROFILE-',
                         auto_size_button=True,
                         font=font,
                         button_color=(TEXT_COLOR, BUTTON_COLOR),
                         pad=default_padding,
                         mouseover_colors=ON_HOVER_COLOR,
                         border_width=12)

def _menu_options():
    layout = [
        [_v_spacer((0, 12))],
        [_btn_start_game_],
        [_v_spacer((0, 12))],
        [_btn_options],
        [_v_spacer((0, 12))],
        [_btn_profile],
        [_v_spacer((0, 12))],
        [sg.Button('Exit', size=(18, 1),
                   auto_size_button=True,
                   key='-EXIT-',
                   font=font,
                   button_color=(TEXT_COLOR, BUTTON_COLOR),
                   pad=default_padding,
                   mouseover_colors=ON_HOVER_COLOR,
                   border_width=12)]
    ]
    return layout


# All the stuff inside your window.
_menu_layout = [[_title()],
                [sg.Column(_menu_options(), background_color=MAIN_BACK_COLOR)],
                ]

def reset(*args):
    # Funcions
    pass

screen = Screen(
    SCREEN_NAME,
    _menu_layout,
    reset
)

if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Figurace -' + SCREEN_NAME, _menu_layout, resizable=True,
                       background_color=MAIN_BACK_COLOR, element_justification='c').Finalize()
    # window.Maximize()

    while True:     # Event Loop
        event, values = window.read()

        if event in ('-START-',):
            # TODO start running the game
            print('Going to the game screen')

        if event in ('-PROFILE-',):
            # TODO Go to the profile screen
            print('Going to the profile screen')

        if event in ('-OPTIONS-',):
            # TODO Go to the options screen
            print('Going to the Options Screen')

        if event in ('-EXIT-',):  # EXIT GAME
            # TODO Save the data
            if (sg.PopupOKCancel('Are you sure ? ', button_color=('#FFFFFF', '#205375'), text_color='#FFFFFF') == 'OK'):
                print('Closing Game..')
                break
            else:
                print('Exit cancelled')

        if(sg.WIN_CLOSED,):
            break

    window.close()
