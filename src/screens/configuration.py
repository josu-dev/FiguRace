import PySimpleGUI as sg

from src import csg, common
from src.controllers import theme, difficulty_controller as difficulty_ctr, users_controller as user_ctr
from src.handlers import observer
from src.handlers.screen import Screen

SCREEN_NAME = "-CONFIGURATION-"
default_padding = 8
_font = (theme.FONT_FAMILY_TEXT, theme.T1_SIZE)
_padding = theme.width // 8


def build_text(text, unit, combo) -> list:
    result = [
        csg.horizontal_spacer(theme.width//16,
                              background_color=theme.BG_BASE),
        sg.Multiline(text,
                     disabled=True,
                     justification='left',
                     size=(25, 1),
                     font=_font,
                     text_color=theme.TEXT_ACCENT,
                     no_scrollbar=True,
                     background_color=theme.BG_BASE,
                     border_width=0,),
        csg.horizontal_spacer(theme.width//16,
                              background_color=theme.BG_BASE),
        sg.Text(unit, background_color=theme.BG_BASE),
        combo, ]
    return result


_cmb_time_per_game = sg.Combo(
    ('15', '30', '60', '90', '180', '300'),
    difficulty_ctr.difficulty.time_per_round,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    size=(3, 1),
    readonly=True,
    key='-TIME-',)

