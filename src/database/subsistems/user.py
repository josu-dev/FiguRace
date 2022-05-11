import json
from os import path
from typing import Any, Callable, TypedDict

from ..paths import DATA_PATH

USERS_PATH = path.join(DATA_PATH, 'users.json')

class UserDefinition(TypedDict):
    nick: str
    age : int
    gender : str
    scores : list[int]
    overall_score : int
    prefered_color: str

class User:
    def __init__(self, definition: UserDefinition):
        self._nick = definition['nick']
        self._age = definition['age']
        self._gender = definition['gender']
        self._scores = definition['scores']
        self._overall_score = definition['overall_score']
        self._prefered_color = definition['prefered_color']
    
    @property
    def nick(self) -> str:
        return self._nick
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, age:int) -> None:
        self._age = age
    
    @property
    def gender(self) -> str:
        return self._gender
    
    @gender.setter
    def gender(self, gender:str) -> None:
        self._gender = gender
    
    @property
    def prefered_color(self) -> str:
        return self._prefered_color

    @property
    def scores(self) -> list[int]:
        return self._scores
    
    def update_score(self, lvl:int, value:int) -> None:
        self._overall_score += 0
        if lvl > len(self._scores):
            self._scores.append(value)
        else:
            self._scores[lvl -1] += value
    
    def get_score(self, lvl:int) -> int:
        if lvl > len(self._scores):
            return 0
        else:
            return self._scores[lvl -1]

    @property
    def overall_score(self) -> int:
        return self._overall_score


def create_user(nick:str, gender:str, age:int, prefered_color:str):
    user_definition : UserDefinition = {
        'nick' : nick,
        'age' : age,
        'gender' : gender,
        'scores' : [],
        'overall_score':0,
        'prefered_color':prefered_color
    }
    return User(user_definition)

def load_users() -> list[UserDefinition]:
    with open(USERS_PATH, mode='r', encoding='utf-8') as file:
        users = json.load(file)
        return users

def save_users(users : list[User]) -> None:
    with open(USERS_PATH, mode='w', encoding='utf-8') as file:
        json.dump(users, file)


class UsersController:
    def __init__(self):
        raw_users = load_users()
        self._users = [User(raw_user) for raw_user in raw_users]
        self._current_user = -1
    
    def _find_user(self, nick:str) -> User:
        for user in self._users:
            if user.nick == nick:
                return user
        raise Exception(f'User {nick} hasnt been registered')
    
    @property
    def users(self) -> list[User]:
        return [user for user in self._users]
    
    def users_transform(self, fn:Callable[[User],Any]) -> list[Any]:
        return [fn(user) for user in self._users]
    
    def user(self, nick: str) -> User:
        return self._find_user(nick)
    
    def user_transform(self, nick: str, fn:Callable[[User],Any]) -> User:
        return fn(self._find_user(nick))
    
    @property
    def current_user(self) -> User:
        return self._users[self._current_user]
    
    @current_user.setter
    def current_user(self, nick:str) -> None:
        self._current_user = self._users.index(self._find_user(nick))
    
    def exit(self) -> None:
        save_users(self._users)