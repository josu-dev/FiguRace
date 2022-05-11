from typing import Any, Callable

subscribers: dict[str, list[Callable[..., Any]]] = dict()


def subscribe(event_type: str, function: Callable[..., Any]) -> None:
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(function)


def post_event(event_type: str, data: Any | None = None) -> None:
    if event_type not in subscribers:
        return
    for function in subscribers[event_type]:
        if data:
            function(data)
        else:
            function()