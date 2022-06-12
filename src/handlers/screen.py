from typing import Any, Callable

import PySimpleGUI as sg

from src import constants

from . import observer


class Screen:
    def __init__(self, key: str, layout: list[list[Any]], config: dict[str, Any], reset: Callable[..., None]) -> None:
        config['key'] = key
        config['visible'] = False
        config['expand_x'] = True
        config['expand_y'] = True
        config['pad'] = 0
        self.key = key
        self.is_visible = False
        self.container = sg.Column(layout, **config)
        self._reset = reset

    def turn_visivility(self) -> None:
        self.is_visible = not self.is_visible
        self.container.update(visible=self.is_visible)
        if self.is_visible:
            self.reset()

    def reset(self) -> None:
        self._reset()


class ScreenController:
    def __init__(self) -> None:
        self._actual_layout: str = ''
        self._layout_stack: list[str] = []
        self._layouts: dict[str, Screen] = {}
        self._composed_layout: list[sg.Element] = []
        observer.subscribe(constants.GOTO_VIEW, self.goto_layout)

    def goto_layout(self, key: str) -> None:
        key = key.rstrip('0123456789')
        self._layouts[self._actual_layout].turn_visivility()
        if key == constants.LAST_SCREEN:
            self._actual_layout = self._layout_stack.pop()
        elif key in self._layout_stack:
            while self._layout_stack.pop() != key:
                continue
            self._actual_layout = key
        else:
            self._layout_stack.append(self._actual_layout)
            self._actual_layout = key

        self._layouts[self._actual_layout].turn_visivility()

    def register(self, screen: Screen) -> None:
        if screen.key in self._layouts:
            raise Exception(
                f'Already registered a screen with key {screen.key}')
        self._layouts[screen.key] = screen
        self._composed_layout.append(screen.container)

    @property
    def composed_layout(self) -> list[list[sg.Element]]:
        return [self._composed_layout]

    def init(self, key: str) -> None:
        if key not in self._layouts:
            raise Exception(f'Screen with key \'{key}\' wasn\'t registered')
        self._actual_layout = key
        self._layouts[key].turn_visivility()
