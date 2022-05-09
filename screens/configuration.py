import PySimpleGUI as sg
NAME = "CONFIGURATION"
MAIN_BACK_COLOR = '#112B3C'
# Vertical Space


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=MAIN_BACK_COLOR)

# Horizontal Space


def _h_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding)


def _title():
    return sg.Text('CONFIGURATIONS', size=(800, 1), background_color=MAIN_BACK_COLOR, text_color='#EFEFEF', key='-title-', font=('Sketch 3D', 82), justification='center', pad=64)


def _menu_options():
    back_color = '#205375'
    text_color = '#EFEFEF'
    on_hover_color = MAIN_BACK_COLOR
    default_padding = 16
    layout = [
        [_v_spacer((0, 16))],
        [_h_spacer((50, 0)),
         sg.Text('time per game ',
                 font=('Sketch 3D', 25),
                 size=(16, 1),
                 background_color=back_color,
                 pad=default_padding, justification='center'),

         sg.Text('Seconds ', background_color=MAIN_BACK_COLOR),

         sg.Input('60', size=(10, 40),
                  key='-TIME-',),

         _h_spacer((350, 0)),

         sg.Text('features per level', size=(16, 1),
                 font=('Sketch 3D', 25),
                 background_color=back_color,
                 pad=default_padding,
                 border_width=12),
         sg.Text('amount : ', background_color=MAIN_BACK_COLOR),
         sg.Input('60',
                  size=(10, 2),
                  key='-CARXLEVEL-', ),
         _h_spacer((50, 0))

         ],
        [_v_spacer((0, 150))],
        [_h_spacer((50, 0)),
         sg.Text('Rounds per game',
                 size=(16, 1),
                 font=('Sketch 3D', 25),
                 background_color=back_color,
                 pad=default_padding,
                 border_width=12),
         sg.Text('Rounds ', background_color=MAIN_BACK_COLOR),
         sg.Input('5',
                  size=(10, 2),
                  key='-QROUNDS-',),
         _h_spacer((350, 0)),
         sg.Text('Points added per Answer',
                 size=(16, 1),
                 background_color=back_color,
                 font=('Sketch 3D', 25),
                 pad=default_padding,
                 border_width=12),
         sg.Text('Added ', background_color=MAIN_BACK_COLOR),
         sg.Input('10', size=(10, 2),
                  key='-+QXANSWER-',),
         _h_spacer((50, 0))],

        [_v_spacer((0, 100))],
        [_h_spacer((550, 0)),
            sg.Button('Exit', size=(16, 1),
                      font=('Sketch 3D', 25),
                      button_color=(text_color, back_color),
                      pad=default_padding,
                      mouseover_colors=on_hover_color,
                      border_width=12),
         _h_spacer((600, 0)), ]

    ]
    return layout


layout = [[_title()],
          [_menu_options()],
          ]

# Create the Window
window = sg.Window('Figurace -' + NAME, layout,
                   background_color=MAIN_BACK_COLOR).Finalize()
window.Maximize()


while True:     # Event Loop
    event, values = window.read()
    if event in ('Tiempo Por Juego'):  # the 1st parameter is the event
        # TODO start running the game
        print('Going to the game screen')

    if event in ('Profile'):
        # TODO Go to the profile screen
        print('Going to the profile screen')

    if event in ('Options'):
        # TODO Go to the options screen
        print('Going to the Options Screen')

    if event in (sg.WIN_CLOSED, 'Exit'):  # EXIT GAME
        # TODO Save the data
        if (sg.PopupOKCancel('Are you sure ? ', button_color=('#FFFFFF', '#205375'), text_color='#FFFFFF') == 'OK'):
            print('Closing Game..')
            break
        else:
            print('exit cancelled')

window.close()
