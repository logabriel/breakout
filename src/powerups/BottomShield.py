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


class BottomShield(PowerUp):
    """
    power-up to create a shield that prevents the balls from falling
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 0)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        play_state.timerBottomShield = 0
        for ball in play_state.balls:
            ball.bandBottomShield = True

        self.active = False