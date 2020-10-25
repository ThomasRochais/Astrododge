import pygame
import os


class Projectile():
    def __init__(self, rocket):
        self.rocket = rocket
        self.game=self.rocket.game
        