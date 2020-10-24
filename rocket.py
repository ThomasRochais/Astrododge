import pygame
import os 
from menu import *
#First let's make a moving rectangle here and then modify to make a moving rocket
class Rocket():
    def __init__(self, game):
        self.game = game #Use a game object
        self.width, self.height = self.game.DISPLAY_W / 20, self.game.DISPLAY_H / 20#Size of the rectangle
        #Initial position of the rectangle (bottom, centered)
        self.x, self.y = self.game.DISPLAY_W / 2 - self.width/2, self.game.DISPLAY_H - self.height
        self.vel=1 #Moving velocity

    def blit_rocket(self):
        pygame.draw.rect(self.game.display,(255,0,0),(self.x,self.y,self.width,self.height))

    def move_left(self):
        if self.x - self.vel > 0:
            self.x -= self.vel

    def move_right(self):
        if self.x + self.vel < self.game.DISPLAY_W - self.width: 
            self.x += self.vel

    def move_up(self):
        if self.y - self.vel > 0:
            self.y -= self.vel

    def move_down(self):
        if self.y + self.vel < self.game.DISPLAY_H - self.height:
            self.y += self.vel