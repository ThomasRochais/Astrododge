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
        self.score = 0  # Points earned by shooting asteroids
        self.high_score_file = 'highscore.txt'  # Best score persisted between sessions
        self.high_score = self.load_high_score()

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
            self.asteroid.asteroids_update()
            self.projectiles_update()
            self.rocket.move_rocket()
            self.redrawGameWindow()
            if self.rocket.life <= 0:  # Game over: show screen, then back to the menu
                self.playing = False
                self.reset_keys()
                self.game_over_screen()

    def load_high_score(self):  # Read the best score from disk, defaulting to 0
        try:
            with open(self.high_score_file) as f:
                return int(f.read().strip())
        except (IOError, ValueError):  # Missing or corrupt file
            return 0

    def save_high_score(self):  # Persist the best score to disk
        try:
            with open(self.high_score_file, 'w') as f:
                f.write(str(self.high_score))
        except IOError:
            pass  # Not fatal: just skip persisting this run

    def game_over_screen(self):
        new_high_score = self.score > self.high_score
        if new_high_score:  # Beat the record: update and persist it
            self.high_score = self.score
            self.save_high_score()
        self.display.fill(self.BLACK)
        self.draw_text('GAME OVER', 50, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 50)
        self.draw_text('Score: ' + str(self.score), 30, self.DISPLAY_W / 2, self.DISPLAY_H / 2 + 10)
        if new_high_score:
            self.draw_text('NEW HIGH SCORE!', 25, self.DISPLAY_W / 2, self.DISPLAY_H / 2 + 45)
        else:
            self.draw_text('High Score: ' + str(self.high_score), 25, self.DISPLAY_W / 2, self.DISPLAY_H / 2 + 45)
        self.draw_text('Press Enter to continue', 20, self.DISPLAY_W / 2, self.DISPLAY_H / 2 + 85)
        self.window.blit(self.display, (0, 0))
        pygame.display.update()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.curr_menu.run_display = False
                    waiting = False
                if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_BACKSPACE):
                    waiting = False
        self.reset_keys()  # Don't carry the keypress into the menu

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                    self.rocket.x, self.rocket.y = self.rocket.starting_position('LEFT')
                    self.rocket.life = 10  # Reset lives for a fresh game
                    self.score = 0  # Reset score for a fresh game
                    self.projectiles = []
                    self.asteroids = []
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
        for p in self.projectiles[:]:  # Iterate a copy so removals don't skip items
            p.move_projectile()
            if p.remove:  # Delete projectiles
                self.projectiles.remove(p)

    def collision_projectile(self, asteroid, projectile):
        if asteroid.y + asteroid.height > projectile.y \
                and asteroid.y < projectile.y + projectile.height \
                and asteroid.x < projectile.x + projectile.width \
                and asteroid.x + asteroid.width > projectile.x:
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

    def draw_hud(self):  # Score on the left, high score centered, lives on the right
        self.draw_text('Score: ' + str(self.score), 20, 70, 20)
        self.draw_text('Best: ' + str(self.high_score), 20, self.DISPLAY_W / 2, 20)
        self.draw_text('Lives: ' + str(self.rocket.life), 20, self.DISPLAY_W - 70, 20)

    def redrawGameWindow(self):
        self.rocket.blit_rocket()  # Draw the rocket
        for p in self.projectiles:  # Draw all the projectiles
            p.blit_projectile()
        for a in self.asteroids:  # Draw all the asteroids
            a.blit_asteroid()
        self.draw_hud()  # Draw the score and lives on top
        self.window.blit(self.display, (0, 0))  # Blitting is drawing
        pygame.display.update()
