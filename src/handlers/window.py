import importlib
import os
from typing import Any

import PySimpleGUI as sg

from src import constants, file

from . import observer, screen


class WindowController:
    def __init__(self) -> None:
        self._screen_ctr = screen.ScreenController()
        self._window: sg.Window
        self._timeout: int | None = None
        self._timeout_key: str = constants.TIME_OUT
        observer.subscribe(constants.UPDATE_TIMEOUT, self.set_timeout)

    def init(self, screens_folder_path: str, initial_screen: str, title: str, app_icon: Any = None, fullscreen: bool = True) -> None:
        path_names = screens_folder_path.split(os.path.sep)
        base_to_folder = path_names[path_names.index('src'):]
        for file_name, _ in file.scan_dir(screens_folder_path, 'py'):
            if file_name.startswith('_'):
                continue
            names = base_to_folder + [file_name.split('.')[0]]
            module = importlib.import_module('.'.join(names))
            self._screen_ctr.register(module.screen)

        self._window = sg.Window(
            title,
            self._screen_ctr.composed_layout,
            icon=app_icon.source if app_icon else None,
            finalize=True,
            element_justification='center',
            resizable=True,
            margins=(0, 0)
        )

        if fullscreen:
            self._window.maximize()

        self._screen_ctr.init(initial_screen)

    def loop(self) -> None:
        try:
            while True:
                event, _ = self._window.read(
                    timeout=self._timeout, timeout_key=self._timeout_key
                )
                if event is None or event.startswith(constants.EXIT_APLICATION):
                    break

                event = event.split()
                if len(event) == 1:
                    observer.post_event(event[0])
                else:
                    observer.post_event(event[0], *event[1:])
        except Exception as error:
            raise error
        finally:
            observer.post_event(constants.EXIT_APLICATION)
            self._window.close()

    def set_timeout(self, duration: int | None = None, key: str = constants.TIME_OUT) -> None:
        self._timeout = duration if duration else None
        self._timeout_key = key
