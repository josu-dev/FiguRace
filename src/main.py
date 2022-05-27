from . import constants, controllers as ctr

from .handlers import observer
from .handlers import window as window_ctr
from .screens import menu, configuration, game, score, configure_game,presentation
from .screens.profile import create_profile, select_profile,edit_profile


def main():
    screens = [
        presentation.screen,
        select_profile.screen, create_profile.screen,edit_profile.screen,
        menu.screen, configuration.screen,
        configure_game.screen, game.screen, score.screen
    ]

    window = window_ctr.set_up(
        screens, ctr.settings.title,
        ctr.settings.starting_page, ctr.settings.full_screen
    )

    # Uncomment to see aplication events
    # for key, val in observer.subscribers.items():
    #     print(key, ':', [fn.__name__ for fn in val])
    
    while True:
        event, _ = window.read()
        if event is None or event.startswith(constants.EXIT_APLICATION):
            observer.post_event(constants.EXIT_APLICATION)
            break

        event = event.split()
        if len(event) == 1:
            observer.post_event(event[0])
        else:
            observer.post_event(event[0], *event[1:])

    window.close()


if __name__ == '__main__':
    main()
