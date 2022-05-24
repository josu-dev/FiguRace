import PySimpleGUI as sg
from src import constants as const
from src.handlers.theme import theme
from src.handlers.layout import Screen
from src import csg
from src.controllers import users_controller as users_ctr
from src.handlers.user import User
from src.handlers import observer

_font = ('System', 32)
_default_padding = 2
SCREEN_NAME = "-SCORE-"
MAIN_BACK_COLOR = '#112B3C'


def _title() -> sg.Text:
    return sg.Text(' S C O R E ', size=(800, 1),
                   background_color=theme.BG_BASE,
                   text_color='#EFEFEF',
                   key='-title-',
                   font=('System', 86),
                   justification='center',
                   pad=64,)


def _game_result() -> sg.Column:

    return sg.Column([[]])

def get_name_and_scores(user: User) -> tuple[str, dict[str,list[int]]]:
    return  user.nick, user.sorted_scores

def create_stat_row(pos:int, score:int, name:str) -> sg.Text:
    content = f'{pos} | {score} | {name}'
    return sg.Text(content)

def _ranking() -> sg.Column:
    difficultyes = [
        'easy', 'normal', 'hard', 'insane', 'custom'
    ]
    ranks = csg.HorizontalList()
    users : list[tuple[str, dict[str,list[int]]]]= users_ctr.users_transform(get_name_and_scores)

    for diff in difficultyes:
        header = sg.Text(diff)
        all_scores = [(score, nick) for nick, scores in users for score in scores[diff]]
        sorted_scores = sorted(all_scores,key=lambda x: x[0])[0:20]
        rows = [[create_stat_row(index,*row)] for index, row in enumerate(sorted_scores)]
        ranks.add([
            [header],
            [sg.Column(rows)]
        ])
    return ranks.pack()

_btn_back = sg.Button('FINISH',
                      auto_size_button=True,
                      key=f'{const.GOTO_VIEW} -MENU-',
                      font=_font,
                      button_color=(theme.TEXT_PRIMARY,
                                    theme.BG_BUTTON),
                      pad=_default_padding,
                      mouseover_colors=theme.BG_BUTTON_HOVER,
                      border_width=12)
# All the stuff inside your window.
_screen_layout = [
    [_title()],
    [_game_result()],
    [_ranking()],
]

_screen_config = {
    'background_color': theme.BG_BASE,
}


def reset(*args):
    # Functions
    pass


screen = Screen(
    SCREEN_NAME,
    _screen_layout,
    _screen_config,
    reset
)
