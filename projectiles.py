import pygame
import os


class Projectile():
    def __init__(self, rocket):
        self.rocket = rocket
        self.game = rocket.game
        self.bullet = pygame.image.load(os.path.join("assets/sprites", "asteroid2.png"))  # Change
        self.width, self.height = self.bullet.get_size()
        self.width, self.height = round(self.width * .05), round(self.height * .05)
        self.bullet = pygame.transform.scale(self.bullet, (self.width, self.height))
        self.x = self.rocket.x + self.rocket.width
        self.y =  self.rocket.y + self.rocket.height / 2 - self.height / 2
        self.vel = self.rocket.vel * 2  # Adjust velocity
        self.freq = self.width // self.vel * 5 # Adjust frequency of frames per bullet
        self.remove = False

    def projectiles_loop(self):
        pass

    def blit_projectile(self):  # Displaying projectile
        self.game.display.blit(self.bullet, (self.x, self.y))

    def move_projectile(self):  # Moving the projectile and checking the boundaries
        if self.x + self.vel < self.game.DISPLAY_W:
            self.x += self.vel
        else:
            self.remove = True

