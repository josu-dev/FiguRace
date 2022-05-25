from typing import Any

import PySimpleGUI as sg

from src import constants
from src.controllers import theme

from . import custom_sg as csg


ImageFile = Any


def screen_title(title: str, spaced: bool = False, alignment: str = 'center', upper: bool = True) -> sg.Text:
    if upper:
        title = title.upper()
    if spaced:
        title = ' '.join(list(title.strip()))
    return sg.Text(
        title,
        size=(len(title), 1),
        background_color=theme.BG_BASE,
        text_color=theme.TEXT_ACCENT,
        font=(theme.FONT_FAMILY, 80),
        justification=alignment,
        pad=32,
        expand_x=True
    )


def goback_button(text: str = 'Volver', border: int = 8, padding: int = 0) -> sg.Button:
    return sg.Button(
        text,
        key=f'{constants.GOTO_VIEW} {constants.LAST_SCREEN}',
        auto_size_button=True,
        button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
        pad=padding,
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=border
    )


def image_button(image: ImageFile, key: str, border: int = 8, padding: int = 0) -> sg.Button:
    return sg.Button(
        key=key,
        image_data=image.source,
        auto_size_button=True,
        button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
        pad=padding,
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=border
    )
