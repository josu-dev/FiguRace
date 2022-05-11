import PySimpleGUI as sg
from .handlers import observer
from .handlers import window as window_c


def main():
    window = window_c.window_set_up()

    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event.startswith(window_c.EXIT_APLICATION):
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
