import pygame
import os


class Projectile():
    def __init__(self, rocket):
        self.rocket = rocket
        self.game = rocket.game
        self.image = pygame.image.load(os.path.join("assets/sprites", "bullet2.png")) 
        self.image = pygame.transform.rotate(self.image, -90)
        self.width, self.height = self.image.get_size()
        # self.width, self.height = round(self.width * .05), round(self.height * .05)
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x = self.rocket.x + self.rocket.width
        self.y = self.rocket.y + self.rocket.height / 2 - self.height / 2
        self.vel = self.rocket.vel * 1  # Adjust velocity
        self.freq = self.width // self.vel * 3  # Adjust frequency of frames per projectile
        self.remove = False

    def blit_projectile(self):  # Displaying projectile
        self.game.display.blit(self.image, (self.x, self.y))

    def move_projectile(self):  # Moving the projectile and checking the boundaries
        if self.x + self.vel < self.game.DISPLAY_W:
            self.x += self.vel
        else:
            self.remove = True
