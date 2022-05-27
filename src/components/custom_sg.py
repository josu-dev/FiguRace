from abc import ABC, abstractmethod
from typing import Any

import PySimpleGUI as sg


Element = sg.Element | sg.Column | sg.Text | sg.Button | sg.Input | sg.Multiline | sg.Frame | sg.Combo | sg.Listbox
LayoutRow = list[Element]
FullLayout = list[LayoutRow]


class ChainedElement(ABC):
    @abstractmethod
    def __init__(self, **column_parameters: Any):
        ...

    @abstractmethod
    def add(self, content: Element | LayoutRow | FullLayout) -> Any:
        ...

    @abstractmethod
    def pack(self) -> sg.Column:
        ...


class HorizontalList(ChainedElement):
    def __init__(self, **column_parameters: Any):
        self._container: list[Element] = []
        self._config = column_parameters

    def add(self, content: Element | LayoutRow | FullLayout) -> 'HorizontalList':
        match content:
            case [[*_], *_]:
                element = sg.Column(content, **self._config)
            case [*_]:
                element = sg.Column([content], **self._config)
            case _:
                element = content
        self._container.append(element)
        return self

    def pack(self):
        return sg.Column([self._container], **self._config)


class VerticalList(ChainedElement):
    def __init__(self, **column_parameters: Any):
        self._container: FullLayout = []
        self._config = column_parameters

    def add(self, content: Element | LayoutRow | FullLayout) -> 'VerticalList':
        match content:
            case [[*_], *_]:
                element = [sg.Column(content, **self._config)]
            case [*_]:
                element = content
            case _:
                element = [content]
        self._container.append(element)
        return self

    def pack(self):
        return sg.Column(self._container, **self._config)


def CenteredElement(element: Element, **column_parameters: Any) -> sg.Column:
    column_parameters['element_justification'] = 'center'
    column_parameters['expand_y'] = True
    column_parameters['expand_x'] = True
    background_color = column_parameters.get('background_color', None)
    return sg.Column(
        [
            [sg.VPush(background_color)],
            [element],
            [sg.VPush(background_color)]
        ],
        **column_parameters
    )


def CenteredLayout(layout: FullLayout, **column_parameters: Any) -> sg.Column:
    column_parameters['element_justification'] = 'c'
    column_parameters['expand_y'] = True
    column_parameters['expand_x'] = True

    return sg.Column(layout, **column_parameters)


def horizontal_spacer(padding: tuple[int, int] = (0, 0), background_color: str | None = None) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=background_color)


def vertical_spacer(padding: tuple[int, int] = (0, 0), background_color: str | None = None) -> sg.Column:
    return sg.Column([[]], size=padding, background_color=background_color)
