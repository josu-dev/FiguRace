
from src import constants
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

observer.subscribe(constants.EXIT_APLICATION, settings_controller.save)
observer.subscribe(constants.EXIT_APLICATION, users_controller.save)