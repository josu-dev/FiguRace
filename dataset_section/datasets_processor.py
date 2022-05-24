import os
import csv
UPPER_GENDERS_SPOTIFY = ["EDM", "DFW", "UK", "R&B", "LGBTQ+"]
ORDEN_SPOTIFY = ["Top Genre", "Artist Type", "Year Released", "Top Year", "BPM" ,"Artist"]
NAMES_REMOVE__SPOTIFY = ["Top Genre", "Year Released","BPM", "Top Year", "Artist Type","Artist"]
path = os.path.dirname(os.path.realpath("."))

def data_process(path:str):
    header:list[str] = []
    datos:list[list[str]] = []
    path_file = os.path.join(path,"grupo27","dataset_section", "base_datasets", 'Spotify_2010-2019_Top_100.csv')
    with open(path_file,"r", encoding="utf-8") as File:  
        csv_reader = csv.reader(File, delimiter=',')
        header = next(csv_reader) # El encabezado para comparar las columnas borradas
        datos = list(csv_reader)
    return header,datos


header,datos = data_process(path)

print(header)

def create_order(orden_list:list[int]):
    # Columnas para invertir datos
    """Agregamos a una lista, los indices manteniendo un orden.
    """
    names_compare = list(map(lambda x: x.lower(), ORDEN_SPOTIFY))
    header_compare = list(map(lambda x: x.lower(), header))
    for name in names_compare:
        for pos,dato2 in enumerate(header_compare):
            if (name == dato2):
                orden_list.append(pos)

def separate_cols(cols_remove:list[int]):
    names_compare = list(map(lambda x: x.lower(), NAMES_REMOVE__SPOTIFY)) # Creamos una lista para comparar
    for column in header:
        if not(column.lower() in names_compare): 
            index_dato = header.index(column)
            cols_remove.append(index_dato)


cols_remove:list[int] = []  # Columnas que voy a eliminar [0, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
#cols_saves:list[int] = []   # Columnas que voy a guardar  [1, 2, 3, 5, 15, 16] 
separate_cols(cols_remove)

def cols_sorted(row:list[str],orden_list:list[int]):
    for indice in range(0,len(row)):                   # [0, 1, 2, 3, 4, 5]
        for indice2,dato in enumerate(orden_list):     # [1, 5, 2, 4, 3, 0]
            if (indice == dato):    
                #print(indice)  
                row[indice2], row[indice] = row[indice], row[indice2]
    return row
# artist, Top Genre, year released, bpm, top year, artist type  Lo que tenemos
# Top Genre, artist, year released, bpm,top year, artist type  Lo que genera
# Top Genre, top year, year released, top year, bpm, artist  # Lo que tendria que generar

def upper_words(word:str):
    genders = word.split()
    for index, gender in enumerate(genders):
        if gender.upper() in UPPER_GENDERS_SPOTIFY:
            genders[index]= gender.upper()
        else:
            genders[index]= gender.title()
    word = " ".join(genders)
    return word

def cols_remove_function(row:list[str],cols_remove:list[int]):
    # Elimino las columnas innecesarias
    for col_index in cols_remove:
        del (row[col_index])
    return row

cols_remove = sorted(cols_remove, reverse=True) # En reverso para sacar primero las columnas desde el final
path_newfile = os.path.join(path,"grupo27", "dataset_section", "processed_datasets", 'Spotify.processed.csv')
print(cols_remove)
with open(path_newfile, "w",encoding="utf-8",newline='') as NewFile:
    csv_writer = csv.writer(NewFile)
    datos.insert(0,header)                  # Vuelvo a insertar el encabezado para eliminar las columnas
    entro:bool = False
    orden_list:list[int] = []  
    for row in datos:
        row[2] = upper_words(row[2])
        row = cols_remove_function(row,cols_remove)
        if entro == False :
            create_order(orden_list)
            print(orden_list)
            entro = True
        row = cols_sorted(row,orden_list)
        csv_writer.writerow(row)
    