import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import RELIEF_FLAT, RELIEF_GROOVE, RELIEF_RAISED, RELIEF_RIDGE, RELIEF_SOLID, RELIEF_SUNKEN;

NAME = 'PROFILE'
BACK_GROUND_COLOR = '#112B3C'
BUTTON_COLOR = '#4BD9F2'
TEXT_BUTTON_COLOR = '#243F50'
# sg.theme('DarkGrey15')
def title ():
    return sg.Text(NAME,size=500,  background_color= BACK_GROUND_COLOR, font=('Aquarius',60),pad= 10, text_color='#2D8BC5')

def menu():
    layout= [[sg.Button('Crear Perfil',border_width = 20,size=(15,1), button_color= (TEXT_BUTTON_COLOR,BUTTON_COLOR),mouseover_colors=BACK_GROUND_COLOR,font=('System',30),pad=5)],
            [sg.Button('Seleccionar Perfil', border_width = 20, size=(15,1), button_color= (TEXT_BUTTON_COLOR,BUTTON_COLOR),mouseover_colors=BACK_GROUND_COLOR,font=('System',30),pad=5)],
            [sg.Button('Exit',border_width = 20, size=(15,1), button_color= (TEXT_BUTTON_COLOR,BUTTON_COLOR),mouseover_colors=BACK_GROUND_COLOR,font=('System',30),pad=5)]]
    return layout

layout= [[title()],
        [sg.Column(menu(),background_color=BACK_GROUND_COLOR)]]

window = sg.Window('Figurace - ' + NAME, layout,background_color=BACK_GROUND_COLOR,element_justification='center').finalize()

window.Maximize()

while True: 
    events, values = window.read()
    if events in ('Crear Perfil'):
        print('Go to Creator profile page')
    if events in ('Seleccionar Perfil'):
        print('Go to profiles page')    
    if events in ('Exit'):
        print('Close program...')
        break
    if events == sg.WIN_CLOSED :
        break
window.close()
