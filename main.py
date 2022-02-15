
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
game_over = False
main_menu = True


world_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,3,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1],
    [1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,4,3,0,0,0,0,1],
    [1,0,0,0,0,0,2,1,1,0,0,0,0,1,1,1,2,2,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,1,1,2,2,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,0,0,0,0,3,3,3,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# load images
space = pygame.image.load("bg/space.png").convert_alpha()
space = pygame.transform.scale(space,(1000,1000))
start_img = pygame.image.load("Button/Start.png").convert_alpha()
exit_img = pygame.image.load("Button/Exit.png").convert_alpha()
restart_image = pygame.image.load("Button/Restard.png").convert_alpha()
# classes

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
    def draw(self):
        
        # get mouse position
        pos = pygame.mouse.get_pos()
        action = False
        # check mouse over
        if self.rect.collidepoint(pos):
            # check mouse click
            if pygame.mouse.get_pressed()[0] == True and self.clicked ==  False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False
            action = False
                
        # drow button
        screen.blit(self.image,self.rect)
        return action
    
button = Button(width // 2 - 100   , height // 2  , restart_image)
start_button = Button(width // 2 -350 , height // 2 , start_img)
exit_button = Button(width // 2 + 150 , height // 2 , exit_img)
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Osticle/Spike.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.move_counter = 0
        
    def update(self):
        self.rect.x += self.direction
        self.move_counter += 1
        if self.move_counter > 50:
            self.direction *= -1
            self.move_counter *= -1
        
spike_group =   pygame.sprite.Group() 

class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Osticle/block_lava.png").convert_alpha()
        self.image = pygame.transform.scale(img,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

lava_group = pygame.sprite.Group()

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
                    lava = Lava(col_count * tile_size, row_count * tile_size)
                    lava_group.add(lava)
                if tile == 3:
                    spike = Enemy(col_count * tile_size +10 , row_count * tile_size + 15)
                    spike_group.add(spike)
                # if tile == 4:
                #     img = pygame.transform.scale(gold,(tile_size,tile_size))
                #     img_rect = img.get_rect()
                #     img_rect.x = col_count * tile_size
                #     img_rect.y = row_count * tile_size
                #     tile = (img,img_rect)
                #     self.tile_list.append(tile)
                col_count += 1
            row_count += 1
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            
                 
world = World(world_data)     

class Player():
    def __init__(self,x,y):
        self.reset(x,y)
    def  update(self):
        # variables
        delta_x = 0
        delta_y = 0
        anim_cooldown = 30
        global game_over
        if game_over == False:
            # get key input
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
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
            # jump animation
            if self.jump == 1 and self.direction == 1 :
                index_jump = random.randint(0, len(self.images_jump_right)-1)
                self.image = self.images_jump_right[index_jump]
            if self.jump == 1 and self.direction == -1 :
                index_jump = random.randint(0, len(self.images_jump_right)-1)
                self.image = self.images_jump_left[index_jump]
            # check for collision
            self.in_air = True
            for tile in world.tile_list:
                # check for x collision
                if tile[1].colliderect(self.rect.x+delta_x, self.rect.y,self.width,self.height):
                    delta_x = 0
                # check for collision y position
                if tile[1].colliderect(self.rect.x, self.rect.y+delta_y,self.width,self.height):
                    # check bolow the ground 
                    if self.velocity < 0:
                        delta_y = tile[1].bottom - self.rect.top
                        self.velocity = 0
                    # check about ground collision
                    elif self.velocity >= 0:
                        delta_y = tile[1].top - self.rect.bottom
                        self.velocity = 0
                        self.in_air = False
            # check for collision with enemies
            if pygame.sprite.spritecollide(self,spike_group,False):
                game_over = True
            # check for collision with lava
            if pygame.sprite.spritecollide(self,lava_group,False):
                game_over = True
            
        if game_over == True:
            self.image = self.death_image
            self.rect.y -= 1 
               
        # update player coridinates
        self.rect.x += delta_x
        self.rect.y += delta_y
        if self.rect.bottom > height:
            self.rect.bottom = height
            delta_y = 0
        # draw
        screen.blit(self.image,self.rect)
    def reset(self,x,y):
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
        self.death_image = pygame.image.load("Ghost/Ghost.png").convert_alpha()
        self.death_image = pygame.transform.scale(self.death_image,(40,60))
        self.image = self.images_right[self.index]    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity = 0
        self.jumped = False
        self.in_air = True
    
        
player = Player(100,height-130)

     
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    # draw background
    screen.blit(space,(0,0))
    
    # draw buttons
    if main_menu == True:
        if exit_button.draw():
            running = False
        if start_button.draw():
            main_menu = False
    else:
        # draw grid
        world.draw()
        # draw player
        player.update()
        if game_over == False:
            # update movement 
            spike_group.update()
        # draw enemy spike
        spike_group.draw(screen)
            # draw lava group
        lava_group.draw(screen)
        
        if game_over == True:
            if button.draw():
                player.reset(100,height-130)
                game_over = False  
    pygame.display.update()
    # clock
    clock.tick(300)    
pygame.quit()
