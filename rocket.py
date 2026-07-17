import graphics


class Rocket():
    def __init__(self, game):
        self.game = game
        # Vector ship rasterized crisply straight to its on-screen size.
        self.image = graphics.load_sprite(
            "assets/sprites/spaceship-a.svg", scale=0.4, rotate=-90)
        self.width, self.height = self.image.get_size()
        self.x, self.y = 0, self.game.DISPLAY_H / 2 - self.height / 2
        self.vel = 1
        self.life = 10  # Initial amount of lives
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = graphics.mask_from(self.image)

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
        self.rect.topleft = (round(self.x), round(self.y))
        self.game.display.blit(self.image, self.rect)

    def move_rocket(self):  # Moving the rocket, clamped to the screen bounds
        self.rect.topleft = (round(self.x), round(self.y))
        if self.game.LEFT_KEY:
            self.rect.x -= self.vel
        if self.game.RIGHT_KEY:
            self.rect.x += self.vel
        if self.game.UP_KEY:
            self.rect.y -= self.vel
        if self.game.DOWN_KEY:
            self.rect.y += self.vel
        self.rect.clamp_ip(self.game.screen_rect)  # Stay fully on-screen
        self.x, self.y = self.rect.x, self.rect.y
