import PySimpleGUI as sg
from src import constants as const
from src.handlers.layout import Screen
from src.handlers import observer
from src.assets.users import *
from src.PyCustomGUI import elements as cg
from src.handlers import layout
from src.handlers.theme import theme
SCREEN_NAME = '-PROFILES-'

_screen_main_title = sg.Text(SCREEN_NAME,
                             size=(len(SCREEN_NAME), 1),
                             background_color=theme.BG_BASE,
                             font=(theme.FONT_FAMILY, 45),
                             pad=0,
                             text_color=theme.TEXT_ACCENT)

_discord_1 = sg.Image(data=discord_red.source,
                      k='1',
                      size=(64, 64),
                      background_color=theme.BG_BASE,
                      subsample=(discord_red.size//64))
_discord_2 = sg.Image(data=discord_yellow.source,
                      k='2',
                      size=(64, 64),
                      background_color=theme.BG_BASE,
                      subsample=(discord_yellow.size//64))
_discord_3 = sg.Image(data=discord_green.source,
                      k='3',
                      size=(64, 64),
                      background_color=theme.BG_BASE,
                      subsample=(discord_green.size//64))
_discord_4 = sg.Image(data=discord_grey.source,
                      k='4',
                      size=(64, 64),
                      background_color=theme.BG_BASE,
                      subsample=(discord_grey.size//64))

button_1 = sg.Button('Pepe',
                     k='1',
                     size=(10, 2),
                     border_width=15,
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 22),
                     pad=0
                     )
button_2 = sg.Button('Charly',
                     k='2',
                     size=(10, 2),
                     border_width=15,
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 22),
                     pad=0
                     )
button_3 = sg.Button('Nestor',
                     k='3',
                     size=(10, 2),
                     border_width=15,
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 22),
                     pad=0
                     )
button_4 = sg.Button('Free',
                     k='4',
                     size=(10, 2),
                     border_width=15,
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 22),
                     pad=0
                     )

buttons = cg.HorizontalList(justification='c',
    background_color=theme.BG_BASE,
    element_justification='c').add(
    [[_discord_1], [button_1]],
).add(
    [[_discord_2], [button_2]]
).add(
    [[_discord_3], [button_3]]
).add(
    [[_discord_4], [button_4]]
).pack()

_turn = sg.Button('<--',
                  key=f'{const.GOTO_VIEW} -PROFILE-',
                  border_width=15,
                  size=(7, 0),
                  button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                  mouseover_colors=theme.BG_BUTTON_HOVER,
                  font=(theme.FONT_FAMILY, 20), pad=20)

_screen_layout = [
    [_screen_main_title],
    [cg.CenteredElement(buttons,background_color=theme.BG_BASE)],
    [_turn],
]

_screen_config = {
    'background_color' : theme.BG_BASE
}

def function_to_execute_on_event() -> None:
    # This function calls updates on database, updates elements of ui, or do other stuff
    pass

# observer.subscribe('-EVENT-TYPE-EVENT-EMITTER-', function_to_execute_on_event)


def reset(*args):
    # This function resets de elements of the screen to defaults/configuration values
    # It runs every time that window view moves to this screen
    pass


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
