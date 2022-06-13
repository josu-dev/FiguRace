import csv
import os
import pandas as pd
import pandas as to_csv

SAVES_SPOTIFY = ["Top Genre", "Year Released","BPM", "Top Year", "Artist Type","Artist"]


path = os.path.join(os.getcwd(),"base_datasets", "Spotify_2010-2019_Top_100.csv")
data_set = pd.read_csv(path, encoding='utf-8')
names_compare = (list(map(lambda x: x.lower(), SAVES_SPOTIFY))) 
df = pd. read_csv (path, usecols = names_compare)

df.to_csv('datos.csv', mode='a')

print(df)



# En formato csv


#sep = ';'

#print(data_set)