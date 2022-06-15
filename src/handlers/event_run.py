# LA TABLA POSEE

# ● Marca de tiempo (timestamp)                  time.time()
# ● Número de Partida (autoincremental o UUID)   uuid.uuid4()
# ● Nombre de evento
# ● Cantidad total de objetos o personas a adivinar
# ● Usuarie - nick
# ● Estado
# ● Objeto o respuesta
# ● Nivel dificultad

import time
import uuid

START = 'inicio_partida'
INTENT = 'intento'
END = 'fin'


class RunEventController:
    added_events: list[str[str]] = [[]]

    def register_event(self,
                       name: str,
                       rounds: int,
                       user: str,
                       state: str,
                       difficulty: str,
                       user_answer: str = '-',
                       correct_answer: str = '-'
                       ):
        timestamp = int(time.time())
        uid = uuid.uuid4()
        event = [timestamp, uid, name, user, state,
                 user_answer, correct_answer, rounds, difficulty]
        self.added_events.append(event)

    def _save_events(self) -> None:
        pass

    def save(self) -> None:
        self._save_events()
