import PySimpleGUI as sg

from src import constants, common

from src.controllers import theme, run_controller as run_ctr, users_controller as users_ctr
from src.handlers import observer
from src.handlers.layout import Screen


SCREEN_NAME = '-GAME-'
SELECT_OPTION = '-SELECT-OPTION-'
CONFIRM_SELECT = '-CONFIRM-SECLECT-'
SKIP_CARD = '-SKIP-CARD-'
END_RUN = '-END-RUN-'


def create_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        font=(theme.FONT_FAMILY, theme.T1_SIZE),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=theme.BD_SECONDARY,
    )


def create_option_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        font=(theme.FONT_FAMILY, theme.T1_SIZE),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=theme.BD_SECONDARY,
        expand_x=True
    )


game_type: dict[str, sg.Text | sg.Image] = {}


def create_game_type() -> sg.Column:
    game_type['type'] = sg.Text(
        constants.DATASET_TO_ES[run_ctr.dataset_type],
        font=(theme.FONT_FAMILY, theme.H2_SIZE)
    )
    game_type['icon'] = sg.Image('', size=(128, 128))
    layout = [
        [game_type['type']],
        [game_type['icon']]
    ]
    return sg.Column(
        layout,
        background_color=theme.BG_SECONDARY
    )


def refresh_game_type() -> None:
    game_type['type'].update(constants.DATASET_TO_ES[run_ctr.dataset_type])
    # refresh game icon


round_state: dict[str, sg.Text] = {}


def create_round_state() -> sg.Column:
    round_state['difficulty'] = sg.Text(
        constants.DIFFICULTY_TO_ES[users_ctr.current_user.preferred_difficulty],
        font=(theme.FONT_FAMILY, theme.H3_SIZE),
    )
    round_state['time'] = sg.Text(
        f'00:30',
        font=(theme.FONT_FAMILY, theme.T1_SIZE),
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


game_state: dict[str, sg.Text | list[sg.Text]] = {}


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
        ) for i in range(run_ctr.max_rounds)
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


card: dict[str, sg.Text | sg.Button | list[str] |
           list[sg.Button] | list[list[sg.Text]]] = {}


def create_card() -> sg.Column:
    card['data'] = run_ctr.options
    characteristics = run_ctr.hints_types
    card['hints'] = [
        [
            sg.Text(characteristic),
            sg.Text('no loaded')
        ] for characteristic in characteristics
    ]
    card['options'] = [
        create_option_button(
            f'{text.capitalize()}',
            f'{SELECT_OPTION} {i}'
        ) for i, text in enumerate(card['data'])
    ]
    layout = [
        *[hint for hint in card['hints']],
        *[[button] for button in card['options']],
        [
            create_button('Confirmar', f'{CONFIRM_SELECT}'),
            create_button('Pasar', f'{SKIP_CARD}')
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
        key=f'{END_RUN}',
        font=(theme.FONT_FAMILY, 24),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=12,
    )


def finish_game() -> None:

    observer.post_event(constants.GOTO_VIEW, '-SCORE-')


observer.subscribe(END_RUN, finish_game)

screen_layout = [
    [common.screen_title('game', True)],
    [create_game_type(), create_round_state()],
    [create_game_state(), create_card()],
    [create_leave_button()]
]


def reset() -> None:
    # reset_game_type()
    refresh_round_state()
    # reset_game_state()
    refresh_card()


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
