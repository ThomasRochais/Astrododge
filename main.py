import pygame
from game import Game
#from game_original import Game

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()