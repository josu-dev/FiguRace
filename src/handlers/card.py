from dataclasses import dataclass
from random import randint
from typing import Any, Callable

from src import file
from src.constants import PATHS_DATASETS


class Dataset:
    def __init__(self, name: str, raw_dataset: list[list[str]]):
        self._name = name
        self._header = raw_dataset[0]
        self._content = raw_dataset[1:]
        self._used: set[int] = set()

    @property
    def name(self) -> str:
        return self._name

    @property
    def header(self) -> list[str]:
        return self._header

    def _random(self) -> list[str]:
        sample = randint(0, len(self._content))
        return self._content[sample]

    def _random_unique(self) -> list[str]:
        while True:
            sample = randint(0, len(self._content))
            if sample not in self._used:
                self._used.add(sample)
                break
        return self._content[sample]

    def random_sample(self, size: int, unique: int = 0) -> list[list[str]]:
        samples: list[list[str]] = []
        for _ in range(size):
            if unique > 0:
                samples.append(self._random_unique())
                unique -= 1
            else:
                sample = self._random()
                while sample in samples:
                    sample = self._random()
                samples.append(sample)
        return samples

    # This probably is unnecesary
    def apply(self, fn: Callable[[list[str]], Any]) -> list[Any]:
        result_list: list[Any] = []
        for line in self._content:
            result = fn(line)
            if result:
                result_list.append(result)
        return result_list

    def reset(self) -> None:
        self._used = set()


@dataclass
class Card:
    hints: list[str]
    correct_answer: str
    bad_anwers: list[str]


class CardController:
    def __init__(self):
        self._datasets = PATHS_DATASETS
        self._dataset = Dataset('default',[[''],['']])
        self._answers: list[str]

    def _load_dataset(self, name: str) -> None:
        print(name)
        raw_dataset = file.load_csv(PATHS_DATASETS[name])
        self._dataset = Dataset(name, raw_dataset)
        # This probably is unnecesary
        self._answers = self._dataset.apply(lambda line: line[-1])

    def reset(self) -> None:
        if getattr(self, '_dataset', None) is None:
            return
        self._dataset.reset()

    @property
    def types(self) -> list[str]:
        return [key for key in self._datasets]

    def set_type(self, type: str) -> None:
        self._load_dataset(type)
    
    @property
    def current_type(self) -> str:
        return self._dataset.name

    @property
    def characteristics(self) -> list[str]:
        return self._dataset.header

    @property
    def new_card(self) -> Card:
        correct, *bads = self._dataset.random_sample(5, unique=1)
        return Card(
            correct[:-1], correct[-1], [bad[-1] for bad in bads]
        )
