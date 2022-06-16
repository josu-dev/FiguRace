from typing import Any, Callable


_subscribers: dict[str, list[Callable[..., None]]] = dict()


def subscribe(event_type: str, response_fn: Callable[..., None]) -> None:
    if event_type not in _subscribers:
        _subscribers[event_type] = []

    _subscribers[event_type].append(response_fn)


def unsubscribe(event_type: str, response_fn: Callable[..., None]) -> None:
    if event_type not in _subscribers:
        return

    _subscribers[event_type].remove(response_fn)


def post_event(event_type: str, data: Any = None) -> None:
    if event_type not in _subscribers:
        return

    for response_fn in _subscribers[event_type]:
        if data:
            response_fn(data)
        else:
            response_fn()


def remove_event(event_type: str) -> None:
    if event_type not in _subscribers:
        return

    _subscribers.pop(event_type)
