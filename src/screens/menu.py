import PySimpleGUI as sg

SCREEN_NAME = "MENU"
MAIN_BACK_COLOR = '#112B3C'
BACK_COLOR = '#205375'
TEXT_COLOR = '#EFEFEF'
default_padding = 6
font = ('System', 32)


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=MAIN_BACK_COLOR)


def _title():
    return sg.Text('F  I  G  U  R  A  C  E', size=(800, 1), background_color=MAIN_BACK_COLOR, text_color='#EFEFEF', key='-title-', font=('Sketch 3D', 86), justification='center', pad=64)


_btn_start_game_ = sg.Button('Start Game',
                             key='-START-',
                             size=(15, 1),
                             font=font,
                             auto_size_button=True,
                             button_color=(TEXT_COLOR, BACK_COLOR),
                             pad=default_padding,
                             mouseover_colors=MAIN_BACK_COLOR,
                             border_width=12)

_btn_options = sg.Button('Options', size=(15, 1),
                         key='-OPTIONS-',
                         auto_size_button=True,
                         font=font,
                         button_color=(TEXT_COLOR, BACK_COLOR),
                         pad=default_padding,
                         mouseover_colors=MAIN_BACK_COLOR,
                         border_width=12)

_btn_profile = sg.Button('Profile', size=(15, 1),
                         key='-PROFILE-',
                         auto_size_button=True,
                         font=font,
                         button_color=(TEXT_COLOR, BACK_COLOR),
                         pad=default_padding,
                         mouseover_colors=MAIN_BACK_COLOR,
                         border_width=12)


def _menu_options():
    layout = [
        [_v_spacer((0, 16))],
        [_btn_start_game_],
        [_btn_options],
        [_btn_profile],
        [sg.Button('Exit', size=(15, 1),
                   auto_size_button=True,
                   key='-EXIT-',
                   font=font,
                   button_color=(TEXT_COLOR, BACK_COLOR),
                   pad=default_padding,
                   mouseover_colors=MAIN_BACK_COLOR,
                   border_width=12)]
    ]
    return layout


# All the stuff inside your window.
_menu_layout = [[_title()],
                [sg.Column(_menu_options(), background_color=MAIN_BACK_COLOR)],
                ]


if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Figurace -' + SCREEN_NAME, _menu_layout, size=(800, 600),
                       background_color=MAIN_BACK_COLOR, element_justification='c').Finalize()
    window.Maximize()

    while True:     # Event Loop
        event, values = window.read()
        if event in ('-START-',):  # the 1st parameter is the event
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
            if (sg.PopupOKCancel('Are you sure ? ', button_color=('#FFFFFF', '#205375'), TEXT_COLOR='#FFFFFF') == 'OK'):
                print('Closing Game..')
                break
            else:
                print('Exit cancelled')

        if(sg.WIN_CLOSED,):
            break

    window.close()
