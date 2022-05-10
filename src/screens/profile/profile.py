import PySimpleGUI as sg
NAME = 'PROFILE'
BACK_GROUND_COLOR = '#112B3C'
BUTTON_COLOR = '#4BD9F2'
TEXT_BUTTON_COLOR = '#243F50'

def title (name):
    return sg.Text(name,size=500,  background_color= BACK_GROUND_COLOR, font=('Aquarius',60),pad= 0, text_color='#2D8BC5')

def menu():
    layout= [[sg.VPush(background_color = BACK_GROUND_COLOR)],
            [sg.Button('Create Profile',border_width = 20,size=(15,1), button_color= (TEXT_BUTTON_COLOR,BUTTON_COLOR),mouseover_colors=BACK_GROUND_COLOR,font=('System',30),pad=5)],
            [sg.Button('Select Profile', border_width = 20, size=(15,1), button_color= (TEXT_BUTTON_COLOR,BUTTON_COLOR),mouseover_colors=BACK_GROUND_COLOR,font=('System',30),pad=5)],
            [sg.Button('Exit',border_width = 20, size=(15,1), button_color= (TEXT_BUTTON_COLOR,BUTTON_COLOR),mouseover_colors=BACK_GROUND_COLOR,font=('System',30),pad=5)],
            [sg.VPush(background_color = BACK_GROUND_COLOR)]]
            # [sg.Push(background_color = BACK_GROUND_COLOR)],
            # [sg.Push(background_color = BACK_GROUND_COLOR)]]
    return layout

layout= [[title(NAME)],
        [sg.Column(menu(),background_color=BACK_GROUND_COLOR,expand_y=True)],
        [title('')]]

window = sg.Window('Figurace - ' + NAME, layout,background_color=BACK_GROUND_COLOR,element_justification='center',resizable=True).finalize()

window.Maximize()

while True: 
    events, values = window.read()
    if events in ('Create Profile'):
        print('Go to Creator profile page')
    if events in ('Select Profile'):
        print('Go to profiles page')    
    if events in ('Exit'):
        print('Close program...')
        break
    if events == sg.WIN_CLOSED :
        break
window.close()
