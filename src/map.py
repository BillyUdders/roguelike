from dataclasses import dataclass
from dataclasses import field
from typing import Optional
from typing import TYPE_CHECKING

import numpy as np
from tcod.console import Console

from src.datatypes import tiles

if TYPE_CHECKING:
    from src.datatypes.entity import Entity


@dataclass
class Map:
    width: int
    height: int
    entities: set["Entity"]

    tiles: np.array = field(init=False)
    visible: np.array = field(init=False)
    explored: np.array = field(init=False)

    def __post_init__(self):
        dimensions = (self.width, self.height)
        self.tiles = np.full(dimensions, fill_value=tiles.wall, order="F")
        self.visible = np.full(dimensions, fill_value=False, order="F")
        self.explored = np.full(dimensions, fill_value=False, order="F")

    def get_blocking_entity_at_location(
        self, location_x: int, location_y: int
    ) -> Optional["Entity"]:
        for entity in self.entities:
            if (
                entity.blocks_movement
                and entity.x == location_x
                and entity.y == location_y
            ):
                return entity

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".
        """
        console.tiles_rgb[0 : self.width, 0 : self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tiles.SHROUD,
        )

        for entity in self.entities:
            # Only print entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)
