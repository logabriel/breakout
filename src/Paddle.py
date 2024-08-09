"""
ISPPJ1 2024
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Paddle.
"""

import pygame

import settings
from src.Cannon import Cannon


class Paddle:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 64
        self.height = 16
        self.cannonLeft = Cannon(
            self.x - 12, settings.VIRTUAL_HEIGHT - 32 - 6 , 1
        )
        self.cannonRight = Cannon(
            self.x + self.width, settings.VIRTUAL_HEIGHT - 32 - 6, 0
        )

        # By default, the blue paddle
        self.skin = 0

        # By default, the 64-pixels-width paddle.
        self.size = 1

        self.texture = settings.TEXTURES["spritesheet"]
        self.frames = settings.FRAMES["paddles"]

        # The paddle only move horizontally
        self.vx = 0

    def resize(self, size: int) -> None:
        self.size = size
        self.width = (self.size + 1) * 32

    def dec_size(self):
        self.resize(max(0, self.size - 1))

    def inc_size(self):
        self.resize(min(3, self.size + 1))

    def activeCannons(self):
        if self.cannonLeft.active:
            self.cannonLeft.active = False
            self.cannonRight.active = False
        else:
            self.cannonLeft.active = True
            self.cannonRight.active = True

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt: float) -> None:
        next_x = self.x + self.vx * dt

        if self.vx < 0:
            self.x = max(0, next_x)
        else:
            self.x = min(settings.VIRTUAL_WIDTH - self.width, next_x)

        self.cannonLeft.update(dt, self.x - self.cannonRight.width)
        self.cannonRight.update(dt, self.x + self.width)

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, (self.x, self.y), self.frames[self.skin][self.size])
        self.cannonLeft.render(surface)
        self.cannonRight.render(surface)
