import PySimpleGUI as sg
NAME = 'SELECCIONAR PERFIL'
BACK_GROUND_COLOR = '#112B3C'
BUTTON_COLOR = '#4BD9F2'
TEXT_BUTTON_COLOR = '#243F50'


layout = [
    [

    ]]
window = sg.Window('Figurace - ' + NAME, layout,
                   background_color=BACK_GROUND_COLOR, resizable=True, auto_size_buttons=True, margins=(50, 30)).finalize()

window.Maximize()

while True: 

    
window.close()