import os
import csv

words_to_upper = ["Edm", "Dfw", "Uk", "R&b", "Lgbtq+"]

path = os.path.dirname(os.path.realpath("."))
path_file = os.path.join(path,"grupo27", "section_dataset", "base_datasets", 'Spotify_2010-2019_Top_100.csv')
path_newfile = os.path.join(path,"grupo27", "section_dataset", "base_datasets", 'Spotify.csv')

with open(path_file,"r", encoding="utf-8") as File:  
    csv_reader = csv.reader(File, delimiter=',')
    #encabezado = next(csv_reader)
    datos = list(csv_reader)

with open(path_newfile, "w",encoding="utf-8") as NewFile:
    csv_writer = csv.writer(NewFile)
    #csv_writer.writerows(datos)
    #print(datos)
    for row in datos:
        row[2] = row[2].split()
        # A todos los datos pongo la primera letra en mayuscula
        for index, value in enumerate(row[2]):
            row[2][index] = row[2][index].replace(value[0],value[0].upper()) 
        # Paso la lista a una cadena
        
        #print(row[2][0])
        try: 
            word_to_change = words_to_upper.index(row[2][0])
            row[2][0] = words_to_upper[word_to_change].upper()

        except (ValueError , IndexError):
            pass

        row[2] = " ".join(row[2])
        #print(row[2])
        csv_writer.writerow(row)


#if ("Edm" in row[2]) :
#    row[2] = row[2].replace("Edm","EDM") 
#    csv_writer.writerow(row)
#elif ("Dfw" in row[2] ):
#    row[2] = row[2].replace("Dfw","DFW") 
#    csv_writer.writerow(row)
#elif ("Uk" in row[2]):
#    row[2] = row[2].replace("Uk","UK")
#    csv_writer.writerow(row) 
#elif ("R&b" in row[2]):
#    row[2] = row[2].replace("R&b","R&B") 
#    csv_writer.writerow(row)
#elif ("Lgbtq+" in row[2]):
#    print(row[2])
#    row[2] = row[2].replace("Lgbtq+","LGBTQ+") 
#    print(row[2])
#    csv_writer.writerow(row)
#else:
#    csv_writer.writerow(row)