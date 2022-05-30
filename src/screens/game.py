from typing import TypedDict

import PySimpleGUI as sg

from src import constants, common, csg
from src.controllers import theme, run_controller as run_ctr, users_controller as users_ctr
from src.handlers import observer
from src.handlers.screen import Screen


SCREEN_NAME = '-GAME-'
SELECT_OPTION = '-SELECT-OPTION-'
CONFIRM_SELECTED_OPTION = '-CONFIRM-SELECTED-OPTION-'
SKIP_CARD = '-SKIP-CARD-'
END_RUN = '-END-RUN-'


class CardState(TypedDict):
    type: sg.Text
    data: list[str]
    hints: list[list[sg.Text]]
    options: list[sg.Button]
    selected: int
    confirm_button: sg.Button


class RunState(TypedDict):
    difficulty: sg.Text
    time: sg.Text
    user: sg.Text
    rounds: list[sg.Text]


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


run_state: RunState = {}


def create_run_state() -> sg.Column:
    run_state['difficulty'] = sg.Text(
        constants.DIFFICULTY_TO_ES[users_ctr.current_user.preferred_difficulty],
        font=(theme.FONT_FAMILY, theme.H3_SIZE),
    )
    run_state['time'] = sg.Text(
        f'00:30',
        font=(theme.FONT_FAMILY, theme.T1_SIZE),
    )
    run_state['user'] = sg.Text(
        users_ctr.current_user.nick,
        font=(theme.FONT_FAMILY, theme.T1_SIZE),
        size=24,
        justification='center'
    )
    run_state['rounds'] = [
        sg.Text(
            f' {i+1:<2} - ',
            font=(theme.FONT_FAMILY, theme.T2_SIZE)
        ) for i in range(run_ctr.max_rounds)
    ]
    layout = [
        [run_state['difficulty']],
        [run_state['time']],
        [run_state['user']],
        *[[stat] for stat in run_state['rounds']]
    ]
    return sg.Column(
        layout,
        background_color=theme.BG_SECONDARY,
        element_justification='center'
    )


def refresh_timer() -> None:
    run_state['time'].update(run_ctr.time)


def reset_run_state() -> None:
    run_state['difficulty'].update(
        constants.DIFFICULTY_TO_ES[users_ctr.current_user.preferred_difficulty])
    refresh_timer()
    run_state['user'].update(users_ctr.current_user.nick)
    for i, round in enumerate(run_state['rounds']):
        round.update(f' {i+1:<2} - ')


def refresh_run_state() -> None:
    score = run_ctr.score
    for i, round in enumerate(run_state['rounds']):
        points = score[i] if i < len(score) else ''
        round.update(f' {i+1:<2} - {points}')


def create_option_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        font=(theme.FONT_FAMILY, theme.scale(20)),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=theme.BD_SECONDARY,
        expand_x=True
    )


card: CardState = {}


def create_card() -> sg.Column:
    card['type'] = sg.Text(
        constants.DATASET_TO_ES[run_ctr.dataset_type],
        font=(theme.FONT_FAMILY, theme.H2_SIZE),
    )
    card['data'] = run_ctr.options
    characteristics = run_ctr.hints_types
    card['hints'] = [
        [
            sg.Text(
                characteristic,
                font=(theme.FONT_FAMILY, theme.T1_SIZE)
            ),
            sg.Text(
                'no loaded',
                font=(theme.FONT_FAMILY, theme.T1_SIZE)
            ),
        ] for characteristic in characteristics
    ]
    card['options'] = [
        create_option_button(
            f'{text.capitalize()}',
            f'{SELECT_OPTION} {i}'
        ) for i, text in enumerate(card['data'])
    ]
    card['selected'] = -1
    card['confirm_button'] = create_button('Confirmar', f'{CONFIRM_SELECTED_OPTION}')
    layout = [
        [card['type']],
        *[hint for hint in card['hints']],
        *[[button] for button in card['options']],
        [
            card['confirm_button'],
            create_button('Pasar', f'{SKIP_CARD}')
        ]
    ]
    return sg.Column(
        layout
    )


def refresh_card() -> None:
    hints = run_ctr.hints

    for i, row in enumerate(card['hints']):
        if i < len(hints):
            row[1].update(hints[i])
        else:
            row[1].update('')


run_ctr.registry_event('bad_option', refresh_card)


def current_answer(index: str) -> None:
    if card['selected'] >= 0:
        card['options'][card['selected']].update(button_color=theme.BG_BUTTON)
    card['selected'] = int(index)
    card['options'][card['selected']].update(button_color=theme.BG_PRIMARY)
    card['confirm_button'].update(disabled=False, button_color=(theme.TEXT_BUTTON,theme.BG_BUTTON))


observer.subscribe(SELECT_OPTION, current_answer)


def new_answer() -> None:
    card['confirm_button'].update(disabled=True,button_color=(theme.TEXT_BUTTON_DISABLED,theme.BG_BUTTON_DISABLED))
    card['options'][card['selected']].update(disabled=True,button_color=(theme.TEXT_BUTTON_DISABLED,theme.BG_BUTTON_DISABLED))
    run_ctr.new_answer(card['data'][card['selected']])


observer.subscribe(CONFIRM_SELECTED_OPTION, new_answer)


def reset_card() -> None:
    card['type'].update(constants.DATASET_TO_ES[run_ctr.dataset_type])
    card['data'] = run_ctr.options
    characteristics = run_ctr.hints_types
    hints = run_ctr.hints

    for i, row in enumerate(card['hints']):
        row[0].update(f'{characteristics[i]}: ')
        if i < len(hints):
            row[1].update(hints[i])
        else:
            row[1].update('')

    for option, content in zip(card['options'], card['data']):
        option.update(content, disabled=False, button_color=theme.BG_BUTTON)

    card['selected'] = -1
    card['confirm_button'].update(disabled=True)


def end_round() -> None:
    refresh_run_state()
    reset_card()


run_ctr.registry_event('win_round', end_round)
run_ctr.registry_event('loose_round', end_round)


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
    total_score = sum(run_ctr.score)
    users_ctr.current_user.update_score(
        users_ctr.current_user.preferred_difficulty, total_score
    )
    observer.post_event(constants.GOTO_VIEW, '-RESULT-')


run_ctr.registry_event('end_run', finish_game)


def force_end_round() -> None:
    run_ctr.end_round()
    end_round()


observer.subscribe(SKIP_CARD, force_end_round)


def force_end_game() -> None:
    run_ctr.end_run()


observer.subscribe(END_RUN, force_end_game)

screen_layout = [
    [sg.VPush(theme.BG_BASE)],
    [
        csg.CenteredElement(
            create_run_state(),
            background_color=theme.BG_BASE
        ),
        # csg.CenteredElement(
        #     create_card(),
        #     background_color=theme.BG_BASE
        # ),
        create_card(),
        sg.Push(theme.BG_BASE)
    ],
    [create_leave_button()],
    [sg.VPush(theme.BG_BASE)]
]


def reset() -> None:
    run_ctr.reset()
    reset_run_state()
    reset_card()


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
