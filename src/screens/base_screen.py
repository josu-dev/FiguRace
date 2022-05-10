import PySimpleGUI as sg
from handlers.layout import Screen
from handlers import observer

SCREEN_NAME = '-BASE-SCREEN-'


def _v_spacer(padding: tuple[int, int] = (0, 0)) -> sg.Column:
    return sg.Column([[]], size=padding)


_main_title = sg.Text('FIGURACE', size=(800, 1), text_color='#EFEFEF',
                      key='-title-', font=('Sketch 3D', 82), justification='center', pad=64)

_button_exit = sg.Button(
    'Exit', key='exit  ', size=(32, 1),
    font=('Sketch 3D', 20), border_width=12
)

_menu_layout = [
    [_v_spacer((0, 16))],
    [sg.Text('TAS JOGANDO RE PIOLA PA ', font='Sketch 72')],
    [_button_exit]
]


_screen_layout = [
    [_main_title],
    [sg.Column(_menu_layout)],
]

def function_to_execute_on_event() -> None:
    # This function calls updates on database, updates elements of ui, or do other stuff
    pass

observer.subscribe('-EVENT-TYPE-EVENT-EMITTER-', function_to_execute_on_event)

# If an element(normaly a button) needs to emit and event, the way it works is that the button key has the event name first and optional data
# For example -MY-EVENT-NAME- some_data_here

def reset():
    # This function resets de elements of the screen to defaults/configuration values
    # It runs every time that window view moves to this screen
    pass


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    reset
)

def main() -> None:
    window = sg.Window(SCREEN_NAME, _screen_layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED: break

if __name__ == '__main__':
    main()
