import PySimpleGUI as sg
from src import constants as const
from .handlers import observer
from .handlers import window as window_c

def main():
    
    window = window_c.window_set_up()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event.startswith(const.EXIT_APLICATION):
            observer.post_event(const.EXIT_APLICATION)
            break

        event = event.split()
        if len(event) == 1:
            observer.post_event(event[0], None)
        else:
            observer.post_event(event[0], *event[1:])

    window.close()


if __name__ == '__main__':
    main()
