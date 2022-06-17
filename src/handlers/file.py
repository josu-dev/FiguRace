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
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def ensure_file_dirs(path: str) -> None:
    parent_path = os.path.dirname(path)
    if not os.path.exists(parent_path):
        os.makedirs(parent_path, exist_ok=True)


def load_json(path: str, default_value: Any, encoding_format: str = 'utf-8') -> JSON:
    if not os.path.exists(path):
        save_json(path, default_value)

    with open(path, mode='r', encoding=encoding_format) as file:
        return json.load(file)


def save_json(path: str, value: Any, is_custom_class: bool = False, encoding_format: str = 'utf-8') -> None:
    ensure_file_dirs(path)

    with open(path, mode='w', encoding=encoding_format) as file:
        if is_custom_class:
            json.dump(value, file, default=lambda o: o.__dict__, indent=4)
        else:
            json.dump(value, file, indent=4)


def load_csv(path: str, encoding_format: str = 'utf-8') -> CSV:
    if not os.path.exists(path):
        raise Exception(f'No exists a csv file at: {path}')

    with open(path, mode='r', encoding=encoding_format) as file:
        csv_reader = csv.reader(file, delimiter=',')
        return list(csv_reader)


def load_csv_safe(path: str, default_value: CSV, encoding_format: str = 'utf-8') -> CSV:
    if not os.path.exists(path):
        save_csv(path, default_value)

    with open(path, mode='r', encoding=encoding_format) as file:
        csv_reader = csv.reader(file, delimiter=',')
        return list(csv_reader)


def save_csv(path: str, value: CSV, encoding_format: str = 'utf-8') -> None:
    ensure_file_dirs(path)

    with open(path, mode='w', encoding=encoding_format) as file:
        csv_writer = csv.writer(file, delimiter=',', lineterminator='\n')
        csv_writer.writerows(value)


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
