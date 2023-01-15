from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.types.entity import Entity
    from src.engine import Engine


class Action(ABC):
    @abstractmethod
    def perform(self, engine: "Engine", entity: "Entity"):
        raise NotImplementedError()


@dataclass
class EscapeAction(Action):
    def perform(self, engine: "Engine", entity: "Entity"):
        raise SystemExit()


@dataclass
class MovementAction(Action):
    dx: int
    dy: int

    def perform(self, engine: "Engine", entity: "Entity"):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds.
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile.

        entity.move(self.dx, self.dy)
