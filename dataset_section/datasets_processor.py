import os
import csv


UPPER_GENDERS = ["EDM", "DFW", "UK", "R&B", "LGBTQ+"]
names_to_remove = ["Artist", "Top Genre", "Year Released","BPM", "Top Year", "Artist Type"]
cols_to_remove:list[int] = [] #list[int] # Voy a guardar los indices a eliminar :D
columnas_guardadas:list[int] = [] #list[int] # Voy a guardar los indices a eliminar :D


ORDEN = ["Top Genre", "Artist Type", "Year Released", "Top Year", "BPM" ,"Artist"]

path = os.path.dirname(os.path.realpath("."))
path_file = os.path.join(path,"grupo27", "dataset_section", "base_datasets", 'Spotify_2010-2019_Top_100.csv')
path_newfile = os.path.join(path,"grupo27", "dataset_section", "processed_datasets", 'Spotify.processed.csv')

with open(path_file,"r", encoding="utf-8") as File:  
    csv_reader = csv.reader(File, delimiter=',')
    header = next(csv_reader) # El encabezado para comparar las columnas borradas
    datos = list(csv_reader)


ORDEN_LIST:list[int] = [] 
cont = 0


# Columnas para invertir datos
columnas2 = list(map(lambda x: x.lower(), names_to_remove)) # Creamos una lista para comparar
columnas3 = list(map(lambda x: x.lower(), ORDEN))

for dato1 in columnas3:
    pos = 0
    for dato2 in header:
        if (dato1 == dato2):
            ORDEN_LIST.append(pos)
        pos = pos + 1
#________________________________________
    
print(ORDEN_LIST)

for column in header:
    if not(column.lower() in columnas2): # Columnas que quiero eliminar
        index_dato = header.index(column)
        cols_to_remove.append(index_dato)
    else:                                 # Para ordenar los datos entre listas
        index_dato2 = header.index(column)
        columnas_guardadas.append(index_dato2)
print(cols_to_remove)
print(columnas_guardadas)
cols_to_remove = sorted(cols_to_remove, reverse=True) # En reverso para sacar primero las columnas desde el final

#print(header)




with open(path_newfile, "w",encoding="utf-8",newline='') as NewFile:
    csv_writer = csv.writer(NewFile)
    #csv_writer.writerow(header) # Agrego el encabezado ya que termine de usarlo
    datos.insert(0,header) #Vuelvo a insertar el encabezado para eliminar las columnas
    #___________________________________________
    for row in datos:
        genders = row[2].split()
        for index, gender in enumerate(genders):
            if gender.upper() in UPPER_GENDERS:
                genders[index]= gender.upper()
            else:
                genders[index]= gender.title()
        #_______________________________________
        row[2] = " ".join(genders)
        
        # Elimino las columnas innecesarias
        for col_index in cols_to_remove:
            del (row[col_index])
        #print(type(row))
        
        for col_index in columnas_guardadas:
            for dato in ORDEN_LIST:
                if (row[col_index] == row[dato]):
                    aux = row[dato]
                    row[dato]= row[col_index]
                    row[col_index] = aux
        print()

        

        csv_writer.writerow(row)
