import PySimpleGUI as sg
from src import constants, csg, common
from src.controllers import theme
from src.controllers import users_controller as users_ctr
from src.handlers.layout import Screen
from src.handlers.user import User
from src.handlers import observer

FONT = ('System', 32)
SCREEN_NAME = '-SCORE-'
HISTORIAL_SIZE = 20


def _game_result() -> sg.Column:

    return sg.Column([[]])

def get_name_and_scores(user: User) -> tuple[str, dict[str,list[int]]]:
    return  user.nick, user.sorted_scores

def create_stat_row(pos:int, score:int, name:str) -> sg.Text:
    content = f'{pos} | {score} | {name}'
    return sg.Text(content)

rankings : dict[str,sg.Multiline] = dict()

def rank_header(name:str) -> sg.Text:

    return sg.Text(
        constants.DIFFICULTY_TO_ES[name],
        size=(16, 1),
        background_color=theme.BG_PRIMARY,
        text_color=theme.TEXT_ACCENT,
        font=('System', 26),
        justification='center',
    )

def rank_content(scores: list[tuple[int,str]]) -> str:
    content : list[str] = []
    scores = sorted(scores,key=lambda x: x[0],reverse=True)
    for i in range(HISTORIAL_SIZE):
        if i < len(scores):
            score, name = scores[i]
            row = f' {i+1:^2} {score:^5} {name:^14} '
        else:
            row = '\n'
        content.append(row)
    return '\n'.join(content)

def create_rank(scores: str) -> sg.Multiline:
    return sg.Multiline(
        scores,
        size=(1,20),
        disabled=True,
        font=('Consolas', 16),
        justification='center',
        no_scrollbar=True,
        text_color=theme.TEXT_ACCENT,
        background_color=theme.BG_PRIMARY,
        expand_x=True,
        border_width=0
    )

def create_ranking() -> sg.Column:
    difficulties = [
        'easy', 'normal', 'hard', 'insane', 'custom'
    ]
    ranks = csg.HorizontalList()
    users : list[tuple[str, dict[str,list[int]]]]= users_ctr.users_transform(get_name_and_scores)

    for diff in difficulties:
        all_scores = [(score, nick) for nick, scores in users for score in scores[diff]]
        ranks.add([
            [rank_header(diff)],
            [create_rank(rank_content(all_scores))]
        ])
    return ranks.pack()

def create_button(text: str, key: str) -> sg.Button:
    return sg.Button(
        text,
        key=key,
        font= FONT,
        button_color=(
            theme.TEXT_BUTTON,
            theme.BG_BUTTON
        ),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=12,
    )

buttons = (
    csg.HorizontalList(
        background_color=theme.BG_BASE,
        element_justification='center'
    ).add([
        create_button('MENU', f'{constants.GOTO_VIEW} -MENU-'),
        create_button('VOLVER A JUGAR', f'{constants.GOTO_VIEW} -GAME-'),
        create_button('NUEVO JUEGO', f'{constants.GOTO_VIEW} -CONFIGGAME-')
    ]).pack()
)
    

# All the stuff inside your window.
screen_layout = [
    [common.screen_title('score', True)],
    [_game_result()],
    [create_ranking()],
    [buttons]
]

screen_config = {
    'background_color': theme.BG_BASE,
    'justification':'center',
    'element_justification':'center',
}


def reset(*args):
    # Functions
    pass


screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
