import csv
import json
import os

from typing import Any


JSON = Any


def load_json(path: str, encoding_format: str = 'utf-8') -> JSON:
    if not os.path.exists(path):
        raise Exception(f'No exist a file in: {path}')

    with open(path, mode='r', encoding=encoding_format) as file:
        return json.load(file)


def save_json(path: str, value: object, is_custom_class: bool = False, write_mode: str = 'w', encoding_format: str = 'utf-8') -> None:
    with open(path, mode=write_mode, encoding=encoding_format) as file:
        if is_custom_class:
            json.dump(value, file, default=lambda o: o.__dict__, indent=4)
        else:
            json.dump(value, file)


def load_csv(path: str, char_delimiter: str = ',', encoding_format: str = 'utf-8') -> list[list[str]]:
    if not os.path.exists(path):
        raise Exception(f'No exist a file in: {path}')

    with open(path, mode='r', encoding=encoding_format) as file:
        csv_reader = csv.reader(file, delimiter=char_delimiter)
        return list(csv_reader)
