"""Ranking Screen with the 20 best scores of all difficulties
"""
from typing import Any

import PySimpleGUI as sg

from src import constants, csg, common
from src.controllers import theme, users_controller as users_ctr
from src.handlers.screen import Screen
from src.handlers.user import User


SCREEN_NAME = '-RANKING-'
HISTORIAL_SIZE = 20


rankings: dict[str, sg.Multiline] = {
    'easy': Any,
    'normal': Any,
    'hard': Any,
    'insane': Any,
    'custom': Any
}

NameScores = tuple[str, dict[str, list[int]]]


def get_name_and_scores(user: User) -> NameScores:
    """Return the name and score of an User
    Args:
        user : the user to get the name and score.
    Returns:
        A tuple with the nick and scores.
    """
    return user.nick, user.sorted_scores


def rank_header(name: str) -> sg.Text:
    """Header of a column .
    Args:
        name: name of the header needed.
    Returns:
        A sg.Text with the theme applied and the text passed by argument
    """
    return sg.Text(
        constants.DIFFICULTY_TO_ES[name],
        size=(16, 1),
        background_color=theme.BG_PRIMARY,
        text_color=theme.TEXT_ACCENT,
        font=(theme.FONT_FAMILY_TEXT, theme.T1_SIZE),
        justification='center',
    )


def rank_content(scores: list[tuple[int, str]]) -> str:
    """Content of the ranking table.
    Manipulate the information to display it correctly on the screen. Sort the first 20 scores
    Args:
        scores: scores that need to be ordered before display it.

    Returns:
        A string of the 20 first scores line per line.
    """
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
    """Create the content of a column.

    Args:
        scores: the string with the scores to display
    Returns: 
        A multiline text with all the info of the scores with the theme applied correctly for the layout. 
    """
    return sg.Multiline(
        scores,
        size=(1, 20),
        disabled=True,
        font=(theme.FONT_FAMILY_TEXT, theme.T2_SIZE),
        justification='center',
        no_scrollbar=True,
        text_color=theme.TEXT_ACCENT,
        background_color=theme.BG_PRIMARY,
        expand_x=True,
        border_width=0
    )


def create_ranking() -> sg.Column:
    """ Create all the rankings columns for each difficulty.
    """
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
    """Refresh ranking information to the last update
    """
    users: list[NameScores] = users_ctr.users_transform(get_name_and_scores)

    for difficulty in rankings:
        all_scores = [
            (score, nick) for nick, scores in users for score in scores[difficulty]
        ]
        rankings[difficulty].update(rank_content(all_scores))


screen_layout = [
    [common.screen_title('ranking', True)],
    [sg.VPush(theme.BG_BASE)],
    [create_ranking()],
    [sg.VPush(theme.BG_BASE)],
    [
        common.navigation_button(
            'Menu Principal', '-MENU-', padding=(theme.scale(64), theme.scale(64))
        ),
        sg.Push(theme.BG_BASE)
    ],
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}


def reset():
    """
    Refresh ranking information to the last update
    """
    refresh_rankings()


screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
