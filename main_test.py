import pygame
from game import Game

if __name__ == "__main__":
    g = Game()
    #Thomas: Commenting this out so I can test projectiles
    # while g.running:
    #     g.curr_menu.display_menu()
    #     g.game_loop()
    win=pygame.display.set_mode((500,500))
    pygame.display.set_caption("Test Game")
    x=50
    y=50
    width=40
    height=60
    vel=5
    run=True
    while run:
        pygame.time.delay(100)
        for even in pygame.event.get():
            if even.type==pygame.QUIT:
                run=False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= vel
        if keys[pygame.K_RIGHT]:
            x += vel
        if keys[pygame.K_UP]:
            y -= vel
        if keys[pygame.K_DOWN]:
            y += vel   
        win.fill((0,0,0))     
        pygame.draw.rect(win,(255,0,0),(x,y,width,height))
        pygame.display.update()
    pygame.quit()