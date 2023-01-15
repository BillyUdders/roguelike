from dataclasses import dataclass
from typing import Iterable, Any, List

from tcod.console import Console
from tcod.context import Context

from src.input_handler import InputHandler
from src.map import Map
from src.types.actions import Action
from src.types.entity import Entity


@dataclass
class Engine:
    entities: List[Entity]
    event_handler: InputHandler
    game_map: Map
    player: Entity

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action: Action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()