from dataclasses import dataclass
from dataclasses import field

import numpy as np
from tcod.console import Console

from src.datatypes import tiles


@dataclass
class Map:
    width: int
    height: int
    tiles: np.array = field(init=False)

    def __post_init__(self):
        self.tiles = np.full(
            (self.width, self.height), fill_value=tiles.wall, order="F"
        )

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0 : self.width, 0 : self.height] = self.tiles["dark"]
