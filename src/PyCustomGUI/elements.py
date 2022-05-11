from contextlib import contextmanager
import PySimpleGUI as sg


@contextmanager
def open_window(window: sg.Window):
    try:
        yield window
    except Exception as error:
        raise error
    finally:
        print('ClosingWindow')
        window.close()


class OpenWindow:
    def __init__(self, window: sg.Window):
        self.window = window

    def __enter__(self):
        return self.window

    def __exit__(self, exc_type, exc_value, traceback):
        self.window.close()


class CustomList:
    def __init__(self):
        self.contenedor = []
        self.buttons = []

    def add(self, fila):
        self.contenedor.append(fila)
        self.buttons.append(fila[0])
        return self

    def pack(self):
        return sg.Column(self.contenedor), self.buttons


class CustomHList:
    def __init__(self, backgraund):
        self.contenedor = []
        self.backgraund = backgraund

    def add(self, layout, *args, **kwargs):
        element = sg.Column(layout, *args, **kwargs)
        self.contenedor.append(element)
        return self

    def pack(self):
        return sg.Column([self.contenedor], background_color=self.backgraund, justification='c')


def CenterElement(element):
    return sg.Column([
        [sg.VPush(background_color='#112B3C')],
        [element],
        [sg.VPush(background_color='#112B3C')]
    ],        
        justification='center',
        background_color='#112B3C',
        # background_color='#112B3C',
        # pad=(150,150)
        expand_y=True
    )
