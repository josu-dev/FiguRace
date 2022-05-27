from typing import Any, Callable, TypedDict

from src import constants, file
from . import observer, difficulty


RESULTS_LENGTH = 20
DEFAULT_PREFERRED_DIFFICULTY = difficulty.DEFAULT_NORMAL

class UserJSON(TypedDict):
    nick: str
    age: int
    gender: str
    preferred_color: str
    preferred_difficulty: str
    custom_difficulty: difficulty.DifficultyJSON
    scores: dict[str, list[int]]

def default_difficulty() -> difficulty.DifficultyJSON:
    return {
        'time_per_round': 50,
        'rounds_per_game': 10,
        'points_correct_answer': 12,
        'points_bad_answer': -2,
        'characteristics_shown': 3
    }

def default_scores() -> dict[str, list[int]]:
    return {
        'easy': [],
        'normal': [],
        'hard': [],
        'insane': [],
        'custom': []
    }


class User:
    def __init__(self, definition:UserJSON):
        self._nick = definition['nick']
        self._age = definition['age']
        self._gender = definition['gender']
        self._preferred_color = definition['preferred_color']
        self._preferred_difficulty = definition.get(
            'preferred_difficulty',DEFAULT_PREFERRED_DIFFICULTY
        )
        self._custom_difficulty = difficulty.Difficulty(
            **definition.get('custom_difficulty',default_difficulty())
        )
        self._scores = definition.get('scores',default_scores())

    @property
    def nick(self) -> str:
        return self._nick

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, gender: str) -> None:
        self._gender = gender

    @property
    def preferred_color(self) -> str:
        return self._preferred_color
    
    @property
    def preferred_difficulty(self) -> str:
        return self._preferred_difficulty

    @preferred_difficulty.setter
    def preferred_difficulty(self, type:str) -> None:
        self._preferred_difficulty = type

    @property
    def scores(self) -> dict[str, list[int]]:
        return self._scores

    def update_score(self, difficulty: str, value: int) -> None:
        self._scores[difficulty].append(value)
        if len(self._scores[difficulty]) > RESULTS_LENGTH:
            self._scores[difficulty].pop(0)

    def get_score(self, difficulty: str) -> list[int]:
        return self._scores[difficulty]

    @property
    def sorted_scores(self) -> dict[str, list[int]]:
        return {
            difficulty: sorted(results) for difficulty, results in self._scores.items()
        }

    def to_json(self) -> UserJSON:
        return {
            'nick': self._nick,
            'age': self._age,
            'gender': self._gender,
            'preferred_color': self._preferred_color,
            'preferred_difficulty': self._preferred_difficulty,
            'custom_difficulty': self._custom_difficulty.to_json(),
            'scores': self._scores
        }


def default_user() -> User:
    return User({
        'nick': 'default',
        'age': 0,
        'gender': 'undefined',
        'preferred_color': 'undefined',
        'preferred_difficulty': 'undefined',
        'custom_difficulty': default_difficulty(),
        'scores': default_scores()
    })


class UsersController:
    def __init__(self, users_path: str, default_user: str = ''):
        self._file_path = users_path
        raw_users: dict[str, UserJSON] = file.load_json(users_path)
        self._users = {
            nick: User(definition) for nick, definition in raw_users.items()
        }
        self._current_user: str = default_user
        observer.subscribe(difficulty.UPDATE_DIFFICULTY_TYPE,self._update_user_difficulty)
    

    @property
    def user_list(self) -> list[User]:
        return [user for _, user in self._users.items()]

    def users_transform(self, fn: Callable[[User], Any]) -> list[Any]:
        return [fn(user) for _, user in self._users.items()]

    def user(self, nick: str) -> User:
        return self._users[nick]

    def user_transform(self, nick: str, fn: Callable[[User], Any]) -> User:
        return fn(self._users[nick])

    @property
    def current_user(self) -> User:
        return self._users.get(
            self._current_user, default_user()
        )

    @current_user.setter
    def current_user(self, nick: str) -> None:
        self._current_user = nick
        observer.post_event(constants.USER_CHANGE, self.current_user)
    
    def _update_user_difficulty(self, type: str) -> None:
        self.current_user.preferred_difficulty = type

    def _save_users(self) -> None:
        file.save_json(
            self._file_path,
            {nick: user.to_json() for nick, user in self._users.items()},
        )

    def save(self) -> None:
        self._save_users()
