from abc import ABC, abstractmethod
from typing import Any

import PySimpleGUI as sg

from src import constants


Element = Any
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


def CenteredElement(element: Element, horizontal_only: bool = False, **column_parameters: Any) -> sg.Column:
    column_parameters['element_justification'] = 'center'
    column_parameters['expand_y'] = not horizontal_only
    column_parameters['expand_x'] = True
    background_color = column_parameters.get('background_color', None)
    if horizontal_only:
        return sg.Column(
            [
                [element]
            ],
            **column_parameters
        )
    return sg.Column(
        [
            [sg.VPush(background_color)],
            [element],
            [sg.VPush(background_color)]
        ],
        **column_parameters
    )


def CenteredLayout(layout: FullLayout, horizontal_only: bool = False, **column_parameters: Any) -> sg.Column:
    column_parameters['element_justification'] = 'center'
    column_parameters['expand_y'] = not horizontal_only
    column_parameters['expand_x'] = True
    background_color = column_parameters.get('background_color', None)
    if horizontal_only:
        return sg.Column(
            layout,
            **column_parameters
        )
    return sg.Column(
        [
            [sg.VPush(background_color)],
            *layout,
            [sg.VPush(background_color)]
        ],
        **column_parameters
    )


def horizontal_spacer(width: int, background_color: str | None = None) -> sg.Column:
    return sg.Column([[]], size=(width, 0), background_color=background_color)


def vertical_spacer(height: int, background_color: str | None = None) -> sg.Column:
    return sg.Column([[]], size=(0, height), background_color=background_color)


def custom_popup(layout: FullLayout, close_keys: list[str], background_color: str | None = None, duration: int | None= None) -> str:
    window = sg.Window(
        '', layout, background_color=background_color,
        no_titlebar=True, keep_on_top=True, finalize=True,
        margins=(0, 0), resizable=False, modal=True
    )
    
    while True:
        event, _ = window.read(timeout=duration, timeout_key='-TIME-OUT-')
        if event is None or event == '-TIME-OUT-':
            event = constants.EXIT_APLICATION
            break
        if event in close_keys:
            break

    window.close()
    return event
