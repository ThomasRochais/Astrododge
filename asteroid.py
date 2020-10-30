import pygame
import os


class Asteroid():
    def __init__(self, game, id):
        self._id = id
        self.game = game
        self.asteroid = pygame.transform.scale(pygame.image.load(os.path.join("assets/sprites", "asteroid2.png")), (50,50))
        self.width, self.height = self.asteroid.get_size()
        self.x, self.y = 50,50
        self.vel = 1

    def move_asteroid(self):
        if self.x > self.game.rocket.x:
            self.x = self.x - self.vel
            self.y = self.y
        
    def blit_asteroid(self):  # Displaying spaceship
        self.game.display.blit(self.asteroid, (self.x, self.y))
