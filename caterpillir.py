import pygame
from pygame.locals import *

def draw_block():
    surface.fill((225, 225, 225))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000,500))
    surface.fill((255,255,255))

    block = pygame.image.load("green leaf.png").convert()
    surface.blit(block,(0,0))

    pygame.display.flip()
    
    running = True
    
    
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
    surface.blit(block,(0,0))  

     
     
