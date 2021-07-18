import pygame
import os


class Rocket():
    def __init__(self, game):
        self.game = game
        self.image = pygame.image.load(os.path.join("assets/sprites", "spaceship-a.svg"))
        self.image = pygame.transform.rotate(self.image, -90)
        self.width, self.height = self.image.get_size()
        self.width, self.height = round(self.width * .4), round(self.height * .4)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.x, self.y = 0, self.game.DISPLAY_H / 2 - self.height / 2
        self.vel = 1
        self.life = 10  # Initial amount of lives

    def starting_position(self, pos):
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

    def blit_rocket(self):  # Displaying rocket image
        self.game.display.blit(self.image, (self.x, self.y))

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

    def collision_rocket(self, asteroid):
        if asteroid.y + asteroid.height > self.y and asteroid.y < self.y + self.height \
                and asteroid.x < self.x + self.width / 2 and asteroid.x + asteroid.width > self.x:
            return True
        elif asteroid.y + asteroid.height > self.y + self.height / self.width * (asteroid.x + asteroid.width / 2) \
                and asteroid.y < self.y - self.height / self.width * (asteroid.x + asteroid.width / 2) \
                and asteroid.x < self.x + self.width \
                and asteroid.x + asteroid.width > self.x + self.width / 2:
            return True
        else:
            return False
