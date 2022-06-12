'''Contains helper functions to work with files.'''
import csv
import json
import os

from typing import Any


JSON = Any
CSV = list[list[str]]
FileName = str
Path = str


def ensure_dirs(path: str) -> None:
    parent_path = os.path.dirname(path)
    if not os.path.exists(parent_path):
        os.makedirs(parent_path, exist_ok=True)


def load_json(path: str, default_value: Any, encoding_format: str = 'utf-8') -> JSON:
    ensure_dirs(path)

    if not os.path.exists(path):
        save_json(path, default_value)

    with open(path, mode='r', encoding=encoding_format) as file:
        return json.load(file)


def save_json(path: str, value: Any, is_custom_class: bool = False, write_mode: str = 'w', encoding_format: str = 'utf-8') -> None:
    ensure_dirs(path)

    with open(path, mode=write_mode, encoding=encoding_format) as file:
        if is_custom_class:
            json.dump(value, file, default=lambda o: o.__dict__, indent=4)
        else:
            json.dump(value, file, indent=4)


def load_csv(path: str, delimiter_char: str = ',', encoding_format: str = 'utf-8') -> CSV:
    ensure_dirs(path)

    if not os.path.exists(path):
        raise Exception(f'No exist a csv file at: {path}')

    with open(path, mode='r', encoding=encoding_format) as file:
        csv_reader = csv.reader(file, delimiter=delimiter_char)
        return list(csv_reader)


def scan_dir(path: str, file_extension: str | None = None) -> list[tuple[FileName, Path]]:
    if not os.path.exists(path):
        return []

    if file_extension is None:
        results = [(entry.name, entry.path) for entry in os.scandir(path)]
    else:
        results = [
            (entry.name, entry.path)
            for entry in os.scandir(path) if entry.is_file() and entry.name.endswith(file_extension)
        ]
    return results
