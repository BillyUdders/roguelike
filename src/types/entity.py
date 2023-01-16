from dataclasses import dataclass, field

from src.types.common import Color


@dataclass(eq=True)
class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    x: int = field(hash=True)
    y: int = field(hash=True)
    char: str
    color: Color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
