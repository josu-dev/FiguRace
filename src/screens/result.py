import PySimpleGUI as sg

from src import csg, common
from src.controllers import theme, run_controller as run_ctr
from src.handlers.screen import Screen


SCREEN_NAME = '-RESULT-'
FIELD_MAX_CHARACTERS = 32

summary: dict[str, sg.Text] = {}


def create_stat_type(text: str, width: int | None = None) -> sg.Text:
    return sg.Text(
        text,
        size=(width, 1),
        font=(theme.FONT_FAMILY, theme.T1_SIZE),
        pad=(theme.T1_SIZE//3)*2,
        text_color=theme.TEXT_PRIMARY,
        background_color=theme.BG_PRIMARY,
    )


def create_stat_field(name: str, key: str) -> sg.Column:
    width = FIELD_MAX_CHARACTERS - len(name)
    summary[key] = create_stat_type(' ', width)
    return sg.Column(
        [[create_stat_type(name), summary[key]]],
        background_color=theme.BG_PRIMARY
    )


def create_summary() -> sg.Column:
    left_layout = [
        [create_stat_field('Total rondas:', 'total_rounds')],
        [create_stat_field('Rondas completadas:', 'rounds_complete')],
        [create_stat_field('Rondas ganadas:', 'rounds_winned')],
        [create_stat_field('Tiempo total:', 'total_time')],
        [create_stat_field('Total intentos:', 'total_tryes')],
    ]
    right_layout = [
        [create_stat_field('Puntos totales:', 'total_points')],
        [create_stat_field('Rondas salteadas:', 'rounds_skiped')],
        [create_stat_field('Rondas perdidas:', 'rounds_loosed')],
        [create_stat_field('Tiempo promedio:', 'average_time')],
        [create_stat_field(' ', 'undefined')],
    ]

    return sg.Column(
        [[
            sg.Column(left_layout, background_color=theme.BG_PRIMARY),
            csg.horizontal_spacer(theme.scale(32), background_color=theme.BG_SECONDARY),
            sg.Column(right_layout, background_color=theme.BG_PRIMARY),
        ]],
        background_color=theme.BG_SECONDARY
    )


def refresh_summary() -> None:
    for key, value in run_ctr.stats.items():
        summary[key].update(str(value))


def create_nav_buttons() -> sg.Column:
    padding = (theme.scale(16), theme.scale(16))
    buttons = [
        common.navigation_button('Menu Principal', '-MENU-', padding=padding),
        common.navigation_button('Volver a Jugar', '-GAME-', padding=padding),
        common.navigation_button('Nuevo Juego', '-CONFIGURE-GAME-', padding=padding),
    ]
    return sg.Column(
        [buttons],
        background_color=theme.BG_BASE,
        element_justification='center'
    )


screen_layout = [
    [common.screen_title('resultado', True)],
    [csg.vertical_spacer(theme.scale(32), background_color=theme.BG_BASE)],
    [create_summary()],
    [csg.vertical_spacer(theme.scale(32), background_color=theme.BG_BASE)],
    [create_nav_buttons()]
]

screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'center',
}


def reset():
    refresh_summary()


screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
