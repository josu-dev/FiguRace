import PySimpleGUI as sg
NAME = "CONFIGURATION"
MAIN_BACK_COLOR = '#112B3C'
# Vertical Space


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=MAIN_BACK_COLOR)

# Horizontal Space


def _h_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding)


def _title() -> sg.Text:
    return sg.Text('C O N F I G U R A T I O N S', size=(800, 1), background_color=MAIN_BACK_COLOR, text_color='#EFEFEF', key='-title-', font=('System', 82), justification='center', pad=64)


def _menu_options():
    MAIN_BACK_COLOR = '#112B3C'
    text_color = '#EFEFEF'
    on_hover_color = MAIN_BACK_COLOR
    default_padding = 16
    layout = [
        [_h_spacer((50, 0)),
         sg.Multiline('Time per game ',
                      disabled=True,
                      font=('System', 25),
                      size=(16, 1),
                      text_color=text_color,
                      no_scrollbar=True,
                      background_color=MAIN_BACK_COLOR,
                      pad=default_padding,
                      border_width=12,
                      justification='center'),

         sg.Text('Seconds ', background_color=MAIN_BACK_COLOR),

         sg.Combo(
             ('15', '30', '60', '90', '180', '300'),
             time_per_game,
             size=(10, 40),
             readonly=True,
             key='-TIME-',),

         _h_spacer((350, 0)),

         sg.Multiline('Features per level', size=(16, 1),
                      font=('System', 25),
                      disabled=True,
                      text_color=text_color,
                      no_scrollbar=True,
                      background_color=MAIN_BACK_COLOR,
                      pad=default_padding,
                      border_width=12),
         sg.Text('Amount  ', background_color=MAIN_BACK_COLOR),

         sg.Combo(('1', '2', '3', '4', '5'),
                  features_per_level,
                  readonly=True,
                  size=(10, 40),
                  key='-CARXLEVEL-', ),
         _h_spacer((50, 0))

         ],

        [_h_spacer((50, 0)),
         sg.Multiline('Rounds per game',
                      text_color=text_color,
                      size=(16, 1),
                      disabled=True,
                      font=('System', 25),
                      background_color=MAIN_BACK_COLOR,
                      pad=default_padding,
                      no_scrollbar=True,
                      border_width=12),
         sg.Text('Rounds   ', background_color=MAIN_BACK_COLOR),
         sg.Combo(('3', '5', '8', '10', '20'),
                  rounds_per_game,
                  readonly=True,
                  size=(10, 40),
                  key='-QROUNDS-',),
         _h_spacer((350, 0)),
         sg.Multiline('Points added',
                      text_color=text_color,
                      no_scrollbar=True,
                      auto_size_text=True,
                      size=(16, 1),
                      disabled=True,
                      background_color=MAIN_BACK_COLOR,
                      font=('System', 25),
                      pad=default_padding,
                      border_width=12),
         sg.Text('Correct  ', background_color=MAIN_BACK_COLOR),
         sg.Combo(('1', '5', '10', '25', '50'),
                  points_added,
                  readonly=True,
                  size=(10, 40),
                  key='-+QXANSWER-',),
         _h_spacer((50, 0))],
        [_h_spacer((50, 0)),
            sg.Multiline('Points substracted',
                         text_color=text_color,
                         no_scrollbar=True,
                         auto_size_text=True,
                         size=(16, 1),
                         disabled=True,
                         background_color=MAIN_BACK_COLOR,
                         font=('System', 25),
                         pad=default_padding,
                         border_width=12),
         sg.Text('Wrong    ', background_color=MAIN_BACK_COLOR),
         sg.Combo(('1', '5', '10', '25', '50'),
                  points_added,
                  readonly=True,
                  size=(10, 40),
                  key='--QXANSWER-',),
         _h_spacer((1000, 0))],

        [_h_spacer((550, 0)),
         _v_spacer((0, 350)),

            sg.Button('Exit', size=(16, 1),
                      font=('System', 25),
                      button_color=(text_color, MAIN_BACK_COLOR),
                      pad=default_padding,
                      mouseover_colors=on_hover_color,
                      border_width=12),
         _h_spacer((600, 0)), ]]

    return layout


# TODO parameters to the other screens
time_per_game = 60
rounds_per_game = 5
points_added = 10
point_substracted = 10
features_per_level = 3

layout = [[_title()],
          [_menu_options()],
          ]


if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Figurace -' + NAME, layout,
                       background_color=MAIN_BACK_COLOR).Finalize()
    window.Maximize()

    while True:     # Event Loop
        event, values = window.read()

        if event in ('Exit',):  # EXIT GAME
            # TODO Save the data
            if (sg.PopupOKCancel('Are you sure ? ', button_color=('#FFFFFF', '#205375'), text_color='#FFFFFF') == 'OK'):
                print('Closing Game..')
                break
            else:
                print('Exit cancelled')

        if event in (sg.WIN_CLOSED, ):
            break
    window.close()
