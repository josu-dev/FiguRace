'''Base template of all screens in the application.'''
import PySimpleGUI as sg

from src import constants, csg, common
from src.controllers import theme
from src.handlers import observer


SCREEN_NAME = '-BASE-SCREEN-'


def create_custom_element(text: str, key: str) -> sg.Button:
    '''Create a generic theme button.

    Args:
        text : text displayed on the button
        key : key used to refer the button

    Returns:
        an sg.Button with the theme applied with the text and key passed by args'''
    return sg.Button(
        text,
        key=key,
        font=(theme.FONT_FAMILY, theme.H3_SIZE),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=theme.BD_PRIMARY,
    )


content_layout = [
    [sg.Text('This is for squema example', font=theme.FONT_FAMILY)],
    [csg.vertical_spacer(theme.scale(64))],
    [create_custom_element('My element', constants.EXIT_APLICATION)],
    [csg.vertical_spacer(theme.scale(64))],
    [common.navigation_button('Exit', constants.EXIT_APLICATION)]
]


def function_to_execute_on_event() -> None:
    # This function calls updates on database, updates elements of ui, or do other stuff
    pass


observer.subscribe('-EVENT-TYPE-EVENT-EMITTER-', function_to_execute_on_event)

# If an element(normaly a button) needs to emit and event, the way it works is that the button key has the event name first and optional data
# For example -MY-EVENT-NAME- some_data_here


screen_layout = [
    [common.screen_title('base screen', True)],
    [sg.Column(content_layout)],
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}


def screen_reset() -> None:
    '''This function resets the elements of the screen to defaults/configuration values.
    It runs every time that window view moves to this screen.'''
    pass
