import pygame
import time
from menu import MainMenu, OptionsMenu, CreditsMenu
from rocket import Rocket
from projectile import Projectile
from asteroid import Asteroid


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.UP_KEY, self.DOWN_KEY = False, False
        self.START_KEY, self.BACK_KEY = False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.rocket = Rocket(self)
        self.projectile = Projectile(self.rocket)
        self.projectiles = []
        self.asteroids = []

    def game_loop(self):
        i = 0  # Projectiles loop
        while self.playing:
            self.display.fill(self.BLACK)  # Black screen
            self.check_events()
            self.generateAsteroid()
            if self.START_KEY:
                self.playing = False
                # Reset the keys so the menu doesn't jump around
                self.reset_keys()
            if i == 0:  # Generate a new projectile every freq per frame
                self.projectiles.append(Projectile(self.rocket))
            i = (i + 1) % self.projectile.freq
            self.generateAsteroid()
            self.projectiles_update()
            self.rocket.move_rocket()
            self.redrawGameWindow()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                    self.rocket.x, self.rocket.y = self.rocket.starting_position('LEFT')
                    self.projectiles = []
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
            # Needed for continuous and diagonal movements
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = False
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = False
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = False
                if event.key == pygame.K_UP:
                    self.UP_KEY = False
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = False
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = False

    def projectiles_update(self):
        for p in self.projectiles:  # Move the projectiles
            p.move_projectile()
            if p.remove:  # Delete projectiles
                self.projectiles.pop(self.projectiles.index(p))

    def reset_keys(self):
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.UP_KEY, self.DOWN_KEY = False, False
        self.START_KEY, self.BACK_KEY = False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def redrawGameWindow(self):
        self.rocket.blit_rocket()  # Draw the rocket
        for p in self.projectiles:  # Draw all the projectiles
            p.blit_projectile()
        self.window.blit(self.display, (0, 0))  # Blitting is drawing
        pygame.display.update()

    def generateAsteroid(self):
        asteroid = Asteroid(self, len(self.asteroids) + 1)
        asteroid.blit_asteroid()
        self.asteroids.append(asteroid)
