import os
import csv

UPPER_GENDERS = ["EDM", "DFW", "UK", "R&B", "LGBTQ+"]

path = os.path.dirname(os.path.realpath("."))
path_file = os.path.join(path,"grupo27", "dataset_section", "base_datasets", 'Spotify_2010-2019_Top_100.csv')
path_newfile = os.path.join(path,"grupo27", "dataset_section", "processed_datasets", 'Spotify.processed.csv')

with open(path_file,"r", encoding="utf-8") as File:  
    csv_reader = csv.reader(File, delimiter=',')
    datos = list(csv_reader)

with open(path_newfile, "w",encoding="utf-8",newline='') as NewFile:
    csv_writer = csv.writer(NewFile)
    for row in datos:
        genders = row[2].split()
        for index, gender in enumerate(genders):
            if gender.upper() in UPPER_GENDERS:
                genders[index]= gender.upper()
            else:
                genders[index]= gender.title()

        row[2] = " ".join(genders)
        csv_writer.writerow(row)
