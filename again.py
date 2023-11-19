import pygame, sys
import random
from pygame.math import Vector2

class CATERPILLAR:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        self.crunch_sound = pygame.mixer.Sound('human-impact-on-ground-6982.mp3')
    def draw_caterpillar(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(183,111,122), block_rect)
    def move_caterpillar(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+ self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True
    def play_crunch_sound(self):
        self.crunch_sound.play()
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)


class FRUIT:
    def __init__(self):
        self.randomize()
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x *cell_size),int(self.pos.y *cell_size),cell_size,cell_size)
        screen.blit(grapes,fruit_rect)
    
       # pygame.draw.rect(screen,(225,225,225),fruit_rect)
    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y =random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)





class MAIN:
    def __init__(self):
        self.caterpillar = CATERPILLAR()
        self.fruit = FRUIT()
    def update(self):
        self.caterpillar.move_caterpillar()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.caterpillar.draw_caterpillar()
        self.draw_score()

    def check_collision (self):
        if self.fruit.pos == self.caterpillar.body[0]:
            self.fruit.randomize()
            self.caterpillar.play_crunch_sound()
    

            
            self.caterpillar.add_block()
    def check_fail(self):
        #check if caterpillir is outside of the screen 
        if not 0 <= self.caterpillar.body[0].x < cell_number or not 0 <= self.caterpillar.body[0].y < cell_number:
            self.game_over()

        for block in self.caterpillar.body[1:]:
            if block == self.caterpillar.body[0]:
                self.game_over()
         
        

    def game_over(self):
        self.caterpillar.reset()
    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0:

                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    def draw_score(self):
        score_text = str(len(self.caterpillar.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        grapes_rect = grapes.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(grapes_rect.left,grapes_rect.top,grapes_rect.width + score_rect.width,grapes_rect.height)
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(grapes,grapes_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

        
pygame.mixer.pre_init(44100,-16,512)

        




pygame.init()
cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
grapes = pygame.image.load('grape.png').convert_alpha()
grapes = pygame.transform.scale(grapes,(50,50))
game_font = pygame.font.Font('Spooky_Squishe.otf', 25)
pygame.display.set_caption('The Great Caterpillar ')
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
main_game = MAIN()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
            


        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.caterpillar.direction.y != 1:
                        main_game.caterpillar.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    if main_game.caterpillar.direction.x != -1:
                        main_game.caterpillar.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    if main_game.caterpillar.direction.y != -1:
                        main_game.caterpillar.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    if main_game.caterpillar.direction.x != 1:
                        main_game.caterpillar.direction = Vector2(-1,0)

    screen.fill((175,215,70))
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)  