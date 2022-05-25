import PySimpleGUI as sg

from src import constants, csg, common

from src.controllers import theme,cards_controller as cards_ctr, settings_controller, users_controller as users_ctr
from src.handlers import observer
from src.handlers.card import Card
from src.handlers.layout import Screen
from src.screens.configure_game import layout

difficulty_ctr = settings_controller.difficulty_controller

SCREEN_NAME = '-GAME-'
FONT = (theme.FONT_FAMILY, 48)
SELECT_OPTION = '-SELECT-OPTION-'
NUMBER_ROUNDS = 10
CONFIRM_SELECT = '-CONFIRM-SECLECT-'
SKIP_CARD = '-SKIP-CARD-'


def create_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        font=(theme.FONT_FAMILY, 24),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=4,
    )


def create_option_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        font=(theme.FONT_FAMILY,24),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=2,
        expand_x=True
    )

game_type : dict[str,sg.Text | sg.Image]= {}


def create_game_type() -> sg.Column:
    game_type['type'] = sg.Text(
        constants.DATASET_TO_ES[cards_ctr.current_type],
        font=FONT
    )
    game_type['icon'] = sg.Image('',size=(128,128))
    layout = [
        [game_type['type']],
        [game_type['icon']]
    ]
    return sg.Column(
        layout,
        background_color=theme.BG_SECONDARY
    )


def refresh_game_type() -> None:
    game_type['type'].update(constants.DATASET_TO_ES[cards_ctr.current_type])
    # refresh game icon

round_state : dict[str,sg.Text] = {}


def create_round_state() -> sg.Column:
    round_state['difficulty'] = sg.Text(
        constants.DIFFICULTY_TO_ES[difficulty_ctr.difficulty_name],
        font= FONT,
    )
    round_state['time'] = sg.Text(
        f'00:30',
        font= FONT,
    )
    layout = [
        [round_state['difficulty']],
        [round_state['time']]
    ]
    return sg.Column(
        layout
    )


def refresh_round_state() -> None:
    pass


game_state : dict[str,sg.Text|list[sg.Text]] = {}

def create_game_state() -> sg.Column:
    game_state['user'] = sg.Text(
        users_ctr.current_user.nick,
        font=(theme.FONT_FAMILY, 24),
        size=24,
        justification='center'
    )
    game_state['rounds'] = [
        sg.Text(
            f' {i+1:<2} - ',
            font=(theme.FONT_FAMILY, 16)
        ) for i in range(NUMBER_ROUNDS,)
    ]
    layout = [
        [game_state['user']],
        *[[stat] for stat in game_state['rounds']]
    ]
    return sg.Column(
        layout,
        background_color=theme.BG_SECONDARY,
        element_justification='center'
    )

def refresh_game_state() -> None:
    pass


card : dict[str, sg.Text | sg.Button | Card | list[sg.Button]| list[list[sg.Text]]] = {}

def create_card() -> sg.Column:
    card['data'] = cards_ctr.new_card
    characteristics = cards_ctr.characteristics
    card['hints'] = [
            [
                sg.Text(characteristic),
                sg.Text('no loaded')
            ] for characteristic in characteristics
        ]
    card['options'] = [
        create_option_button(
            f'Opcíon {i+1}',
            f'{SELECT_OPTION} {i+1}'
        ) for i in range(len(card['data'].bad_anwers) + 1)
    ]
    layout = [
        *[hint for hint in card['hints']],
        *[[button] for button in card['options']],
        [
            create_button('Confirmar',f'{CONFIRM_SELECT}'),
            create_button('Pasar',f'{SKIP_CARD}')
        ]
    ]
    return sg.Column(
        layout
    )


def refresh_card() -> None:
    pass


def create_leave_button() -> sg.Button:
    return sg.Button(
        'Abandonar partida',
        key= f'{constants.GOTO_VIEW} -SCORE-',
        font=(theme.FONT_FAMILY,24),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=12,
    )

screen_layout = [
    [common.screen_title('game', True)],
    [create_game_type(), create_round_state()],
    [create_game_state(),create_card()],
    [create_leave_button()]
]


def reset() -> None:
    refresh_game_type()


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