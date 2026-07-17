import random

import pygame

import graphics


class Character():
    # Rescuable characters: fly the rocket into one for a bonus.
    SPRITES = [
        "assets/sprites/pico-a.svg",
        "assets/sprites/nano-a.svg",
        "assets/sprites/giga-a.svg",
        "assets/sprites/tera-a.svg",
    ]

    def __init__(self, game):
        self.game = game
        self.image = graphics.load_sprite(random.choice(self.SPRITES), scale=0.5)
        self.width, self.height = self.image.get_size()
        # Stationary spawn: random spot clear of the HUD band and the screen edges.
        top_margin = 45  # Keep below the HUD text along the top
        self.x = random.uniform(0, self.game.DISPLAY_W - self.width)
        self.y = random.uniform(top_margin, self.game.DISPLAY_H - self.height)
        self.freq = 400  # Frames between spawns (mirrors asteroid/projectile freq)
        self.lifespan = 4000  # Milliseconds visible before vanishing if not rescued
        self.spawn_time = pygame.time.get_ticks()
        self.reward = 5  # Points earned for rescuing this character
        self.remove = False
        self.rect = self.image.get_rect(topleft=(round(self.x), round(self.y)))
        self.mask = graphics.mask_from(self.image)

    def blit_character(self):  # Displaying character
        self.rect.topleft = (round(self.x), round(self.y))
        self.game.display.blit(self.image, self.rect)

    def update_character(self):  # Vanish once its lifespan elapses
        if pygame.time.get_ticks() - self.spawn_time >= self.lifespan:
            self.remove = True

    def characters_update(self):
        for c in self.game.characters[:]:  # Iterate a copy so removals don't skip items
            c.update_character()
            if c.remove:  # Expired: gone before it was rescued
                self.game.characters.remove(c)
            elif graphics.masks_collide(self.game.rocket, c):  # Rescued by the rocket
                self.game.characters.remove(c)
                self.game.score += c.reward
