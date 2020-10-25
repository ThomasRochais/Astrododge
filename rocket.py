import pygame
import os 


class Rocket():
    def __init__(self, game):
        self.game = game  # Use a game object
        # Initial position of the rectangle (bottom, centered)
        self.spaceship = pygame.image.load(os.path.join("assets/sprites", "spaceship-a.svg"))
        self.width, self.height = self.spaceship.get_size()
        # Rescale spaceship
        self.width, self.height = round(self.width * .4), round(self.height * .4)
        self.spaceship = pygame.transform.scale(self.spaceship, (self.width, self.height))
        # Initial position and velocity
        self.x, self.y = self.game.DISPLAY_W / 2 - self.width / 2, self.game.DISPLAY_H - self.height
        self.vel = 1  # Moving velocity

    def blit_rocket(self):
        self.game.display.blit(self.spaceship, (self.x, self.y))

    def move_left(self):
        if self.x - self.vel > 0:
            self.x -= self.vel

    def move_right(self):
        if self.x + self.vel < self.game.DISPLAY_W - self.width:
            self.x += self.vel

    def move_up(self):
        if self.y - self.vel > 0:
            self.y -= self.vel

    def move_down(self):
        if self.y + self.vel < self.game.DISPLAY_H - self.height:
            self.y += self.vel