_cmb_features_per_level = sg.Combo(
    ('1', '2', '3', '4', '5'),
    difficulty_ctr.difficulty.characteristics_shown,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-CARXLEVEL-')

_cmb_rounds_per_game = sg.Combo(
    ('3', '5', '8', '10', '20'),
    difficulty_ctr.difficulty.rounds_per_game,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-QROUNDS-')

_cmb_plus_points = sg.Combo(
    ('1', '5', '10', '25', '50'),
    difficulty_ctr.difficulty.points_correct_answer,
    background_color=theme.BG_BUTTON,
    text_color=theme.BG_BASE,
    font=_font,
    readonly=True,
    size=(3, 1),
    key='-+QXANSWER-')

_cmb_sub_points = sg.Combo(
    ('-1', '-5', '-10', '-25', '-50'),
    difficulty_ctr.difficulty.points_bad_answer,
    background_color=theme.BG_BUTTON,
    font=_font,
    text_color=theme.BG_BASE,
    readonly=True,
    size=(3, 1),
    key='--QXANSWER-')

_btn_save = sg.Button(
    'Guardar Dificultad', size=(16, 1),
    key='-SAVE-DIFF-CUSTOM-',
    font=('System', theme.H3_SIZE),
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    pad=default_padding,
    mouseover_colors=theme.BG_BUTTON_HOVER,
    border_width=theme.BD_PRIMARY)


_input_nick = sg.Multiline(user_ctr.current_user.nick,
                           size=(20, 1),
                           disabled=True,
                           no_scrollbar=True,
                           background_color=theme.BG_BASE,
                           font=_font,
                           text_color=theme.TEXT_ACCENT,
                           border_width=theme.BD_PRIMARY,
                           enable_events=True
                           )

_input_age = sg.Input(default_text=user_ctr.current_user.age,
                      size=(20, 1),
                      background_color=theme.BG_BASE,
                      font=_font,
                      text_color=theme.TEXT_ACCENT,
                      border_width=theme.BD_PRIMARY,
                      key='-AGE-',
                      enable_events=True
                      )

_input_gender = sg.Input(default_text=user_ctr.current_user.gender,
                         size=(20, 1),
                         background_color=theme.BG_BASE,
                         font=_font,
                         text_color=theme.TEXT_ACCENT,
                         border_width=theme.BD_PRIMARY,
                         key='-GENDER-',
                         enable_events=True
                         )


_btn_edit = sg.Button(
    'Actualizar Usuario',
    key='-EDIT-USER-',
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    mouseover_colors=theme.BG_BUTTON_HOVER,
    font=_font,
    border_width=theme.BD_ACCENT
)


def header() -> list:
    return [
        csg.horizontal_spacer(_padding,
                              background_color=theme.BG_BASE),
        sg.Text('DIFICULTAD PERSONALIZADA', pad=((50, 0), (50, 0)),
                background_color=theme.BG_BASE, font=('System', theme.H3_SIZE)),
        sg.Push(background_color=theme.BG_BASE),
        sg.Text('EDITAR USUARIO', pad=((50, 0), (50, 0)),
                background_color=theme.BG_BASE, font=('System', theme.H3_SIZE)),
        csg.horizontal_spacer(_padding,
                              background_color=theme.BG_BASE)
    ]


def textv_spacer() -> list:
    return [csg.vertical_spacer(theme.height//64, background_color=theme.BG_BASE)]


def texth_spacer() -> list:
    return csg.horizontal_spacer(theme.width//6, background_color=theme.BG_BASE)


def text_input(text: str) -> sg.Text:
    return sg.Text(text,
                   size=(6, 1),
                   background_color=theme.BG_BASE,
                   font=_font,
                   pad=theme.scale(25)
                   )


def menu_options() -> list[list]:
    config_layout = [
        header(),
        [csg.vertical_spacer(
            theme.height//16, background_color=theme.BG_BASE)],

        [*build_text('Tiempo de partida', 'Segundos:',
                     _cmb_time_per_game),
         texth_spacer(),
         text_input('Nick'),
         _input_nick],
        textv_spacer(),

        [*build_text('Características por nivel',
                     'Cantidad:  ', _cmb_features_per_level,),
         texth_spacer(),
         text_input('Edad'),
         _input_age],
        textv_spacer(),

        [*build_text('Rounds por juego', 'Cantidad:  ',
                     _cmb_rounds_per_game),
         texth_spacer(),
         text_input('Género'),
         _input_gender],
        textv_spacer(),

        [csg.vertical_spacer(theme.scale(12), background_color=theme.BG_BASE)],
        [*build_text('Puntos añadidos ', 'Cantidad:  ',
                     _cmb_plus_points),
         texth_spacer(),
         csg.horizontal_spacer(theme.scale(
             100), background_color=theme.BG_BASE),
         _btn_edit,
         csg.horizontal_spacer(theme.scale(80), background_color=theme.BG_BASE)],
        textv_spacer(),

        [csg.vertical_spacer(theme.scale(12), background_color=theme.BG_BASE)],
        build_text('Puntos restados', 'Cantidad:  ', _cmb_sub_points),
        textv_spacer(),

        [csg.vertical_spacer(theme.scale(350), background_color=theme.BG_BASE),
            common.navigation_button('<--', screen_name='-MENU-'),
            csg.horizontal_spacer(theme.scale(
                200), background_color=theme.BG_BASE),
         _btn_save, ]
    ]

    return config_layout


def validate_age():
    age = _input_age.get()
    try:
        age = int(age)
        if age <= 0 or age > 100:
            raise ValueError
    except ValueError:
        _input_age.update(background_color='Red')
        return False
    _input_age.update(background_color=theme.BG_BASE,)
    return True


def validate_gender():
    gender = _input_gender.get()
    if gender == '':
        _input_gender.update(background_color='red')
        return False
    _input_gender.update(background_color=theme.BG_BASE,)
    return True


def validate_all() -> None:
    result = validate_gender() + validate_age()
    _btn_edit.update(disabled=result != 2)


def save_settings() -> None:
    changes = {
        'time_per_round': int(_cmb_time_per_game.get()),
        'rounds_per_game': int(_cmb_rounds_per_game.get()),
        'points_correct_answer': int(_cmb_plus_points.get()),
        'points_bad_answer':  int(_cmb_sub_points.get()),
        'characteristics_shown': int(_cmb_features_per_level.get())
    }
    difficulty_ctr.update_difficulty(**changes)


def update_user() -> None:
    user_ctr.current_user.age = _input_age.get()
    user_ctr.current_user.gender = _input_gender.get()
    pass


def refresh_inputs() -> None:
    _input_nick.update(value=user_ctr.current_user.nick)
    _input_age.update(value=user_ctr.current_user.age)
    _input_gender.update(value=user_ctr.current_user.gender)


def reset():
    refresh_inputs()
    pass


_configuration_layout = [
    [common.screen_title('Configuración', spaced=True,
                         alignment='center')],
    [sg.Column(menu_options(), background_color=theme.BG_BASE, expand_x=True)],


]

_screen_config = {
    'background_color': theme.BG_BASE,
    'element_justification': 'c'
}

observer.subscribe(
    '-AGE-',
    validate_all
)
observer.subscribe(
    '-GENDER-',
    validate_all
)
observer.subscribe(
    '-EDIT-USER-',
    update_user
)
observer.subscribe(
    '-SAVE-DIFF-CUSTOM-',
    save_settings,
)
screen = Screen(
    SCREEN_NAME,
    _configuration_layout,
    _screen_config,
    reset
)
