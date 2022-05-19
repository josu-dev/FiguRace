import os


PATH_SRC = os.path.dirname(__file__)
PATH_JSON = os.path.join(PATH_SRC,'database', 'json')
PATH_SETTINGS = os.path.join(PATH_JSON,'app.json')
PATH_DIFFICULTIES = os.path.join(PATH_JSON,'difficulties.json')
PATH_THEME = os.path.join(PATH_JSON,'theme.json')


GOTO_VIEW = '-GOTO-VIEW-'
EXIT_APLICATION = '-EXIT-APP-'