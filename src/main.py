"""
    Initialize the execution of the program and configure everything necessary.
"""
from . import controllers as ctr
from .assets import app_icon
from .handlers import window
from .screens import create_profile, introduction, menu, configuration, game, ranking, configure_game, result, select_profile


def main():
    """
        Register the screens of the app.
        Initializes the Window Controller and setup all for the visualization of the windows on the app.
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


if __name__ == '__main__':
    main()
