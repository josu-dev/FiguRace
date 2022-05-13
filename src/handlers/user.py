from typing import Any, Callable, TypedDict

from src import file


class UserJSON(TypedDict):
    nick: str
    age: int
    gender: str
    prefered_color: str
    scores: list[int]


class User:
    def __init__(self, nick: str, age: int, gender: str, prefered_color: str, scores: list[int] | None = None):
        self._nick = nick
        self._age = age
        self._gender = gender
        self._prefered_color = prefered_color
        self._scores = [] if scores == None else scores

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
    def prefered_color(self) -> str:
        return self._prefered_color

    @property
    def scores(self) -> list[int]:
        return self._scores

    def update_score(self, lvl: int, value: int) -> None:
        if lvl > len(self._scores):
            self._scores.append(value)
        else:
            self._scores[lvl - 1] += value

    def get_score(self, lvl: int) -> int:
        if lvl > len(self._scores):
            return 0
        else:
            return self._scores[lvl - 1]

    @property
    def overall_score(self) -> int:
        return sum(self._scores)

    def to_dict(self) -> UserJSON:
        return {
            'nick': self._nick,
            'age': self._age,
            'gender': self._gender,
            'prefered_color': self._prefered_color,
            'scores': self._scores
        }


class UsersController:
    def __init__(self, users_path: str, default_user: str = ''):
        self._file_path = users_path
        raw_users: dict[str, UserJSON] = file.load_json(users_path)
        self._users = {
            nick: User(**definition) for nick, definition in raw_users.items()
        }
        self._current_user: str = default_user

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
        return self._users[self._current_user]

    @current_user.setter
    def current_user(self, nick: str) -> None:
        self._current_user = nick

    def _save_users(self) -> None:
        file.save_json(
            self._file_path,
            {nick: user.to_dict() for nick, user in self._users.items()},
        )

    def save(self) -> None:
        self._save_users()
