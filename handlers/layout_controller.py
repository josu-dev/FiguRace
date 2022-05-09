from typing import Any
import PySimpleGUI as sg

ElementLayout = list[list[sg.Element]]
class LayoutHandler:
    def __init__(self):
        self.actual_layout: str
        self.window : sg.Window
        self.layout_stack : list[str] = []
        self.layouts : list[str] = []
        self.window_layout : list[sg.Element] = []

    def goto_layout(self, key:str) -> None:
        self.layout_stack.append(self.actual_layout)
        self.window[self.actual_layout].update(visible=False)
        self.actual_layout = key
        self.window[key].update(visible=True)
    
    def exit_layout(self) -> None:
        new_layout = self.layout_stack.pop()
        self.window[self.actual_layout].update(visible=False)
        self.actual_layout = new_layout
        self.window[self.actual_layout].update(visible=True)
    
    def registry(self, layout: ElementLayout, key : str) -> None:
        self.layouts.append(key)
        self.window_layout.append(sg.Column(layout=layout, key=key, visible=False))

    def create_window(self, starting_layout : str, window_config : dict[Any, Any]) -> sg.Window:
        self.window = sg.Window(layout=[self.window_layout], **window_config)
        self.actual_layout = starting_layout
        self.window[self.actual_layout].update(visible=True)
        return self.window
