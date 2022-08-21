import PySimpleGUI as sg

from ..controllers import observer, theme, theme_controller as theme_ctr, settings
from . import _common, _csg


SCREEN_NAME = '-CONFIGURE-THEME-'
THEME_OPTIONS_COMBO = '-THEME-OPTIONS-COMBO-'
CHOOSE_THEME = '-CHOOSE-THEME-'


themes_combo = _common.styled_combo(
    theme_ctr.theme_list,
    theme_ctr.theme_name,
    THEME_OPTIONS_COMBO,
    True
)

confirm_button = sg.Button(
    'Confirmar',
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    mouseover_colors=theme.BG_BUTTON_HOVER,
    font=(theme.FONT_FAMILY, theme.T1_SIZE),
    pad=theme.scale(32),
    disabled=True,
    key=CHOOSE_THEME,
    border_width=theme.BD_PRIMARY
)


def update_confirm_button() -> None:
    confirm_button.update(
        disabled=themes_combo.get() == settings.theme
    )


observer.subscribe(THEME_OPTIONS_COMBO, update_confirm_button)


def confirm_theme_selection() -> None:
    settings.theme = themes_combo.get()
    update_confirm_button()
    _csg.custom_popup(
        [
            [sg.Text(
                f'El tema \'{settings.theme}\' ahora es el predefinido\nReinicie para ver los cambios',
                font=(theme.FONT_FAMILY, theme.T1_SIZE),
                text_color=theme.TEXT_ACCENT,
                background_color=theme.BG_SECONDARY,
                pad=theme.scale(32),
                justification='center'
            )],
            [_csg.centered(
                sg.Button(
                    'Aceptar',
                    font=(theme.FONT_FAMILY, theme.T1_SIZE),
                    pad=theme.scale(32),
                    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
                    mouseover_colors=theme.BG_BUTTON_HOVER,
                    border_width=theme.BD_SECONDARY
                ),
                True,
                background_color=theme.BG_SECONDARY
            )]
        ],
        background_color=theme.BG_SECONDARY,
    )


observer.subscribe(CHOOSE_THEME, confirm_theme_selection)


screen_layout = [
    [
        _common.screen_title('configurar tema', True)],
    [
        _csg.centered(themes_combo, background_color=theme.BG_BASE)],
    [
        sg.Push(theme.BG_BASE),
        confirm_button,
        sg.Push(theme.BG_BASE)],
    [
        sg.VPush(theme.BG_BASE)],
    [
        _common.navigation_button(
            'Menu Principal', '-MENU-', padding=(theme.scale(64),)*2,
        ),
        sg.Push(theme.BG_BASE)],
]


screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}


def screen_reset() -> None:
    '''This function resets the elements of the screen to defaults/configuration values.
    It runs every time that window view moves to this screen.'''
    themes_combo.update(value=settings.theme)
    update_confirm_button()
