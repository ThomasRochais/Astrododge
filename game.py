import pygame
from pygame import key
from menu import *
from rocket import *
class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 600, 800
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.rocket=Rocket(self)

    def game_loop(self):
        while self.playing:
            #self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            pygame.key.set_repeat(10,5)#So rocket can keep moving when pressing and holding keys
            self.display.fill(self.BLACK)#Black screen
            self.check_events()
            if self.START_KEY:
                self.playing= False
            if self.LEFT_KEY:
                self.rocket.move_left()
            if self.RIGHT_KEY:
                self.rocket.move_right()
            if self.UP_KEY:
                self.rocket.move_up()
            if self.DOWN_KEY:
                self.rocket.move_down() 
            self.redrawGameWindow()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
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
                    
    def reset_keys(self):
        self.LEFT_KEY, self.RIGHT_KEY,self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def redrawGameWindow(self):
        self.rocket.blit_rocket()#Draw the rocket
        self.window.blit(self.display, (0,0))#Blitting is drawing
        pygame.display.update()
