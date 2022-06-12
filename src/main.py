'''Initialize the execution of the application and configure everything necessary.'''
from . import constants, controllers as ctr
from .assets import app_icon
from .handlers import window


def main() -> None:
    '''Creates the application.

    - Set up everything necessary.
    - Initialize it.
    - Runs the event loop.
    '''

    window_ctr = window.WindowController()

    window_ctr.init(
        constants.PATH_SCREENS,
        ctr.settings.starting_page,
        ctr.settings.title,
        app_icon,
        ctr.settings.full_screen
    )

    window_ctr.loop()


def main_dev(args: list[str]) -> None:
    '''Creates the application on developer mode.

    - Set up everything necessary.
    - Initialize it.
    - Runs the event loop.

    Args:
        args: list of developer arguments passed through the command line
    '''
    duration = 5 * 1000
    initial_screen = '-SELECT-PROFILE-'
    for arg in args:
        match arg.split('='):
            case '--to', timeout:
                if not timeout.isdecimal():
                    print(f'Argument error: value for flag -to must be an integer, invalid \'{timeout}\'')
                    return
                timeout = int(timeout)
                if timeout == 0:
                    print(f'Argument error: value for flag -to must be greater than 0')
                    return
                duration = int(timeout) * 1000
            case '--is', screen:
                initial_screen = screen
            case _:
                pass

    window_ctr = window.WindowController()

    window_ctr.init(
        constants.PATH_SCREENS,
        initial_screen,
        ctr.settings.title,
        app_icon,
        ctr.settings.full_screen
    )
    window_ctr.set_timeout(duration, constants.EXIT_APLICATION)

    window_ctr.loop()


if __name__ == '__main__':
    main()
