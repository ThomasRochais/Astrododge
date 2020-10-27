import pygame
import os


class Rocket():
    def __init__(self, game):
        self.game = game
        self.spaceship = pygame.image.load(os.path.join("assets/sprites", "spaceship-a.svg"))
        self.spaceship = pygame.transform.rotate(self.spaceship, -90)
        self.width, self.height = self.spaceship.get_size()
        self.width, self.height = round(self.width * .4), round(self.height * .4)
        self.spaceship = pygame.transform.scale(self.spaceship, (self.width, self.height))
        self.x, self.y = 0, self.game.DISPLAY_H / 2 - self.height / 2
        self.vel = 1

    def position(self, pos):
        if pos == 'CENTER':
            return self.game.DISPLAY_W / 2 - self.width / 2, self.game.DISPLAY_H / 2 - self.height / 2
        if pos == 'TOP':
            return self.game.DISPLAY_W / 2 - self.width / 2, 0
        if pos == 'BOTTOM':
            return self.game.DISPLAY_W / 2 - self.width / 2, self.game.DISPLAY_H - self.height
        if pos == 'LEFT':
            return 0, self.game.DISPLAY_H / 2 - self.height / 2
        if pos == 'RIGHT':
            return self.game.DISPLAY_W - self.width, self.game.DISPLAY_H / 2 - self.height / 2

    def blit_rocket(self):  # Displaying spaceship
        self.game.display.blit(self.spaceship, (self.x, self.y))

    def move_rocket(self):  # Moving the rocket and checking the boundaries
        if self.game.LEFT_KEY:
            if self.x - self.vel > 0:
                self.x -= self.vel
        if self.game.RIGHT_KEY:
            if self.x + self.vel < self.game.DISPLAY_W - self.width:
                self.x += self.vel
        if self.game.UP_KEY:
            if self.y - self.vel > 0:
                self.y -= self.vel
        if self.game.DOWN_KEY:
            if self.y + self.vel < self.game.DISPLAY_H - self.height:
                self.y += self.vel
