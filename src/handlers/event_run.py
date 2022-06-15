import os
import time
import uuid
from . import file


class RunEventController:
    '''Controller of the events occurred during the execution of the game
    '''
    START = 'inicio_partida'
    INTENT = 'intento'
    END = 'fin'

    def __init__(self, path) -> None:
        '''Initialization of the file used for save the information of the events
        Args:
           path : Path of the file that we will be working
        '''
        self._file_path = os.path.join(path, 'events.csv')
        self._events: list[str[str]] = file.load_csv_safe(
            self._file_path, self.default_header())

    def register_event(self,
                       name: str,
                       rounds: int,
                       user: str,
                       state: str,
                       difficulty: str,
                       user_answer: str = '-',
                       correct_answer: str = '-'
                       ) -> None:
        '''Register an event to add on the csv
        Args:
                name: event name
                rounds : rounds of the current game
                user : current user
                state : state of the action to register
                difficulty : current difficulty
                user_answer : only if the event is an intent of answer
                correct_answer : the correct answer to the current question. Only if the event is an intent of answer
        '''
        timestamp = int(time.time())
        uid = uuid.uuid4()
        event = [timestamp, uid, name, user, state,
                 user_answer, correct_answer, rounds, difficulty]
        self._events.append(event)

    def default_header() -> list[str]:
        '''Return the header of the csv to use like default
        '''
        return ['timestamp', 'id', 'evento', 'personas a adivinar', 'usuarie', 'estado', 'texto ingresado', 'respuesta', 'nivel']

    def save(self) -> None:
        '''Save the list obtained into a csv
        '''
        file.save_csv(self._file_path, self._events)
