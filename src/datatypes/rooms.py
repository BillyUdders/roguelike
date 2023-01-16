from dataclasses import dataclass
from dataclasses import field


@dataclass
class RectangularRoom:
    x: int
    y: int
    width: int
    height: int
    x2: int = field(init=False)
    y2: int = field(init=False)

    def __post_init__(self):
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height

    @property
    def center(self) -> tuple[int, int]:
        center_x = int((self.x + self.x2) / 2)
        center_y = int((self.y + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> tuple[slice, slice]:
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x + 1, self.x2), slice(self.y + 1, self.y2)

    def intersects(self, other: "RectangularRoom") -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        return (
            self.x <= other.x2
            and self.x2 >= other.x
            and self.y <= other.y2
            and self.y2 >= other.y
        )
