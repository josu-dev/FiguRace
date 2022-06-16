from dataclasses import dataclass
from random import randint

from . import file


class Dataset:
    def __init__(self, name: str, raw_dataset: list[list[str]]) -> None:
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
        sample = randint(0, len(self._content) - 1)
        return self._content[sample]

    def _random_unique(self) -> list[str]:
        while True:
            sample = randint(0, len(self._content) - 1)
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

    def reset(self) -> None:
        self._used = set()


@dataclass
class Card:
    hints: list[str]
    correct_answer: str
    bad_anwers: list[str]


class CardController:
    def __init__(self, datasets_folder_path: str) -> None:
        self._datasets = {
            file_name.split('.')[0]: path
            for file_name, path in file.scan_dir(datasets_folder_path, file_extension='csv')
        }
        if len(self._datasets) == 0:
            raise Exception(
                f'Must exist at least 1 dataset with csv format at \'{datasets_folder_path}\' to start the game'
            )

        default = list(self._datasets.keys())[0]
        self._load_dataset(default)

    def _load_dataset(self, name: str) -> None:
        raw_dataset = file.load_csv(self._datasets[name])
        self._dataset = Dataset(name, raw_dataset)

    def reset(self) -> None:
        self._dataset.reset()

    @property
    def types_list(self) -> list[str]:
        return [key for key in self._datasets]

    @property
    def type(self) -> str:
        return self._dataset.name

    @type.setter
    def type(self, type: str) -> None:
        self._load_dataset(type)

    @property
    def characteristics(self) -> list[str]:
        return self._dataset.header

    @property
    def new_card(self) -> Card:
        correct, *bads = self._dataset.random_sample(5, unique=1)
        return Card(
            correct[:-1], correct[-1], [bad[-1] for bad in bads]
        )
