import json
from os import path
from typing import TypedDict

from .paths import STORAGE_PATH


class UserContent(TypedDict):
    age : int
    gender : str
    score : list[int]

class UserDefinition(TypedDict):
    nick: str
    content: UserContent

def load_users() -> list[UserDefinition]:
    users_path = path.join(STORAGE_PATH, 'users.json')
    with open(users_path, mode='r', encoding='utf-8') as file:
        users = json.load(file)
        return users

def save_users(users : list[UserDefinition]) -> None:
    users_path = path.join(STORAGE_PATH, 'users.json')
    with open(users_path, mode='w', encoding='utf-8') as file:
        json.dump(file, file)

users = load_users()

def get_user_nicks() -> list[str]:
    nicks = [user['nick'] for user in users]
    return nicks

def get_user(nick : str) -> UserDefinition:
    for user in users:
        if user['nick'] == nick:
            return user
    return {
        'nick':'undefined',
        'content': {
            'age': 0,
            'gender': 'undefined',
            'score': [0]
        }
    }

def update_user(updated_user: UserDefinition) -> None:
    for index, user in enumerate(users):
        if user['nick'] == updated_user['nick']:
            users[index] = updated_user
            break
    save_users(users)