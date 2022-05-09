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