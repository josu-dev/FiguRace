import os
import time
import uuid
from enum import Enum

from . import file
from src import translations


class EventNames(Enum):
    START = 'inicio_partida'
    INTENT = 'intento'
    END = 'fin'


class EventStates(Enum):
    ERROR = 'error'
    OK = 'ok'
    TIME_OUT = 'timeout'
    ENDED = 'finalizada'
    CANCELED = 'cancelada'
    DEFAULT = '-'


class RunEventController:
    '''Controller of the events occurred during the execution of the game.'''
    STATES = EventStates
    NAMES = EventNames

    def __init__(self, path: str) -> None:
        '''Initialization of the file used for save the information of the events.

        Args:
           path : Path of the file that we will be working.'''
        self._file_path = os.path.join(path, 'events.csv')
        self._events = file.load_csv_safe(
            self._file_path, [self.default_header()]
        )

    def register_event(
        self,
        name: EventNames,
        rounds: int,
        user: str,
        difficulty: str,
        state: EventStates = EventStates.DEFAULT,
        user_answer: str = '-',
        correct_answer: str = '-'
    ) -> None:
        '''Register an event to add on the csv
        Args:
                name: event name
                rounds : rounds of the current game
                user : current user
                difficulty : current difficulty
                state : state of the action to register
                user_answer : only if the event is an intent of answer
                correct_answer : the correct answer to the current question. Only if the event is an intent of answer'''
        timestamp = int(time.time())
        uid = uuid.uuid4().hex
        difficulty = translations.DIFFICULTY_TO_ES[difficulty]
        event = [
            timestamp, uid, name.value, rounds, user, state.value,
            user_answer, correct_answer,  difficulty
        ]
        self._events.append(event)  # type: ignore

    def default_header(self) -> list[str]:
        '''Return the header of the csv to use like default.'''
        return ['timestamp', 'id', 'evento', 'cantidad a adivinar', 'usuarie', 'estado', 'texto ingresado', 'respuesta', 'nivel']

    def save(self) -> None:
        '''Save the list obtained into a csv.'''
        file.save_csv(self._file_path, self._events)
