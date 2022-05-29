import PySimpleGUI as sg

from src import csg, common
from src.controllers import theme, users_controller as users_ctr
from src.handlers import observer
from src.handlers.screen import Screen


SCREEN_NAME = '-CREATE-USER-'
LOAD_USER_FIELD = '-LOAD-USER-FIELD-'
EVENT_ADD_PROFILE = '-ADD-PROFILE-'
FIELD_TYPE_LIST = ['nick', 'age', 'gender']


def create_input(key: str) -> sg.Input:
    return sg.Input(
        size=(20, 1),
        background_color=theme.BG_BASE,
        font=(theme.FONT_FAMILY, theme.H3_SIZE),
        text_color=theme.TEXT_ACCENT,
        border_width=theme.BD_SECONDARY,
        key=f'{LOAD_USER_FIELD} {key}',
        enable_events=True
    )


inputs: dict[str, list[sg.Input | bool]] = {}

for type in FIELD_TYPE_LIST:
    inputs[type] = [create_input(type), False]

create_button = sg.Button(
    'Crear',
    button_color=(theme.TEXT_BUTTON, theme.BG_BUTTON),
    mouseover_colors=theme.BG_BUTTON_HOVER,
    font=(theme.FONT_FAMILY, theme.H4_SIZE),
    pad=theme.scale(32),
    disabled=True,
    key=EVENT_ADD_PROFILE,
    border_width=theme.BD_ACCENT
)


def create_formulary() -> sg.Column:
    layout = [
        [
            sg.Text(
                'Nick',
                size=(6, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H3_SIZE),
                pad=theme.scale(25)
            ),
            inputs['nick'][0]
        ],
        [
            sg.Text(
                'Edad',
                size=(6, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H3_SIZE),
                pad=theme.scale(25)
            ),
            inputs['age'][0]
        ],
        [
            sg.Text(
                'Género', size=(6, 1),
                background_color=theme.BG_BASE,
                font=(theme.FONT_FAMILY, theme.H3_SIZE),
                pad=theme.scale(25)
            ),
            inputs['gender'][0]
        ],
        [
            sg.Push(theme.BG_BASE),
            create_button,
            sg.Push(theme.BG_BASE)
        ]
    ]

    return csg.CenteredLayout(
        layout,
        background_color=theme.BG_BASE
    )


def reset_formulary() -> None:
    for value in inputs.values():
        value[0].update('')
        value[1] = False
    create_button.update(disabled=True)


def validate_nick():
    nick = inputs['nick'][0].get()
    if nick == '' or nick in users_ctr.users_transform(lambda user: user.nick):
        inputs['nick'][0].update(background_color='red')
        return False
    inputs['nick'][0].update(background_color=theme.BG_BASE)
    return True


def validate_age():
    age = inputs['age'][0].get()
    try:
        age = int(age)
        if age <= 0 or age > 100:
            raise ValueError
    except ValueError:
        inputs['age'][0].update(background_color='Red')
        return False
    inputs['age'][0].update(background_color=theme.BG_BASE)
    return True


def validate_gender():
    gender = inputs['gender'][0].get()
    if gender == '' or len(gender) < 4:
        inputs['gender'][0].update(background_color='red')
        return False
    inputs['gender'][0].update(background_color=theme.BG_BASE)
    return True


def validate_inputs(key: str):
    if key == 'nick':
        inputs['nick'][1] = validate_nick()
    elif key == 'age':
        inputs['age'][1] = validate_age()
    elif key == 'gender':
        inputs['gender'][1] = validate_gender()

    for _, valid in inputs.values():
        print(valid)
        if not valid:
            break
    else:
        create_button.update(disabled=False)


observer.subscribe(LOAD_USER_FIELD, validate_inputs)


def create_user():
    users_ctr.add(
        inputs['nick'][0].get(),
        int(inputs['age'][0].get()),
        inputs['gender'][0].get()
    )
    reset_formulary()


observer.subscribe(EVENT_ADD_PROFILE, create_user)


screen_layout = [
    [common.screen_title('crear usuario', True)],
    [create_formulary()],
    [common.goback_button('Menu Selección', padding=(theme.scale(64),)*2)],
]


def reset() -> None:
    reset_formulary()


screen_config = {
    'background_color': theme.BG_BASE,
}

screen = Screen(
    SCREEN_NAME,
    screen_layout,
    screen_config,
    reset
)
