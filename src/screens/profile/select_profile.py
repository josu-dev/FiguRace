from typing import Any
import PySimpleGUI as sg
from src import constants as const
from src.handlers.layout import Screen
from src.handlers import observer
from src.screens import menu
from src.controllers import theme
from src.assets.users import *
from src import csg, common
from src.controllers import users_controller as users_ctr
from src.assets.wallpaper import image as wall


SCREEN_NAME = '-SELECT-PROFILE-'
USER_NAME = '-USER-NAME-'
USER_IMAGE = '-USER-IMAGE-'
EVENT_CREATE_USER = '-CREATE-USER-'
EVENT_DELETE_USER = '-DELETE-USER-'
EVENT_MODIFY_USER = '-EDITION-USER-'

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
    return sg.Button('Crear',
                     key=key,
                     visible=visible,
                     size=(7, 0),
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 20),
                     pad=20)


def edit_user_button(visible: bool, card_name: str) -> sg.Button:
    key = f'{EVENT_MODIFY_USER} {card_name}'
    return sg.Button('Editar',
                     key=key,
                     visible=visible,
                     size=(7, 0),
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 20),
                     pad=20)


def remove_user_button(visible: bool, card_name: str) -> sg.Button:
    key = f'{EVENT_DELETE_USER} {card_name}'
    return sg.Button('Eliminar',
                     key=key,
                     visible=visible,
                     size=(7, 0),
                     button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                     mouseover_colors=theme.BG_BUTTON_HOVER,
                     font=(theme.FONT_FAMILY, 20),
                     pad=20)


def select_user_image(color: str, card_name: str) -> sg.Image:
    if color == 'yellow':
        source = user_yellow.source
    elif color == 'red':
        source = user_red.source
    elif color == 'green':
        source = user_green.source
    elif color == 'violet':
        source = user_violet.source
    else:
        source = user_grey.source
    key = f'{USER_IMAGE} {card_name}'
    return sg.Image(
        key=key,
        data=source,
        size=(100, 100),
        background_color=theme.BG_BASE,
        subsample=(96//100)
    )


users_ctrards: dict[str, dict[str, sg.Button | sg.Text]] = dict()
users_ctrards = {str(index): dict() for index in range(5)}

_hlist_config = {
    'background_color': theme.BG_BASE,
}

img = sg.Image(data=wall.source,
               size=(1366, 768),
               background_color=theme.BG_BASE,
               subsample=(wall.size//1366))


def create_user_cards() -> sg.Column:
    h_list = csg.HorizontalList(
        background_color=theme.BG_BASE,
        element_justification='c',
        vertical_alignment='center',
        expand_y=True,
        expand_x=True,)
    users_list = users_ctr.user_list
    for index in range(5):
        card_name = str(index)
        exist = index < len(users_list)
        if exist:
            name = users_list[index].nick
            color_user = users_list[index].prefered_color
        else:
            name = 'Vacío'
            color_user = 'grey'

        user_image = select_user_image(color_user, card_name)
        name_text = user_name(name, card_name)
        create_button = create_user_button(not exist, card_name)
        edit_button = edit_user_button(exist, card_name)
        remove_button = remove_user_button(exist, card_name)

        users_ctrards[card_name]['image'] = user_image
        users_ctrards[card_name]['name'] = name_text
        users_ctrards[card_name]['create'] = create_button
        users_ctrards[card_name]['edit'] = edit_button
        users_ctrards[card_name]['remove'] = remove_button

        h_list.add([
            [user_image],
            [name_text],
            [edit_button],
            [remove_button],
            [create_button],
        ])

    return h_list.pack()


def create_new_user(card_name) -> None:
    users_ctrards[card_name]['edit'].update(visible=True)
    users_ctrards[card_name]['remove'].update(visible=True)
    users_ctrards[card_name]['create'].update(visible=False)
    observer.post_event(const.GOTO_VIEW, '-CREATE-PROFILE-')


observer.subscribe(EVENT_CREATE_USER, create_new_user)


def reset(*args: Any):
    users_list = users_ctr.user_list
    for index, name in enumerate(users_ctrards):
        exist = index < len(users_list)
        users_ctrards[name]['name'].update(visible=exist)


def reset(*args: Any):
    pass
# _profile_layout = [
#     [
#         sg.VPush(background_color = theme.BG_BASE)
#     ],
# ]


_go = sg.Button('Confirmar', key=f'{const.GOTO_VIEW} {menu.SCREEN_NAME}',
                  border_width=15,
                  button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                  mouseover_colors=theme.BG_BUTTON_HOVER,
                  font=(theme.FONT_FAMILY,theme.T1_SIZE),
                  )

_select_profile_layout = [
    [sg.Listbox(values=users_ctr.users_transform(lambda user: user.nick),
                expand_x=True, 
                expand_y=True,
                background_color=theme.BG_BASE,
                text_color= theme.TEXT_PRIMARY,
                font=(theme.FONT_FAMILY,theme.H3_SIZE)
                )],
    
]

_screen_layout = [
    [common.screen_title('PERFILES', alignment='left')],
    [sg.Column(_select_profile_layout,
               background_color=theme.BG_BASE,
               expand_x=True,
               element_justification='left',
               vertical_alignment='left',
               expand_y=True,
               )],
    [csg.CenteredElement(_go,background_color = theme.BG_BASE)]
]

def function_to_execute_on_event() -> None:
    # This function calls updates on database, updates elements of ui, or do other stuff
    pass

# observer.subscribe('-EVENT-TYPE-EVENT-EMITTER-', function_to_execute_on_event)


_screen_config = {
    'background_color': theme.BG_BASE,
}

screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
