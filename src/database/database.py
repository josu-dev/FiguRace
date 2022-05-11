from os import path
from src import constants as const
from src.database.app import load_app_settings
from src.database.user import UsersController
from src.handlers import observer

DATA_PATH = path.join(path.dirname(__file__), 'data')

app = load_app_settings()

users = UsersController()

observer.subscribe(const.EXIT_APLICATION, users.exit)
