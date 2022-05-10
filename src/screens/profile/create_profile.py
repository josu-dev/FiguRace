from tkinter import font
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import T

NAME = 'CREATE PROFILE'
BACK_GROUND_COLOR = '#112B3C'
BUTTON_COLOR = '#4BD9F2'
TEXT_BUTTON_COLOR = '#243F50'

_title = sg.Text(NAME, size=500, background_color=BACK_GROUND_COLOR,
                font=('Segoe Script', 45), pad=0, text_color='#2D8BC5')

_layout = [
    [sg.Text('Nick', size=(4, 1), background_color='#112B3C', font=('System', 45), pad=(5, 35)),
     sg.Input(size=(20, 15), do_not_clear=False, background_color=BACK_GROUND_COLOR, font=('System', 30), text_color='white')],
    [sg.Text('Age', size=(4, 1), background_color=BACK_GROUND_COLOR, font=('System', 45), pad=(5, 35)),
     sg.Input(size=(20, 10), do_not_clear=False, background_color=BACK_GROUND_COLOR, font=('System', 30), text_color='white')],
    [sg.Text('Gender', size=(7, 1), background_color=BACK_GROUND_COLOR, font=('System', 45), pad=(5, 20)),
     sg.Combo(('Female','Male', 'Undefined', 'Other'), 'Female', background_color='#8DC3E4', font=('System', 30), readonly=True, text_color=BACK_GROUND_COLOR)],
    [sg.Button('Save',key='-SAVE-', border_width=15, size=(15, 1), button_color=(TEXT_BUTTON_COLOR, BUTTON_COLOR), mouseover_colors=BACK_GROUND_COLOR, font=('System', 20), pad=(10, 5))]]
    # [sg.VPush(background_color=BACK_GROUND_COLOR)]
_turn = sg.Button('<--', key='-BACK-', border_width=15, size=(7,0), button_color=(
    TEXT_BUTTON_COLOR, BUTTON_COLOR), mouseover_colors=BACK_GROUND_COLOR, font=('System', 20),pad=20)

_layout = [[_title],
          [sg.Column(_layout, background_color=BACK_GROUND_COLOR,expand_x=True, element_justification='c')],
          [_turn]]

window = sg.Window('Figurace - ' + NAME, _layout,
                   background_color=BACK_GROUND_COLOR,resizable=True).finalize()

window.Maximize()

while True:
    events, values = window.read()
    if events in ('-BACK-'):
        print('back page...')
        break
    if events == sg.WIN_CLOSED:
        break
window.close()
