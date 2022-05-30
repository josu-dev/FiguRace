from typing import Any

import PySimpleGUI as sg

from src import constants
from src.controllers import theme

from . import custom_sg as csg


ImageFile = Any


def screen_title(title: str, spaced: bool = False, alignment: str = 'center', upper: bool = True, size: int = theme.H2_SIZE, padding: int = 0) -> sg.Text:
    if upper:
        title = title.upper()
    if spaced:
        title = ' '.join(list(title.strip()))
    return sg.Text(
        title,
        size=(len(title), 1),
        background_color=theme.BG_BASE,
        text_color=theme.TEXT_ACCENT,
        font=(theme.FONT_FAMILY, size),
        justification=alignment,
        pad=padding if padding else (size//3)*2,
        expand_x=True
    )


def navigation_button(
    text: str, screen_name: str, font_size: int = theme.T1_SIZE,
    padding: tuple[int, int] = (0, 0), border: int = theme.BD_PRIMARY
) -> sg.Button:
    return sg.Button(
        text,
        key=f'{constants.GOTO_VIEW} {screen_name}',
        font=(theme.FONT_FAMILY, font_size),
        button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=border,
        pad=padding
    )


def goback_button(text: str, font_size: int = theme.H4_SIZE, padding: tuple[int, int] = (0, 0)) -> sg.Button:
    return navigation_button(text, constants.LAST_SCREEN, font_size, padding)


def image_button(image: ImageFile, size: tuple[int, int], key: str, border: int = theme.BD_PRIMARY, padding: int = 0) -> sg.Button:
    return sg.Button(
        key=key,
        image_size=size,
        image_subsample=(image.size//max(size)),
        image_data=image.source,
        auto_size_button=True,
        button_color=(theme.TEXT_PRIMARY, theme.BG_BUTTON),
        pad=padding,
        mouseover_colors=theme.BG_BUTTON_HOVER,
        border_width=border
    )
