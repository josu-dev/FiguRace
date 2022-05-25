import os


PATH_SRC = os.path.dirname(__file__)
PATH_JSON = os.path.join(PATH_SRC, 'database', 'json')
PATH_SETTINGS = os.path.join(PATH_JSON, 'app.json')
PATH_DIFFICULTIES = os.path.join(PATH_JSON, 'difficulties.json')
PATH_THEME = os.path.join(PATH_JSON, 'theme.json')
PATH_USERS = os.path.join(PATH_JSON, 'users.json')

PATH_CSV = os.path.join(PATH_SRC, 'database', 'csv')
PATHS_DATASETS = {
    'spotify': os.path.join(PATH_CSV, 'spotify.csv'),
    'lakes': os.path.join(PATH_CSV, 'lakes.csv'),
    'fifa': os.path.join(PATH_CSV, 'fifa.csv'),
}


GOTO_VIEW = '-GOTO-VIEW-'
LAST_SCREEN = '-LAST-SCREEN-'
EXIT_APLICATION = '-EXIT-APP-'
USER_CHANGE = '-USER-CHANGE-'


DIFFICULTY_TO_ES = {
    'easy': 'Fácil',
    'normal': 'Intermedio',
    'hard': 'Difícil',
    'insane': 'Insano',
    'custom': 'Personalizada',
}
DIFFICULTY_TO_EN = {
    'Fácil': 'easy',
    'Intermedio': 'normal',
    'Difícil': 'hard',
    'Insano': 'insane',
    'Personalizada': 'custom',
}
DATASET_TO_ES = {
    'fifa' : 'FIFA 21',
    'spotify' : 'Spotify',
    'lakes' : 'Lagos Argentina'
}
DATASET_TO_EN = {
    'FIFA 21': 'fifa',
    'Spotify': 'spotify',
    'Lagos Argentina': 'lakes'
}
