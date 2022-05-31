from typing import Any, Callable


subscribers: dict[str, list[Callable[..., None]]] = dict()


def subscribe(event_type: str, function: Callable[..., None]) -> None:
    if event_type not in subscribers:
        subscribers[event_type] = []

    subscribers[event_type].append(function)


def unsubscribe(event_type: str, function: Callable[..., None]) -> None:
    if event_type not in subscribers:
        return

    subscribers[event_type].remove(function)


def post_event(event_type: str, data: Any = None) -> None:
    if event_type not in subscribers:
        return

    for function in subscribers[event_type]:
        if data:
            function(data)
        else:
            function()


def remove_event(event_type: str) -> None:
    if event_type not in subscribers:
        return

    subscribers.pop(event_type)
