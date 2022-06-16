import os
import time
import uuid
from enum import Enum
from typing import Any

from .. import constants, translations
from . import file, observer
from .user import UsersController
from .difficulty import DifficultyController


class EventNames(Enum):
    START = 'inicio_partida'
    TRY = 'intento'
    END = 'fin'


class EventStates(Enum):
    ERROR = 'error'
    OK = 'ok'
    TIME_OUT = 'timeout'
    ENDED = 'finalizada'
    CANCELED = 'cancelada'
    DEFAULT = ''


class RunEventController:
    '''Controller of the events occurred during the execution of the game.'''

    def __init__(self, path: str, user_ctr: UsersController, difficulty_ctr: DifficultyController) -> None:
        '''Initialization of the file used for save the information of the events.

        Args:
           path : Path of the file that we will be working.
           user_ctr : A user controller to access to the current user.
           difficulty_ctr : A difficulty controller to access to the current difficulty.'''
        self._file_path = os.path.join(path, 'events.csv')

        self._events = file.load_csv_safe(
            self._file_path, [self.default_header()]
        )
        self._user_ctr = user_ctr
        self._difficulty_ctr = difficulty_ctr
        self._uid = ''
        self._playing = False
        observer.subscribe(constants.RUN_EVENT, self.register_event)

    def register_event(self, event_data: dict[str, Any]) -> None:
        '''Register an event to add on the csv.

        Args:
            event_data: data of the event composed by 
                name,Q of rounds,current user,state,user answer, correct answer and difficulty'''

        if(event_data['name'] == EventNames.START):
            self._uid = uuid.uuid4().hex
            self._playing = True
        elif(event_data['name'] == EventNames.END):
            self._playing = False
        event = [
            int(time.time()),
            self._uid,
            event_data['name'].value,
            event_data['rounds'],
            self._user_ctr.current_user.nick,
            event_data.get('state', EventStates.DEFAULT).value,
            event_data.get('user_answer', EventStates.DEFAULT.value),
            event_data.get('correct_answer', EventStates.DEFAULT.value),
            translations.DIFFICULTY_TO_ES[self._difficulty_ctr.difficulty_name],
        ]
        self._events.append(event)  # type: ignore

    def default_header(self) -> list[str]:
        '''Return the header of the csv to use like default.'''
        return ['timestamp', 'id', 'evento', 'cantidad a adivinar', 'usuarie', 'estado', 'texto ingresado', 'respuesta', 'nivel']

    def save(self) -> None:
        '''Save the list obtained into a csv.
        Before saving I check if the player was playing to do the END event.'''
        if(self._playing):
            event_data = {'name': EventNames.END,
                          'rounds': self._difficulty_ctr.difficulty.rounds_per_game, 'state': EventStates.CANCELED}
            self._register_event(event_data)
        file.save_csv(self._file_path, self._events)
