from typing import Any

import PySimpleGUI as sg

from src import constants, csg, common

from src.controllers import theme, users_controller as users_ctr
from src.handlers.layout import Screen
from src.handlers.user import User


SCREEN_NAME = '-SCORE-'
HISTORIAL_SIZE = 20


def create_summary() -> sg.Column:

    return sg.Column([[]])


def refresh_summary() -> None:
    pass


rankings: dict[str, sg.Multiline] = {
    'easy': Any,
    'normal': Any,
    'hard': Any,
    'insane': Any,
    'custom': Any
}

NameScores = tuple[str, dict[str, list[int]]]


def get_name_and_scores(user: User) -> NameScores:
    return user.nick, user.sorted_scores


def rank_header(name: str) -> sg.Text:
    return sg.Text(
        constants.DIFFICULTY_TO_ES[name],
        size=(16, 1),
        background_color=theme.BG_PRIMARY,
        text_color=theme.TEXT_ACCENT,
        font=('System', theme.T1_SIZE),
        justification='center',
    )


def rank_content(scores: list[tuple[int, str]]) -> str:
    content: list[str] = []
    scores = sorted(scores, key=lambda x: x[0], reverse=True)
    for i in range(HISTORIAL_SIZE):
        if i < len(scores):
            score, name = scores[i]
            row = f' {i+1:>2}{score:>6}{name:^15} '
        else:
            row = '\n'
        content.append(row)
    return '\n'.join(content)


def create_rank(scores: str) -> sg.Multiline:
    return sg.Multiline(
        scores,
        size=(1, 20),
        disabled=True,
        font=('Consolas', theme.T2_SIZE),
        justification='center',
        no_scrollbar=True,
        text_color=theme.TEXT_ACCENT,
        background_color=theme.BG_PRIMARY,
        expand_x=True,
        border_width=0
    )


def create_ranking() -> sg.Column:
    ranks = csg.HorizontalList(pad=(0, 0), background_color=theme.BG_SECONDARY)
    users: list[NameScores] = users_ctr.users_transform(get_name_and_scores)

    for difficulty in rankings:
        all_scores = [
            (score, nick) for nick, scores in users for score in scores[difficulty]
        ]
        rankings[difficulty] = create_rank(rank_content(all_scores))
        ranks.add([
            [rank_header(difficulty)],
            [rankings[difficulty]]
        ])
    return ranks.pack()


def refresh_rankings() -> None:
    users: list[NameScores] = users_ctr.users_transform(get_name_and_scores)

    for difficulty in rankings:
        all_scores = [
            (score, nick) for nick, scores in users for score in scores[difficulty]
        ]
        rankings[difficulty].update(rank_content(all_scores))


def create_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        font=('System', theme.H3_SIZE),
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=theme.BD_PRIMARY,
    )


buttons = (
    csg.HorizontalList(
        background_color=theme.BG_BASE,
        element_justification='center'
    ).add([
        create_button('MENU', f'{constants.GOTO_VIEW} -MENU-'),
        create_button('VOLVER A JUGAR', f'{constants.GOTO_VIEW} -GAME-'),
        create_button('NUEVO JUEGO', f'{constants.GOTO_VIEW} -CONFIGURE-GAME-')
    ]).pack()
)

screen_layout = [
    [common.screen_title('score', True)],
    [create_summary()],
    [create_ranking()],
    [csg.vertical_spacer((0, 32), background_color=theme.BG_BASE)],
    [buttons]
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}


def reset():
    refresh_summary()
    refresh_rankings()


screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
