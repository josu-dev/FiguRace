from . import constants, controllers as ctr
from .handlers import observer, window as window_ctr
from .screens import introduction, menu, configuration, game, ranking, configure_game, result, select_profile, edit_profile, create_user


def main():
    screens = [
        # introduction.screen,
        select_profile.screen, edit_profile.screen, create_user.screen,
        menu.screen, configuration.screen, ranking.screen,
        configure_game.screen, game.screen, result.screen
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
