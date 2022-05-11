import PySimpleGUI as sg

from .handlers import observer
from .handlers import window as window_c
from .database import database as db

def main():
    theme = db.theme
    window = window_c.window_set_up()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, window_c.EXIT_APLICATION):
            observer.post_event(window_c.EXIT_APLICATION)
            break

        event = event.split()
        if len(event) == 1:
            observer.post_event(event[0], None)
        else:
            observer.post_event(event[0], *event[1:])

    window.close()


if __name__ == '__main__':
    main()
