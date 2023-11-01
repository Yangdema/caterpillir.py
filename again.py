import pygame, sys
import random
from pygame.math import Vector2

class CATERPILLIR:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
    def draw_caterpillir(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122), block_rect)
    def move_caterpillir(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+ self.direction)
        self.body = body_copy[:]
class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x *cell_size),int(self.pos.y *cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(225,225,225),fruit_rect)
    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y =random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)




class MAIN:
    def __init__(self):
        self.caterpillir = CATERPILLIR()
        self.fruit = FRUIT()
    def update(self):
        self.caterpillir.move_caterpillir()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.caterpillir.draw_caterpillir()

    def check_collision (self):
        if self.fruit.pos == self.caterpillir.body[0]:
            self.fruit.randomize()
            
            #add another block to caterpillir


        




pygame.init()
cell_size = 40
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()





SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exist()
        if event.type == SCREEN_UPDATE:
            main_game.update()
            


        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_game.caterpillir.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    main_game.caterpillir.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    main_game.caterpillir.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    main_game.caterpillir.direction = Vector2(-1,0)

    screen.fill((175,215,70))
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)