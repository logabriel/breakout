"""
Assignment 3: Breakout

Author: Gabriel Perez and Ramon Belandria
"""

import random
from typing import TypeVar

from gale.factory import Factory

import settings
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp


class CannonsPair(PowerUp):
    """
    powerup to pair of cannons that trigger projectiles
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 6)
        

    def take(self, play_state: TypeVar("PlayState")) -> None:
        play_state.paddle.activeCannons()

        self.active = False