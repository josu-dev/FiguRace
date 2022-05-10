import PySimpleGUI as sg

NAME = "MENU"
MAIN_BACK_COLOR = '#112B3C'
# Vertical Space


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=MAIN_BACK_COLOR)

# Horizontal Space


# Make the menu options


def _title():
    return sg.Text('F  I  G  U  R  A  C  E', size=(800, 1), background_color=MAIN_BACK_COLOR, text_color='#EFEFEF', key='-title-', font=('Sketch 3D', 86), justification='center', pad=64)


def _menu_options():
    back_color = '#205375'
    text_color = '#EFEFEF'
    on_hover_color = MAIN_BACK_COLOR
    default_padding = 12
    font = ('System', 32)
    layout = [
        [_v_spacer((0, 16))],
        [sg.Button('Start Game',
                   size=(15, 1),
                   font=font,
                   auto_size_button=True,
                   button_color=(text_color, back_color),
                   pad=default_padding,
                   mouseover_colors=on_hover_color,
                   border_width=12)],
        [sg.Button('Options', size=(15, 1),
                   auto_size_button=True,
                   font=font,
                   button_color=(text_color, back_color),
                   pad=default_padding,
                   mouseover_colors=on_hover_color,
                   border_width=12)],
        [sg.Button('Profile', size=(15, 1),
                   auto_size_button=True,
                   font=font,
                   button_color=(text_color, back_color),
                   pad=default_padding,
                   mouseover_colors=on_hover_color,
                   border_width=12)],
        [sg.Button('Exit', size=(15, 1),
                   auto_size_button=True,
                   font=font,
                   button_color=(text_color, back_color),
                   pad=default_padding,
                   mouseover_colors=on_hover_color,
                   border_width=12)]
    ]
    return layout


# All the stuff inside your window.
layout = [[_title()],
          [sg.Column(_menu_options(), background_color=MAIN_BACK_COLOR)],
          ]


if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Figurace -' + NAME, layout,
                       background_color=MAIN_BACK_COLOR, element_justification='c').Finalize()
    window.Maximize()

    while True:     # Event Loop
        event, values = window.read()
        if event in ('Start Game',):  # the 1st parameter is the event
            # TODO start running the game
            print('Going to the game screen')

        if event in ('Profile',):
            # TODO Go to the profile screen
            print('Going to the profile screen')

        if event in ('Options',):
            # TODO Go to the options screen
            print('Going to the Options Screen')
        if(sg.WIN_CLOSED,):
            break
        if event in ('Exit',):  # EXIT GAME
            # TODO Save the data
            if (sg.PopupOKCancel('Are you sure ? ', button_color=('#FFFFFF', '#205375'), text_color='#FFFFFF') == 'OK'):
                print('Closing Game..')
                break
            else:
                print('exit cancelled')

    window.close()
