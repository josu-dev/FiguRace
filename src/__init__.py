from .database import file
from .components import custom_sg as csg
from .handlers.user import UsersController

from src import constants as const

users_controller = UsersController(const.PATH_USERS)
