from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from tcod.console import Console
from tcod.context import Context
from tcod.map import compute_fov

from src.datatypes.actions import Action
from src.datatypes.entity import Entity
from src.input_handler import InputHandler
from src.map import Map


@dataclass
class Engine:
    event_handler: InputHandler
    game_map: Map
    player: Entity

    def __post_init__(self):
        self.update_fov()

    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.entities - {self.player}:
            print(f"The {entity.name} wonders when it will get to take a real turn.")

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action: Action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)
            self.handle_enemy_turns()
            self.update_fov()

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        context.present(console)
        console.clear()
