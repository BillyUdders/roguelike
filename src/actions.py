from dataclasses import dataclass


class Action:
    pass


class EscapeAction(Action):
    pass


@dataclass
class MovementAction(Action):
    dx: int
    dy: int
