from os import path

SRC_PATH = path.join(path.dirname(__file__),'..','')
DATABASE_PATH = path.dirname(__file__)
DATA_PATH = path.join(DATABASE_PATH,'data')
DEFAULT_SETTINGS = path.join(path.dirname(__file__),'..','settings.json')

print(SRC_PATH, DATABASE_PATH, DEFAULT_SETTINGS)