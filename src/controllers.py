"""
    Controllers consumed on the app that manage all the informations of the
    difficulty, users, settings, theme, datasets, game run.
"""
from . import constants
from .handlers import observer
from .handlers.card import CardController
from .handlers.difficulty import DifficultyController
from .handlers.user import UsersController
from .handlers.setting import SettingsController
from .handlers.theme import ThemeController
from .handlers.run import RunController


settings_controller = SettingsController(constants.PATH_SETTINGS)
settings = settings_controller.settings

users_controller = UsersController(constants.PATH_USERS, settings.default_user)

difficulty_controller = DifficultyController(
    constants.PATH_DIFFICULTIES, users_controller.current_user.preferred_difficulty
)

theme_controller = ThemeController(constants.PATH_THEME, settings.theme)
theme = theme_controller.theme

cards_controller = CardController(constants.PATH_DATASETS)

run_controller = RunController(cards_controller, difficulty_controller)


observer.subscribe(constants.EXIT_APLICATION, settings_controller.save)
observer.subscribe(constants.EXIT_APLICATION, users_controller.save)
observer.subscribe(constants.EXIT_APLICATION, difficulty_controller.save)
