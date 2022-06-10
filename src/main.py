"""
    Initialize the execution of the program and configure everything necessary.
"""
from . import constants, controllers as ctr
from .assets import app_icon
from .handlers import window
from .screens import create_profile, introduction, menu, configuration, game, ranking, configure_game, result, select_profile


def main() -> None:
    """
        Register the screens of the app.
        Initializes the Window Controller and setup all for the visualization of the app.
        Runs the aplication loop.
    """
    screens = [
        introduction.screen,
        select_profile.screen, create_profile.screen,
        menu.screen, configuration.screen, ranking.screen,
        configure_game.screen, game.screen, result.screen
    ]

    window_ctr = window.WindowController()

    window_ctr.init(
        screens,
        ctr.settings.starting_page,
        ctr.settings.title,
        app_icon,
        ctr.settings.full_screen
    )

    window_ctr.loop()


def main_dev(args: list[str]) -> None:
    duration = 5 * 1000
    initial_screen = '-SELECT-PROFILE-'
    for arg in args:
        match arg.split(':'):
            case '-to', timeout:
                if not timeout.isdecimal():
                    print(f'Argument error: value for flag -to must be an integer, invalid \'{timeout}\'')
                    return
                timeout = int(timeout)
                if timeout == 0:
                    print(f'Argument error: value for flag -to must be greater than 0')
                    return
                duration = int(timeout) * 1000
            case '-is', screen:
                initial_screen = screen
            case _:
                pass

    screens = [
        introduction.screen,
        select_profile.screen, create_profile.screen,
        menu.screen, configuration.screen, ranking.screen,
        configure_game.screen, game.screen, result.screen
    ]

    for screen in screens:
        if screen.key == initial_screen:
            break
    else:
        print(f'Argument error: value for flag -is must be a registered screen, invalid \'{initial_screen}\'')
        return

    window_ctr = window.WindowController()

    window_ctr.init(
        screens,
        initial_screen,
        ctr.settings.title,
        app_icon,
        ctr.settings.full_screen
    )
    window_ctr.set_timeout(duration, constants.EXIT_APLICATION)

    window_ctr.loop()


if __name__ == '__main__':
    main()
