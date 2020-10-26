import pygame
import os


class Rocket():
    def __init__(self, game):
        self.game = game  # Use a game object
        # Initial position of the rectangle (bottom, centered)
        self.spaceship = pygame.image.load(os.path.join("assets/sprites", "spaceship-a.svg"))
        # Rotate the spaceship 90degrees clockwise
        self.spaceship = pygame.transform.rotate(self.spaceship, -90)
        self.width, self.height = self.spaceship.get_size()
        # Rescale spaceship
        self.rescale(.4)
        self.spaceship = pygame.transform.scale(self.spaceship, (self.width, self.height))
        # Initial position and velocity
        self.init_pos('LEFT')
        self.vel = 1  # Moving velocity

    def init_pos(self, pos):  # Initial position of spaceship
        if pos == 'CENTER':
            self.x, self.y = self.game.DISPLAY_W / 2 - self.width / 2, self.game.DISPLAY_H / 2 - self.height / 2
        if pos == 'TOP':
            self.x, self.y = self.game.DISPLAY_W / 2 - self.width / 2, 0
        if pos == 'BOTTOM':
            self.x, self.y = self.game.DISPLAY_W / 2 - self.width / 2, self.game.DISPLAY_H - self.height
        if pos == 'LEFT':
            self.x, self.y = 0, self.game.DISPLAY_H / 2 - self.height / 2
        if pos == 'RIGHT':
            self.x, self.y = self.game.DISPLAY_W - self.width, self.game.DISPLAY_H / 2 - self.height / 2

    def rescale(self, scale):  # Rescaling spaceship
        self.width, self.height = round(self.width * scale), round(self.height * scale)

    def blit_rocket(self):  # Displaying spaceship
        self.game.display.blit(self.spaceship, (self.x, self.y))

    def move_left(self):  # Moving spaceship left
        if self.x - self.vel > 0:
            self.x -= self.vel

    def move_right(self):  # Moving spaceship right
        if self.x + self.vel < self.game.DISPLAY_W - self.width:
            self.x += self.vel

    def move_up(self):  # Moving spaceship up
        if self.y - self.vel > 0:
            self.y -= self.vel

    def move_down(self):  # Moving spaceship down
        if self.y + self.vel < self.game.DISPLAY_H - self.height:
            self.y += self.vel
