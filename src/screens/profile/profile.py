import PySimpleGUI as sg

SCREEN_NAME = 'PROFILE'
BACK_GROUND_COLOR = '#112B3C'
BUTTON_COLOR = '#4BD9F2'
TEXT_BUTTON_COLOR = '#243F50'



_title = sg.Text(SCREEN_NAME, size=500,  background_color=BACK_GROUND_COLOR,
                font=('Segoe Script', 45), pad=0, text_color='#2D8BC5')

_layout = [
    [sg.VPush(background_color=BACK_GROUND_COLOR)],
    [sg.Button('Create Profile', key='-CREATE-', border_width=20, size=(15, 1), button_color=(
        TEXT_BUTTON_COLOR, BUTTON_COLOR), mouseover_colors=BACK_GROUND_COLOR, font=('System', 30), pad=7)],
    [sg.Button('Select Profile', key='-SELECT-', border_width=20, size=(15, 1), button_color=(
        TEXT_BUTTON_COLOR, BUTTON_COLOR), mouseover_colors=BACK_GROUND_COLOR, font=('System', 30), pad=7)],
    [sg.VPush(background_color=BACK_GROUND_COLOR)]]

_turn = sg.Button('<--', key='-BACK-', border_width=15, size=(7,0), button_color=(
    TEXT_BUTTON_COLOR, BUTTON_COLOR), mouseover_colors=BACK_GROUND_COLOR, font=('System', 20),pad=20)
    
layout = [[_title],
          [sg.Column(_layout, background_color=BACK_GROUND_COLOR, expand_y=True, expand_x= True, element_justification='c')],
          [_turn]
          ]

window = sg.Window('Figurace - ' + SCREEN_NAME, layout, background_color=BACK_GROUND_COLOR,
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
