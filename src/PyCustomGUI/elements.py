from contextlib import contextmanager
from typing import Any

import PySimpleGUI as sg


Element = sg.Element | sg.Column | sg.Text | sg.Button | sg.Input | sg.Multiline | sg.Frame | sg.Combo | sg.Listbox
ElementLayout = list[list[Element]]


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

    def __exit__(self, exc_type:Any, exc_value:Any, traceback:Any):
        self.window.close()


class HorizontaElementlList:
    def __init__(self, **column_parameters: Any):
        self._container: list[Element] = []
        self._config = column_parameters

    def add(self, element: Element):
        self._container.append(element)
        return self

    def pack(self):
        return sg.Column([self._container], **self._config)


class VerticaElementlList:
    def __init__(self, **column_parameters: Any):
        self._container: list[list[Element]] = []
        self._config = column_parameters

    def add(self, element: Element):
        self._container.append([element])
        return self

    def pack(self):
        return sg.Column(self._container, **self._config)


class HorizontalList:
    def __init__(self, **column_parameters: Any):
        self._container: list[sg.Column] = []
        self._config = column_parameters

    def add(self, layout: ElementLayout):
        element = sg.Column(layout, **self._config)
        self._container.append(element)
        return self

    def pack(self):
        return sg.Column([self._container], **self._config)


class VerticalList:
    def __init__(self, **column_parameters: Any):
        self._container: list[list[Element]] = []
        self._config = column_parameters

    def add(self, layout: ElementLayout):
        element = sg.Column(layout, **self._config)
        self._container.append([element])
        return self

    def pack(self):
        return sg.Column(self._container, **self._config)


def CenteredElement(element: Element, **column_parameters: Any) -> sg.Column:
    column_parameters['justification'] = 'c'
    column_parameters['expand_y'] = True
    column_parameters['expand_x'] = True
    background_color = None if 'background_color'not in column_parameters else column_parameters[
        'background_color']
    return sg.Column(
        [
            [sg.VPush(background_color)],
            [element],
            [sg.VPush(background_color)]
        ],
        **column_parameters
    )


def CenteredLayout(layout: ElementLayout, **column_parameters: Any) -> sg.Column:
    column_parameters['justification'] = 'c'
    column_parameters['expand_y'] = True
    column_parameters['expand_x'] = True

    return sg.Column(
        layout,
        **column_parameters
    )
