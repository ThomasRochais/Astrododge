from projectiles import Projectile
import pygame
from menu import MainMenu, OptionsMenu, CreditsMenu
from rocket import Rocket


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
        self.bullets = []

    def game_loop(self):
        i = 0  # Projectiles loop
        while self.playing:
            self.display.fill(self.BLACK)  # Black screen
            self.check_events()
            if self.START_KEY:
                self.playing = False
                # Reset the keys so the menu doesn't jump around
                self.reset_keys()
            if i == 0:  # Generate a new bullet every freq per frame
                self.bullets.append(Projectile(self.rocket))
            i = (i + 1) % self.projectile.freq
            self.bullets_update()
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
                    self.bullets = []
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

    def bullets_update(self):
        for bullet in self.bullets:  # Move the bullets
            bullet.move_projectile()
            if bullet.remove:  # Delete bullets
                self.bullets.pop(self.bullets.index(bullet))

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
        for bullet in self.bullets:  # Draw all the bullets
            bullet.blit_projectile()
        self.window.blit(self.display, (0, 0))  # Blitting is drawing
        pygame.display.update()
