import csv
import os
import pandas as pd

SAVES_COLS = {                  
'FIFA-21_Complete.csv':         ["age", "nationality", "position", "team" , "potential","name"], 
'Lagos_Argentina - Hoja_1.csv': ["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas"],
'Spotify_2010-2019_Top_100.csv':["top genre", "year released","bpm", "top year", "artist type","artist"]
}

ORDER_COLS = {
'FIFA-21_Complete.csv':         ["team", "nationality", "position", "age", "potential" ,"name"], 
'Lagos_Argentina - Hoja_1.csv': ["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas"],
'Spotify_2010-2019_Top_100.csv':["top genre", "artist type", "year released", "top year", "bpm" ,"artist"]
}


PATH_BASE = os.path.join(os.getcwd(),"base_datasets")
PATH_PROSSED = os.path.join(os.getcwd(),"processed_datasets")

def processed(name_file:str):
    path_base = os.path.join(PATH_BASE,name_file)
    print(path_base)
    path_prossed = os.path.join(PATH_PROSSED,name_file)
    if name_file in SAVES_COLS:
        df = pd. read_csv (path_base, sep = r';|,', engine='python',usecols = (SAVES_COLS[name_file]),)
        df = df[ORDER_COLS[name_file]]
        
    df.to_csv(path_prossed, mode='a',index=False)

names_files = os.listdir(PATH_BASE)
list(map(processed, names_files))




















#SAVES_COLS_LOWER = {
#    key: [item.lower() for item in values] for key,values in SAVES_COLS.items()
#}