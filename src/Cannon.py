from typing import Any, Tuple, Optional

import pygame

import settings

class Cannon:
    def __init__(self, x: int, y: int, sideCanon: int) -> None:
        self.x = x
        self.y = y
        self.width = 12
        self.height = 24

        self.texture = settings.TEXTURES["cannons"]
        self.active = True
        self.sideCannon = sideCanon #0 left, 1 right

    def update(self, dt: float, position: float) -> None:
        self.x = position

    def render(self, surface):
        if self.active:
            surface.blit(
                self.texture, (self.x, self.y), settings.FRAMES["cannons"][self.sideCannon]
            )
