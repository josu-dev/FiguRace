import os


PATH_SRC = os.path.dirname(__file__)
PATH_JSON = os.path.join(PATH_SRC,'database', 'json')
PATH_SETTINGS = os.path.join(PATH_JSON,'app.json')
PATH_DIFFICULTIES = os.path.join(PATH_JSON,'difficulties.json')
PATH_THEME = os.path.join(PATH_JSON,'theme.json')
PATH_USERS = os.path.join(PATH_JSON,'users.json')

PATH_CSV = os.path.join(PATH_SRC,'database', 'csv')
PATHS_DATASETS = {
    'spotify' : os.path.join(PATH_CSV,'spotify.csv'),
    'lakes' : os.path.join(PATH_CSV,'lakes.csv'),
    'fifa' : os.path.join(PATH_CSV,'fifa.csv'),
}

GOTO_VIEW = '-GOTO-VIEW-'
EXIT_APLICATION = '-EXIT-APP-'
