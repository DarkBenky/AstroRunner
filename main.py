from turtle import width
import pygame
from pygame.locals import *
import random

pygame.init()

width = 1000
height = 1000

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Astro Runner")

# game variables
running = True
tile_size = 50
clock = pygame.time.Clock()

world_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,3,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1],
    [1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,3,1],
    [1,0,0,0,0,0,2,1,1,0,0,0,0,1,1,1,2,2,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,1,1,2,2,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# load images
space = pygame.image.load("bg/space.png").convert_alpha()
space = pygame.transform.scale(space,(1000,1000))

# classes

class World():
    def __init__(self,data):
        # variables
        row_count = 0
        self.tile_list = []
        
        # load images
        block = pygame.image.load("Osticle/block.png").convert_alpha()
        block_lava = pygame.image.load("Osticle/block_lava.png").convert_alpha()
        spike = pygame.image.load("Osticle/Spike.png").convert_alpha()
        gold = pygame.image.load("Osticle/gold_bar.png").convert_alpha()
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(block,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(block_lava,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(spike,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(gold,(tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
                 
world = World(world_data)     

class Player():
    def __init__(self,x,y):
        self.images_right = []
        self.images_left = []
        self.images_jump_right = []
        self.images_jump_left = []
        self.index = 0
        self.counter1 = 0
        self.direction = 0
        self.jump = 0
        # load images of walk to array
        for num in range(1,4): 
            img_right = pygame.image.load(f"Runner/astro{num}.png").convert_alpha()
            img_right = pygame.transform.scale(img_right,(40,80))
            left = pygame.transform.flip(img_right,True,False)
            self.images_right.append(img_right)
            self.images_left.append(left)
        # load images of jump to array
        for num in range(0,4): 
            img_jump = pygame.image.load(f"Runner/astro_fire{num}.png").convert_alpha()
            img_jump = pygame.transform.scale(img_jump,(40,80))
            img_jump_left = pygame.transform.flip(img_jump,True,False)
            self.images_jump_left.append(img_jump_left)
            self.images_jump_right.append(img_jump)
        self.image = self.images_right[self.index]    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = 0
        self.jumped = False
    def  update(self):
        # variables
        delta_x = 0
        delta_y = 0
        anim_cooldown = 30
        
        # get key input
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.jumped = True
            self.velocity = -6
            self.jump = 1 
        if key[pygame.K_SPACE] == False:
            self.jumped = False
            self.jump = 0
        if key[pygame.K_a]:
            delta_x -= 1
            self.counter += 1
            self.direction = -1
        if key[pygame.K_d]:
            delta_x += 1.5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_d] == False and key[pygame.K_a] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        # gravity
        self.velocity += 0.1
        if self.velocity > 4:
            self.velocity = 4    
        delta_y += self.velocity
        # animation walk
        if self.counter > anim_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
    
        
        if self.jump == 1 and self.direction == 1:
            index_jump = random.randint(0, len(self.images_jump_right)-1)
            self.image = self.images_jump_right[index_jump]
        if self.jump == 1 and self.direction == -1:
            index_jump = random.randint(0, len(self.images_jump_right)-1)
            self.image = self.images_jump_left[index_jump]
            
        
        
        # check for colision
        
        # update plyer coridinate
        self.rect.x += delta_x
        self.rect.y += delta_y
        if self.rect.bottom > height:
            self.rect.bottom = height
            delta_y = 0
        # draw
        screen.blit(self.image,self.rect)
    
        
player = Player(100,height-130)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # draw background
    screen.blit(space,(0,0))
    # draw grid
    world.draw()
    # draw player
    player.update()
    pygame.display.update()

    clock.tick(300)    
pygame.quit()
