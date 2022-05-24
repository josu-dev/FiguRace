import PySimpleGUI as sg

from src import constants as const

from .handlers.settings import SettingsController
from .handlers.user import UsersController
from .handlers import observer
from .handlers import window as win_controller
from .screens import base_screen, menu, configuration, game, score
from .screens.profile import create_profile, select_profile


sett_controller = SettingsController(
    const.PATH_SETTINGS, const.PATH_DIFFICULTIES)

users_controller = UsersController(const.PATH_USERS)

observer.subscribe(const.EXIT_APLICATION, sett_controller.save)
observer.subscribe(const.EXIT_APLICATION, users_controller.save)


def main():
    screens = [
        base_screen.screen, select_profile.screen,
        create_profile.screen,
        menu.screen, configuration.screen, game.screen, score.screen
    ]

    window = win_controller.set_up(
        screens, sett_controller.setting.title,
        sett_controller.setting.starting_page, sett_controller.setting.full_screen
    )

    while True:
        event, _ = window.read()
        if event is None or event.startswith(const.EXIT_APLICATION):
            observer.post_event(const.EXIT_APLICATION)
            break

        event = event.split()
        if len(event) == 1:
            observer.post_event(event[0])
        else:
            observer.post_event(event[0], *event[1:])

    window.close()


if __name__ == '__main__':
    main()
