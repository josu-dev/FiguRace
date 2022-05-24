import PySimpleGUI as sg

from src.controllers import theme

from . import custom_sg as csg


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
        pad=32
    )
