import csv
import os
import pandas as pd


SAVES_SPOTIFY_LAGOS_FIFA = [["Top Genre", "Year Released","BPM", "Top Year", "Artist Type","Artist"],["Ubicación", "Superficie (km²)", "Profundidad máxima (m)", "Profundidad media (m)", "Coordenadas"],["Age", "Nationality", "Position", "Team" , "Potential","Name"]]


for save in SAVES_SPOTIFY_LAGOS_FIFA:
    saves_lower = (list(map(lambda x: x.lower(), save))) 


path_base = os.path.join(os.getcwd(),"base_datasets", "Spotify_2010-2019_Top_100.csv")


data_set = pd.read_csv(path_base, encoding='utf-8')

df = pd. read_csv (path_base, usecols = saves_spotify)

path_base2 = os.path.join(os.getcwd(),"processed_datasets", 'datos.csv')

df.to_csv(path_base2, mode='a')





# Mmmm.... Algo anda mal..
# Son distintos



# En formato csv


#sep = ';'

#print(data_set)