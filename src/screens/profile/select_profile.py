from typing import Any
import PySimpleGUI as sg
from src import constants as const
from src.handlers.layout import Screen
from src.handlers import observer
from src.screens.profile import create_profile
from src.screens import menu
from src.handlers.theme import theme
from src.assets.users import *
from src import csg
from src import users_controller as users_c

SCREEN_NAME = '-SELECT-PROFILE-'
USER_NAME = '-USER-NAME-'
EVENT_CREATE_USER = '-CREATE-USER-'
EVENT_DELETE_USER = '-CREATE-USER-'
EVENT_MODIFY_USER = '-MODIFY-USER-'

_screen_main_title = sg.Text('SELECCIONAR PERFIL', size=500,
                             background_color=theme.BG_BASE,
                             font=(theme.FONT_FAMILY, 45),
                             text_color=theme.TEXT_ACCENT,
                             pad=0)
_user_red = sg.Image(data=user_red.source,
                     k='1',
                     size=(100, 100),
                     background_color=theme.BG_BASE,
                     subsample=(user_red.size//100))
_user_yellow = sg.Image(data=user_yellow.source,
                        k='2',
                        size=(100, 100),
                        background_color=theme.BG_BASE,
                        subsample=(user_yellow.size//100))
_user_green = sg.Image(data=user_green.source,
                       k='3',
                       size=(100, 100),
                       background_color=theme.BG_BASE,
                       subsample=(user_green.size//100))
_user_grey = sg.Image(data=user_grey.source,
                      k='4',
                      size=(100, 100),
                      background_color=theme.BG_BASE,
                      subsample=(user_grey.size//100))
_user_violet = sg.Image(data=user_violet.source,
                        k='4',
                        size=(100, 100),
                        background_color=theme.BG_BASE,
                        subsample=(user_violet.size//100))


def user_name(name: str, card_name: str) -> sg.Text:
    if name == '':
        name = 'Vacío'
    key = f'{USER_NAME} {card_name}'
    return sg.Text(name,
                   key=key,
                   background_color=theme.BG_BASE,
                   font=(theme.FONT_FAMILY, 45),
                   pad=(5, 20))

def create_user_button(visible: bool, card_name: str) -> sg.Button:
    key = f'{EVENT_CREATE_USER} {card_name}'
    return sg.Button('Crear', key=key,
                     visible=visible,
                     size=(7, 0),
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 20),
                     pad=20)

def edit_user_button(visible: bool, card_name: str) -> sg.Button:
    key = f'{EVENT_MODIFY_USER} {card_name}'
    return sg.Button('Editar', key=key,
                     visible=visible,
                     size=(7, 0),
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 20),
                     pad=20)

def remove_user_button(visible: bool, card_name: str) -> sg.Button:
    key = f'{EVENT_DELETE_USER} {card_name}'
    return sg.Button('Eliminar', key=key,
                     visible=visible,
                     size=(7, 0),
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 20),
                     pad=20)


users_cards: dict[str, dict[str, sg.Button | sg.Text]] = dict()
users_cards = {str(index): dict() for index in range(5)}

def create_user_cards() -> sg.Column:
    h_list = csg.HorizontalList()
    users_list = users_c.user_list
    for index in range(5):
        card_name = str(index)
        exist = index < len(users_list)
        if exist:
            name = users_list[index].nick
        else:
            name = 'Vacío'
        name_text = user_name(name, card_name)
        create_button = create_user_button(not exist, card_name)
        edit_button = edit_user_button(exist, card_name)
        remove_button = edit_user_button(exist, card_name)

        users_cards[card_name]['name'] = name_text
        users_cards[card_name]['create'] = create_button
        users_cards[card_name]['edit'] = edit_button
        users_cards[card_name]['remove'] = remove_button

        h_list.add([
            [name_text],
            [create_button],
            [edit_button],
            [remove_button],
        ])

    return h_list.pack()

_select_profile_layout = [
    [create_user_cards()]
]


# def create_new_user(card_name : str) -> None:
#     users_cards[card_name]['create'].update(visible=False)
#     users_cards[card_name]['edit'].update(visible=True)
#     users_cards[card_name]['remove'].update(visible=True)
#     observer.post_event(const.GOTO_VIEW, '-CREATE-PROFILE-')

# observer.subscribe(EVENT_CREATE_USER, create_new_user)

# def reset(*args: Any):
#     users_list = users_c.user_list
#     for index, name in enumerate(users_cards):
#         exist = index < len(users_list)
#         users_cards[name]['name'].update(visible=exist)


def reset(*args: Any):
    pass
# _profile_layout = [
#     [
#         sg.VPush(background_color = theme.BG_BASE)
#     ],
# ]


_turn = sg.Button('<--', key=f'{const.GOTO_VIEW} {menu.SCREEN_NAME}',
                  border_width=15,
                  size=(7, 0),
                  button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                  mouseover_colors=theme.BG_BUTTON_HOVER,
                  font=(theme.FONT_FAMILY, 20), pad=20)

_screen_layout = [
    [_screen_main_title],
    [sg.Column(_select_profile_layout,
               background_color=theme.BG_BASE,
               expand_x=True,
               element_justification='c',
               vertical_alignment='center',
               expand_y=True)],
    [_turn]
]


def function_to_execute_on_event() -> None:
    # This function calls updates on database, updates elements of ui, or do other stuff
    pass

# observer.subscribe('-EVENT-TYPE-EVENT-EMITTER-', function_to_execute_on_event)


_screen_config = {
    'background_color': theme.BG_BASE
}

screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
