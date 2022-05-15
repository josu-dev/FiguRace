import csv
from os import path
from typing import Callable


LineTransform = Callable[[list[str]], list[str]]


def transform_csv(source_path: str, result_path: str, header_fn: LineTransform, content_fn: LineTransform, source_value_delimiter: str = ',', contains_header: bool = True, remove_header: bool = False, remove_empty_lines: bool = True) -> None:
    with (
        open(source_path, mode='r', encoding='utf-8') as src_file,
        open(result_path, mode='w', encoding='utf-8') as res_file
    ):
        reader = csv.reader(src_file, delimiter=source_value_delimiter)
        writer = csv.writer(res_file, delimiter=',', lineterminator='\n')
        if contains_header:
            header = next(reader)
            if not remove_header:
                writer.writerow(header_fn(header))
        for line in reader:
            if remove_empty_lines and (line.count('') == len(line)):
                continue
            transformed_line = content_fn(line)
            writer.writerow(transformed_line)


def resample_list(index_sequence: list[int]) -> LineTransform:
    sequence = index_sequence

    def resample(original: list[str]) -> list[str]:
        return [original[index] for index in sequence]

    return resample


BASE_PATH = path.dirname(__file__)
SRC_PATH = path.join(BASE_PATH, 'base_datasets')
OUTPUT_PATH = path.join(BASE_PATH, 'processed_datasets')


# Spotify dataset

spotify_resample = resample_list([2, 16, 3, 15, 5, 1])

MUSICAL_ACRONYMS = ('EDM', 'DFW', 'UK', 'R&B', 'LGBTQ+')


def spotify_content(values: list[str]) -> list[str]:
    new_values = spotify_resample(values)
    gender = new_values[0]
    if gender.upper() in MUSICAL_ACRONYMS:
        gender = gender.upper()
    elif '-' in gender:
        gender = '-'.join([word.title() for word in gender.split()])
    else:
        gender = gender.title()
    new_values[0] = gender
    return new_values


transform_csv(
    SRC_PATH + '/Spotify_2010-2019_Top_100.csv',
    OUTPUT_PATH + '/spotify.processed.csv',
    spotify_resample,
    spotify_content
)


# Lakes dataset

lakes_resample = resample_list([1, 2, 3, 4, 5, 1])


def dms_to_dd(coord: str, n_decimals: int = 5) -> str:
    sign = -1 if 'S' in coord or 'O' in coord else 1
    degree, coord = coord[:-2].split('°')
    min, sec = coord.split('\'')
    dd = sign * (int(degree) + int(min)/60 + int(sec)/3600)
    return str(round(dd, n_decimals))


def lakes_content(values: list[str]) -> list[str]:
    new_values = lakes_resample(values)
    for pos, val in enumerate(new_values):
        if val == '':
            new_values[pos] = 'Desconocido'
    dms_coords = new_values[4]
    dd_coords = (dms_to_dd(coord) for coord in dms_coords.split())
    new_values[4] = ' '.join(dd_coords)
    return new_values


transform_csv(
    SRC_PATH + '/Lagos Argentina - Hoja 1 (1).csv',
    OUTPUT_PATH + '/lakes.processed.csv',
    lakes_resample,
    lakes_content
)


# FIFA dataset

fifa_resample = resample_list([8, 2, 3, 5, 7, 1])

POTENTIAL_TABLE = {
    90: 'Sobresaliente',
    80: 'Muy bueno',
    60: 'Bueno',
    -1: 'Regular'
}

POSITION_TABLE = {
    'ST' : 'Delantero',
    'CM' : 'Volante',
    'CDM' : 'Volante defensivo',
    'LB' : 'Lateral izquierdo',
    'GK' : 'Arquero',
    'LM' : 'Volante izquierdo',
    'RM' : 'Volante derecho',
    'CAM' : 'Volante offensivo',
    'LW' : 'Volante izquierdo ofensivo',
    'LWB' : 'Lateral izquierdo ofensivo',
    'CB' : 'Defensor central',
    'RB' : 'Lateral derecho',
    'RW' : 'Volante ofensivo derecho',
    'RWB' : 'Lateral ofensivo derecho',
    'CF' : 'Media punta'
}


def fifa_content(values: list[str]) -> list[str]:
    new_values = fifa_resample(values)
    potential = int(new_values[4])
    for value in POTENTIAL_TABLE:
        if potential >= value:
            new_values[4] = POTENTIAL_TABLE[value]
            break
    positions = new_values[2].split('|')
    translated_positions = '|'.join([POSITION_TABLE[acronym] for acronym in positions])
    new_values[2] = translated_positions
    return new_values


transform_csv(
    SRC_PATH + '/FIFA-21 Complete.csv',
    OUTPUT_PATH + '/fifa.processed.csv',
    fifa_resample,
    fifa_content,
    source_value_delimiter=';'
)
