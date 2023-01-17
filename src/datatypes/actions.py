from abc import ABC
from abc import ABCMeta
from abc import abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.datatypes.entity import Entity
    from src.engine import Engine


class Action(ABC):
    @abstractmethod
    def perform(self, engine: "Engine", entity: "Entity"):
        raise NotImplementedError()


@dataclass
class ActionWithDirection(Action, metaclass=ABCMeta):
    dx: int
    dy: int

    def perform(self, engine: "Engine", entity: "Entity"):
        raise NotImplementedError()


@dataclass
class MovementAction(ActionWithDirection):
    def perform(self, engine: "Engine", entity: "Entity"):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds.
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile.
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return  # Destination is blocked by an entity.

        entity.move(self.dx, self.dy)


@dataclass
class MeleeAction(ActionWithDirection):
    def perform(self, engine: "Engine", entity: "Entity") -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if not target:
            return  # No entity to attack.

        print(f"You kick the {target.name}, much to its annoyance!")


@dataclass
class BumpAction(ActionWithDirection):
    def perform(self, engine: "Engine", entity: "Entity") -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return MeleeAction(self.dx, self.dy).perform(engine, entity)
        else:
            return MovementAction(self.dx, self.dy).perform(engine, entity)


@dataclass
class EscapeAction(Action):
    def perform(self, engine: "Engine", entity: "Entity"):
        raise SystemExit()
