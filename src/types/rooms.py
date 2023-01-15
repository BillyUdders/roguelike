from dataclasses import dataclass, field
from typing import Tuple


@dataclass
class RectangularRoom:
    x1: int
    y1: int
    width: int
    height: int
    x2: int = field(init=False)
    y2: int = field(init=False)

    def __post_init__(self):
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height

    @property
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)
