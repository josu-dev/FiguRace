import PySimpleGUI as sg

from src import constants, csg, common

from src.controllers import theme
from src.handlers import observer
from src.handlers.layout import Screen


SCREEN_NAME = '-BASE-SCREEN-'
FONT = (theme.FONT_FAMILY, 24)

def create_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        font=FONT,
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=12,
    )

_button_exit = sg.Button(
    'Exit', key=constants.EXIT_APLICATION, size=(32, 1),
    font=('Sketch 3D', 20), border_width=12
)

_menu_layout = [
    [csg.vertical_spacer((0, 16))],
    [sg.Text('TAS JOGANDO RE PIOLA PA ', font='Sketch 72')],
    [_button_exit]
]


screen_layout = [
    [common.screen_title('base screen', True)],
    [sg.Column(_menu_layout)],
]


def function_to_execute_on_event() -> None:
    # This function calls updates on database, updates elements of ui, or do other stuff
    pass


observer.subscribe('-EVENT-TYPE-EVENT-EMITTER-', function_to_execute_on_event)

# If an element(normaly a button) needs to emit and event, the way it works is that the button key has the event name first and optional data
# For example -MY-EVENT-NAME- some_data_here


def reset() -> None:
    # This function resets de elements of the screen to defaults/configuration values
    # It runs every time that window view moves to this screen
    pass


screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}

screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)


def main() -> None:
    # Comment screen variable assignment if this file will be runned directly
    window = sg.Window(SCREEN_NAME, screen_layout)

    while True:
        event, values = window.read()

        if event == None or event.startswith(constants.EXIT_APLICATION):
            break

        values = values
    window.close()


if __name__ == '__main__':
    main()
