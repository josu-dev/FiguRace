'''Controllers consumed on the application for managing and accessing states.'''
from . import constants
from .handlers import observer
from .handlers.card import CardController
from .handlers.difficulty import DifficultyController
from .handlers.user import UsersController
from .handlers.setting import SettingsController
from .handlers.run_event import RunEventController
from .handlers.run import RunController
from .handlers.theme import ThemeController


settings_controller = SettingsController(constants.PATH_SETTINGS)
settings = settings_controller.settings

users_controller = UsersController(constants.PATH_USERS, settings.default_user)

difficulty_controller = DifficultyController(
    constants.PATH_DIFFICULTIES, users_controller.current_user.preferred_difficulty
)

theme_controller = ThemeController(constants.PATH_THEME, settings.theme)
theme = theme_controller.theme

run_event_controller = RunEventController(constants.PATH_EVENTS)

cards_controller = CardController(constants.PATH_DATASETS)

run_controller = RunController(
    cards_controller, difficulty_controller, run_event_controller
)


observer.subscribe(constants.EXIT_APLICATION, settings_controller.save)
observer.subscribe(constants.EXIT_APLICATION, users_controller.save)
observer.subscribe(constants.EXIT_APLICATION, difficulty_controller.save)
observer.subscribe(constants.EXIT_APLICATION, run_event_controller.save)
