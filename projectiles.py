import pygame
import os


class Projectile():
    def __init__(self, rocket):
        self.rocket = rocket
        self.game = rocket.game
        self.bullet = pygame.image.load(os.path.join("assets/sprites", "asteroid2.png"))  # Change
        self.width, self.height = self.spaceship.get_size()
        self.x, self.y = self.rocket.x + self.rocket.width, self.rocket.y + self.rocket.height / 2
        self.vel = self.rocket.vel * 3  # Adjust velocity
        self.freq = self.width // self.vel * 3  # Adjust frequency of bullets per frame

    def projectiles_loop(self):
        pass

    def blit_projectile(self):  # Displaying projectile
        self.game.display.blit(self.bullet, (self.x, self.y))

    def move_rocket(self):  # Moving the rocket and checking the boundaries
        if self.x + self.vel < self.game.DISPLAY_W - self.width:
            self.x += self.vel
