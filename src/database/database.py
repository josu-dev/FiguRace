from os import path

from src.database.subsistems.app import load_app_settings
from src.database.subsistems.user import UsersController
from src.handlers import observer, window

from src.database.subsistems.theme import Theme

DATA_PATH = path.join(path.dirname(__file__), 'data')

theme = Theme()

app = load_app_settings()

users = UsersController()

observer.subscribe(window.EXIT_APLICATION, users.exit)
