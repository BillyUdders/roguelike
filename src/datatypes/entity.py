import copy
from typing import TYPE_CHECKING
from typing import TypeVar

if TYPE_CHECKING:
    from src.map import Map

from dataclasses import dataclass
from dataclasses import field

from src.datatypes.common import Color

T = TypeVar("T", bound="Entity")


@dataclass(unsafe_hash=True)
class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    x: int = field(default=0)
    y: int = field(default=0)
    char: str = field(default="?")
    color: Color = field(default=(255, 255, 255))
    name: str = field(default="<Unnamed>")
    blocks_movement: bool = field(default=False)

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

    def spawn(self: T, gamemap: "Map", x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone
