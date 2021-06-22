import pygame
import os
import random
import math


class Asteroid():
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load(os.path.join("assets/sprites", "asteroid1.png"))
        self.width, self.height = self.image.get_size()
        self.width, self.height = round(self.width * .1), round(self.height * .1)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.width, self.height = self.image.get_size()
        self.x, self.y = random.choice([
            (self.game.DISPLAY_W, random.uniform(0, self.game.DISPLAY_H)),
            (random.uniform(0, self.game.DISPLAY_W), - self.height * .99)])
        self.vel = 0.1  # Adjust velocity
        self.gravity = 0.0001  # Gravity coefficient for falling
        self.freq = 100  # Adjust frequency of frames per projectile
        self.remove = False

    def blit_asteroid(self):  # Displaying projectile
        self.game.display.blit(self.image, (self.x, self.y))

    def move_asteroid(self):  # Moving the projectile and checking the boundaries
        vel_y = math.sqrt(2 * self.gravity * (self.y + self.height))
        if self.x + self.width - self.vel > 0 and self.y + vel_y < self.game.DISPLAY_H:
            self.x -= self.vel
            self.y += vel_y
        else:
            self.remove = True
