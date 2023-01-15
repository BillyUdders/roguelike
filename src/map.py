import numpy as np
from tcod.console import Console

from src.types import tiles


class Map:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.tiles = np.full((width, height), fill_value=tiles.floor, order="F")
        self.tiles[30:33, 22] = tiles.wall

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
