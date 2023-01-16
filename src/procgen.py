import random
from collections.abc import Iterator

import tcod

from src.map import Map
from src.types import tiles
from src.types.rooms import RectangularRoom

Coordinates = tuple[int, int]


def tunnel_between(start: Coordinates, end: Coordinates) -> Iterator[Coordinates]:
    """Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:  # 50% chance.
        # Move horizontally, then vertically.
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally.
        corner_x, corner_y = x1, y2

    # Generate the coordinates for this tunnel.
    yield from tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist()
    yield from tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist()


def generate_dungeon(map_width, map_height) -> Map:
    dungeon = Map(map_width, map_height)

    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner] = tiles.floor
    dungeon.tiles[room_2.inner] = tiles.floor

    return dungeon
