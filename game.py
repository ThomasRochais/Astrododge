import pygame
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
        self.asteroid = Asteroid(self)
        self.asteroids = []

    def game_loop(self):
        i = 0  # Projectiles loop
        j = 0  # Asteroids loop
        while self.playing:
            self.display.fill(self.BLACK)  # Black screen
            self.check_events()
            if self.START_KEY:
                self.playing = False
                # Reset the keys so the menu doesn't jump around
                self.reset_keys()
            if i == 0:  # Generate a new projectile every freq per frame
                self.projectiles.append(Projectile(self.rocket))
            i = (i + 1) % self.projectile.freq
            if j == 0:  # Generate a new asteroid every freq per frame
                self.asteroids.append(Asteroid(self))
            j = (j + 1) % self.asteroid.freq
            self.asteroids_update()
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

    def asteroids_update(self):
        for a in self.asteroids:  # Move the asteroids
            a.move_asteroid()
            if a.remove:  # Delete asteroid
                self.asteroids.pop(self.asteroids.index(a))
            else:
                if self.collision_rocket(a, self.rocket):
                    self.asteroids.pop(self.asteroids.index(a))
                    self.rocket.life -= 1
                    print("Rocket lives: ", self.rocket.life)
                else:
                    for p in self.projectiles:
                        if self.collision_projectile(a, p):
                            self.asteroids.pop(self.asteroids.index(a))
                            self.projectiles.pop(self.projectiles.index(p))
                            break

    def projectiles_update(self):
        for p in self.projectiles:  # Move the projectiles
            p.move_projectile()
            if p.remove:  # Delete projectiles
                self.projectiles.pop(self.projectiles.index(p))

    def collision_projectile(self, asteroid, projectile):
        if asteroid.y + asteroid.height > projectile.y \
                and asteroid.y < projectile.y + projectile.height \
                and asteroid.x < projectile.x + projectile.width \
                and asteroid.x + asteroid.width > projectile.x:
            return True
        else:
            return False

    def collision_rocket(self, asteroid, rocket):
        if asteroid.y + asteroid.height > rocket.y and asteroid.y < rocket.y + rocket.height \
                and asteroid.x < rocket.x + rocket.width / 2 and asteroid.x + asteroid.width > rocket.x:
            return True
        elif asteroid.y + asteroid.height > rocket.y + rocket.height / rocket.width * (asteroid.x + asteroid.width / 2) \
                and asteroid.y < rocket.y - rocket.height / rocket.width * (asteroid.x + asteroid.width / 2) \
                and asteroid.x < rocket.x + rocket.width \
                and asteroid.x + asteroid.width > rocket.x + rocket.width / 2:
            return True
        else:
            return False

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
        for a in self.asteroids:  # Draw all the asteroids
            a.blit_asteroid()
        self.window.blit(self.display, (0, 0))  # Blitting is drawing
        pygame.display.update()
