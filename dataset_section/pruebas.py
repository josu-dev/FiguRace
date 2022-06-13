import os
import csv
import os
import pandas as pd

SAVES_COLS = {
'FIFA-21_Complete.csv':         ["Top Genre", "Year Released","BPM", "Top Year", "Artist Type","Artist"], 
'Lagos_Argentina - Hoja_1.csv': ["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas"],
'Spotify_2010-2019_Top_100.csv':["Age", "Nationality", "Position", "Team" , "Potential","Name"],
}

ORDER_COLS = {
'FIFA-21_Complete.csv':         ["Top Genre", "Artist Type", "Year Released", "Top Year", "BPM" ,"Artist"], 
'Lagos_Argentina - Hoja_1.csv': ["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas"],
'Spotify_2010-2019_Top_100.csv':["Team", "Nationality", "Position", "Age", "Potential" ,"Name"],
}
PATH_BASE = os.path.join(os.getcwd(),"base_datasets")
PATH_PROSSED = os.path.join(os.getcwd(),"processed_datasets")

def processed(name_file:str):
    path = os.path.join(name_file)
    
    if name_file in SAVES_COLS:
        print(SAVES_COLS[name_file])

names_files = os.listdir(PATH_BASE)
list(map(processed, names_files))
