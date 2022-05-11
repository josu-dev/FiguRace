from os import path

from database.subsistems.app import load_app_settings
from database.subsistems.user import UsersController

from subsistems.theme import Theme

DATA_PATH = path.join(path.dirname(__file__), 'data')

theme = Theme()

app = load_app_settings()

users = UsersController()