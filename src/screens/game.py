import PySimpleGUI as sg

from src import constants, csg, common

from src.controllers import theme,cards_controller as cards_ctr
from src.handlers import observer
from src.handlers.layout import Screen


SCREEN_NAME = '-GAME-'
FONT = (theme.FONT_FAMILY, 48)

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

game_type : dict[str,sg.Text | sg.Image]= {}

def create_game_type() -> sg.Column:
    game_type['type'] = sg.Text(
        constants.DATASET_TO_ES[cards_ctr.current_type],
        font=FONT
    )
    game_type['icon'] = sg.Image('',source=(128,128))
    layout = [
        [game_type['type']],
        [game_type['icon']]
    ]
    return sg.Column(
        layout,
        background_color=theme.BG_SECONDARY
    )

screen_layout = [
    [common.screen_title('game', True)],
    # [create_game_type(), round_stats],
    # [game_state, card],
    # [leave]
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