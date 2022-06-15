import os
import pandas as pd

POTENTIAL_TABLE_FIFA = {
    90: 'Sobresaliente',
    80: 'Muy bueno',
    60: 'Bueno',
    -1: 'Regular'
}

POSITION_TABLE_FIFA = {
    'ST': 'Delantero',
    'CM': 'Volante',
    'CDM': 'Medio centro defensivo',
    'LB': 'Lateral izquierdo',
    'GK': 'Portero',
    'LM': 'Volante izquierdo',
    'RM': 'Volante derecho',
    'CAM': 'Volante ofensivo',
    'LW': 'Extremo izquierdo',
    'LWB': 'Lateral izquierdo ofensivo',
    'CB': 'Defensor central',
    'RB': 'Lateral derecho',
    'RW': 'Extremo derecho',
    'RWB': 'Lateral ofensivo derecho',
    'CF': 'Media punta'
}

UPPER_GENDERS_SPOTIFY = ["EDM", "DFW", "UK", "R&B", "LGBTQ+"]

def potential_replace(potential:str):
    compare_potential = int(potential)
    for potential_player in POTENTIAL_TABLE_FIFA:
        if compare_potential >= potential_player:
            potential = POTENTIAL_TABLE_FIFA[potential_player]
            break
    return potential

def position_replace(position:str):
    positions = position.split('|')
    position = '|'.join([POSITION_TABLE_FIFA[acronym] for acronym in positions])
    return position

def upper_words(sentence:str):
    """Procesa una frase dependiendo de la consigna"""
    genders = sentence.split()
    for index,gender in enumerate(genders):
        genders[index] = ( gender.upper() if gender.upper() in UPPER_GENDERS_SPOTIFY else gender.title())
    sentence = " ".join(genders)
    return sentence

def rebase_coord(coord: str, n_decimals: int = 5) -> str:
    sign = -1 if 'S' in coord or 'O' in coord else 1
    degree, coord = coord[:-2].split('°')
    min, sec = coord.split('\'')
    dd = sign * (int(degree) + int(min)/60 + int(sec)/3600)
    return str(round(dd, n_decimals)) + '°'

def transform_coords(coords:str) -> str:
    latitude, longitude = coords.split()
    coords = rebase_coord(latitude) + ' ' + rebase_coord(longitude)
    return coords



DATASETS = {                  
    'FIFA-21_Complete.csv':{
        'order': ["team", "nationality", "position", "age", "potential" ,"name"],
        'translation': ['Equipo', 'Nacionalidad', 'Posición', 'Edad', 'Potencial', 'Nombre'
    ],
        'functions': {
            "potential": potential_replace,
            "position": position_replace
            } ,
        'name':"fifa.csv"     
    },
    'Lagos_Argentina - Hoja_1.csv':{
        'order': ["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas"],
        'functions': {
            "Coordenadas": transform_coords
            },  
        "name":'lakes.csv'  
    },
    'Spotify_2010-2019_Top_100.csv':{
        'order': ["top genre", "artist type", "year released", "top year", "bpm" ,"artist"],
        'translation': ['Top genero', 'Tipo artista', 'Año lanzamiento','Mejor año', 'BPM', 'Artista'],
        'functions': {
            "top genre":upper_words
            },
        'name':'spotify.csv'       
    }
}

PATH_BASE = os.path.dirname(os.path.dirname(__file__))
PATH_SOURCE = os.path.join(PATH_BASE,"base_datasets")
PATH_PROSSED = os.path.join(PATH_BASE,"processed_datasets")

def process_dataset(file_name:str):
    if file_name not in DATASETS:
        return
    file_path = os.path.join(PATH_SOURCE,file_name)
    config = DATASETS[file_name]
    processed_path = os.path.join(PATH_PROSSED,config['name'])
    
    with open(file_path, mode = 'r',encoding="UTF-8") as file :
        df = pd. read_csv (file, sep = None,engine="python",usecols = (config['order']))
        df.dropna(how="all" ,inplace=True)
        df = df[config['order']] 
        for columna,function in config['functions'].items():  
            df[columna] = df[columna].apply(function) 
        if 'translation' in config:
            df.rename(
                {   
                    column_name:translation_name
                    for column_name,translation_name in zip(config['order'],config['translation'])
                },
                inplace=True,
                axis= 1
            )                  
        df.to_csv(processed_path, mode='w',index=False)            
    
names_files = os.listdir(PATH_SOURCE)
for file_name in names_files: 
    process_dataset(file_name)