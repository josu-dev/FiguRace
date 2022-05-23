import os
import csv
# Constantes
UPPER_GENDERS = ["EDM", "DFW", "UK", "R&B", "LGBTQ+"]
ORDEN = ["Top Genre", "Artist Type", "Year Released", "Top Year", "BPM" ,"Artist"]
NAMES_REMOVE = ["Artist", "Top Genre", "Year Released","BPM", "Top Year", "Artist Type"]

cols_remove:list[int] = []     # [0, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
cols_saves:list[int] = []       #[1, 2, 3, 5, 15, 16] 

def create_order(orden_list:list[int]):
    # Columnas para invertir datos
    """Agregamos a una lista, los indices manteniendo un orden.
    """
    names_compare = list(map(lambda x: x.lower(), ORDEN))
    for name in names_compare:
        for pos,dato2 in enumerate(header):
            if (name == dato2):
                orden_list.append(pos)


def data_process(path:str):
    header:list[str] = []
    datos:list[list[str]] = []
    path_file = os.path.join(path,"grupo27", "dataset_section", "base_datasets", 'Spotify_2010-2019_Top_100.csv')
    with open(path_file,"r", encoding="utf-8") as File:  
        csv_reader = csv.reader(File, delimiter=',')
        header = next(csv_reader) # El encabezado para comparar las columnas borradas
        datos = list(csv_reader)
    return header,datos


path = os.path.dirname(os.path.realpath("."))
header,datos = data_process(path)

orden_list:list[int] = []  # [2, 16, 3, 15, 5, 1]

create_order(orden_list)

def separate_cols(cols_remove:list[int],cols_saves:list[int]):
    names_compare = list(map(lambda x: x.lower(), NAMES_REMOVE)) # Creamos una lista para comparar
    for column in header:
        if not(column.lower() in names_compare): 
            index_dato = header.index(column)
            cols_remove.append(index_dato)
        else:                                 # Para ordenar los datos entre listas
            index_dato2 = header.index(column)
            cols_saves.append(index_dato2)


cols_remove:list[int] = []  # Columnas que voy a eliminar
cols_saves:list[int] = []   # Columnas que voy a guardar
separate_cols(cols_remove,cols_saves)


cols_remove = sorted(cols_remove, reverse=True) # En reverso para sacar primero las columnas desde el final
path_newfile = os.path.join(path,"grupo27", "dataset_section", "processed_datasets", 'Spotify.processed.csv')

with open(path_newfile, "w",encoding="utf-8",newline='') as NewFile:
    csv_writer = csv.writer(NewFile)
    datos.insert(0,header) # Vuelvo a insertar el encabezado para eliminar las columnas

    def cols_sorted(datos:list[list[str]]):
        for row in datos:
            # Recorro la lista de columnas que tengo que intercambiar 
            # Despues intercambio los datos entre columnas
            for col_index in cols_saves:                # [1, 2, 3, 5, 15, 16]
                for indice,dato in enumerate(orden_list):     
                    if (col_index == dato):                     # [2, 16, 3, 15, 5, 1]
                        aux = row[dato]
                        row[dato]= row[indice]                  # En lugar de col_index,es la posicion de la tabla
                        row[indice] = aux
        return datos
    datos = cols_sorted(datos)

    #___________________________________________
    for row in datos:
        def upper_words(row:list[str]):
            genders = row[2].split()
            for index, gender in enumerate(genders):
                if gender.upper() in UPPER_GENDERS:
                    genders[index]= gender.upper()
                else:
                    genders[index]= gender.title()
            row[2] = " ".join(genders)
            return row
        row = upper_words(row)
        
        def cols_remove_function(row:list[str],cols_remove:list[int]):
            # Elimino las columnas innecesarias
            for col_index in cols_remove:
                del (row[col_index])
            return row
        row = cols_remove_function(row,cols_remove)
        #print(type(row))
        csv_writer.writerow(row)



##________________________________________________________________




