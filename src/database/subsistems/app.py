from dataclasses import dataclass
import json
from os import path
from typing import Any

from database.paths import DATA_PATH

APP_PATH = path.join(DATA_PATH, 'app.json')


@dataclass
class GameSettings:
    def __init__(
            self, time_per_round: int,
            rounds_per_game: int, points_correct_answer: int,
            points_bad_answer: int, caracteristics_shown: int):
        self.time_per_round = time_per_round
        self.rounds_per_game = rounds_per_game
        self.points_correct_answer = points_correct_answer
        self.points_bad_answer = points_bad_answer
        self.caracteristics_shown = caracteristics_shown


class AppSettings:
    def __init__(
            self, name: str, full_screen: bool,
            starting_page: str, theme: str, dificulty: str,
            game: dict[str, int]):
        self.name = name
        self.full_screen = full_screen
        self.starting_page = starting_page
        self.theme = theme
        self.dificulty = dificulty
        self.game = GameSettings(**game)


def read_json() -> Any:
    with open(APP_PATH, mode='r', encoding='utf-8') as file:
        return json.load(file)

json_settings = read_json()

def save_json(app: AppSettings) -> None:
    json_settings['custom'] = app
    with open(APP_PATH, mode='w', encoding='utf-8') as file:
        return json.dump(json_settings, file)


def load_app_settings() -> AppSettings:
    if 'custom' in json_settings:
        return AppSettings(**json_settings['custom'])
    return AppSettings(**json_settings['default'])


