from os import path

from database.subsistems.app import load_app_settings

from subsistems.theme import Theme

DATA_PATH = path.join(path.dirname(__file__), 'data')

theme = Theme()

app = load_app_settings()

def 
# - Handle load of theme
# - Handle load, update, save of app settings