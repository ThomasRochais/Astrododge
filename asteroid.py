import random
import math

import graphics


class Asteroid():
    def __init__(self, game):
        self.game = game
        self.image = graphics.load_sprite(
            "assets/sprites/asteroid1.png", scale=0.1)
        self.width, self.height = self.image.get_size()
        self.x, self.y = random.choice([
            (self.game.DISPLAY_W, random.uniform(0, self.game.DISPLAY_H)),
            (random.uniform(0, self.game.DISPLAY_W), - self.height * .99)])
        self.vel = 0.1  # Adjust velocity
        self.gravity = 0.0001  # Gravity coefficient for falling
        self.freq = 100  # Adjust frequency of frames per projectile
        self.remove = False
        self.rect = self.image.get_rect(topleft=(round(self.x), round(self.y)))
        self.mask = graphics.mask_from(self.image)

    def blit_asteroid(self):  # Displaying asteroid
        self.rect.topleft = (round(self.x), round(self.y))
        self.game.display.blit(self.image, self.rect)

    def move_asteroid(self):  # Moving the asteroid and checking the boundaries
        vel_y = math.sqrt(2 * self.gravity * (self.y + self.height))
        self.x -= self.vel
        self.y += vel_y
        self.rect.topleft = (round(self.x), round(self.y))
        # Gone once it drifts off the left edge or sinks past the bottom.
        if self.rect.right <= 0 or self.rect.bottom >= self.game.DISPLAY_H:
            self.remove = True

    def asteroids_update(self):
        for a in self.game.asteroids[:]:  # Iterate a copy so removals don't skip items
            a.move_asteroid()
            if a.remove:  # Delete asteroid
                self.game.asteroids.remove(a)
            else:
                if graphics.masks_collide(self.game.rocket, a):
                    self.game.asteroids.remove(a)
                    self.game.rocket.life -= 1
                    print("Rocket lives: ", self.game.rocket.life)
                else:
                    for p in self.game.projectiles[:]:
                        if graphics.masks_collide(a, p):
                            self.game.asteroids.remove(a)
                            self.game.projectiles.remove(p)
                            self.game.score += 1  # Reward for destroying an asteroid
                            break
