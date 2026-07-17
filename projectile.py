import pygame

import graphics


class Projectile():
    def __init__(self, rocket):
        self.rocket = rocket
        self.game = rocket.game
        # Procedural glowing bolt, built vertically then turned to fly rightward.
        self.image = pygame.transform.rotate(graphics.make_laser(6, 22), -90)
        self.width, self.height = self.image.get_size()
        self.x = self.rocket.x + self.rocket.width
        self.y = self.rocket.y + self.rocket.height / 2 - self.height / 2
        self.vel = self.rocket.vel * 1  # Adjust velocity
        self.freq = self.width // self.vel * 3  # Adjust frequency of frames per projectile
        self.remove = False
        self.rect = self.image.get_rect(topleft=(round(self.x), round(self.y)))
        self.mask = graphics.mask_from(self.image)

    def blit_projectile(self):  # Displaying projectile
        self.rect.topleft = (round(self.x), round(self.y))
        self.game.display.blit(self.image, self.rect)

    def move_projectile(self):  # Moving the projectile and checking the boundaries
        if self.x + self.vel < self.game.DISPLAY_W:
            self.x += self.vel
            self.rect.topleft = (round(self.x), round(self.y))
        else:
            self.remove = True
