from src import constants

from src.handlers.card import CardController
from src.handlers.user import UsersController
from src.handlers.settings import SettingsController
from src.handlers.theme import ThemeController
from src.handlers import observer


settings_controller = SettingsController(
    constants.PATH_SETTINGS, constants.PATH_DIFFICULTIES
)
settings = settings_controller.setting

users_controller = UsersController(constants.PATH_USERS, settings.default_user)

theme_controller = ThemeController(constants.PATH_THEME, settings.theme)
theme = theme_controller.theme

cards_controller = CardController()

def update_user() -> None:
    settings.default_user = users_controller.current_user.nick

observer.subscribe(constants.EXIT_APLICATION, update_user)
observer.subscribe(constants.EXIT_APLICATION, settings_controller.save)
observer.subscribe(constants.EXIT_APLICATION, users_controller.save)
