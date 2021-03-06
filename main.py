
from numpy import tile
import pygame
from pygame.locals import *
import random
from pygame import mixer

# incialization
pygame.mixer.pre_init(44100,-16,2,512)
mixer.init()
pygame.init()

width = 1000
height = 1000

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Astro Runner")

# fonts
font_score = pygame.font.SysFont("Consolas" , size= 40)
font = pygame.font.SysFont("Consolas" , size= 90)
# colors
white = (255,255,255)
orange = (255,140,0)

# game variables
running = True
tile_size = 50 
clock = pygame.time.Clock()
game_over = False
main_menu = True
level = 1
max_level = 2
score = 0

# create world 
world_data1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,6,0,0,0,0,0,1,1,0,0,0,0,0,0,3,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
    [1,0,0,0,0,0,2,1,1,0,0,0,0,1,1,1,2,2,1,1],
    [1,0,0,0,0,7,1,0,0,0,0,0,0,1,1,1,1,1,1,1],
    [1,0,0,0,5,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,7,1,1,1,1,2,2,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,0,0,0,0,3,3,3,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

world_data2 = [
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
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
    [1,0,0,0,0,0,2,1,1,0,0,0,0,1,1,1,2,2,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1],
    [1,0,0,5,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,1,1,2,2,1,2,2,2,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,4,0,0,1,1,0,0,0,0,3,3,3,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


# load images
space = pygame.image.load("bg/space.png").convert_alpha()
space = pygame.transform.scale(space,(1000,1000))
start_img = pygame.image.load("Button/Start.png").convert_alpha()
exit_img = pygame.image.load("Button/Exit.png").convert_alpha()
restart_image = pygame.image.load("Button/Restard.png").convert_alpha()
# load sound effects and bg music
coin_fx = pygame.mixer.Sound("music/coin.wav")
coin_fx.set_volume(0.4)
jump_fx = pygame.mixer.Sound("music/jump.wav")
jump_fx.set_volume(0.4)
bg_music = pygame.mixer.Sound('music/bg-music.mp3')
bg_music.set_volume(0.1)
bg_music.play(loops = -1)
game_over_fx = pygame.mixer.Sound("music/game_over.wav")
game_over_fx.set_volume(0.8)
# functions

def draw_text(text , font , text_color , x , y):
    img = font.render(text,True,text_color)
    screen.blit(img, (x, y))

def reset_level(level):
    # global variables
    global score
    score = 0
    # reset player position
    player.reset(100,height-130)
    # clear sprite groups
    spike_group.empty()
    lava_group.empty()
    exit_group.empty()
    coin_group.empty()
    platform_group.empty()
    # coin that will show with score
    score_coin = Coin(tile_size // 2 ,tile_size -50)
    coin_group.add(score_coin)
    
    # load data for world
    if level == 1:
        world_data = world_data1
        world = World(world_data)   
    if level == 2:
        world_data = world_data2
        world = World(world_data)
    else:
        world_data = world_data1
        world = World(world_data)
    
    return world
    
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

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,move_x,move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Osticle/platform.png").convert_alpha()
        self.image = pygame.transform.scale(img,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.direction = 1
        self.move_x = move_x
        self.move_y = move_y
        
    def update(self):
        self.rect.x += self.direction * self.move_x
        self.rect.y += self.direction * self.move_y 
        self.move_counter += 1
        if self.move_counter > 50:
            self.direction *= -1
            self.move_counter *= -1
              
platform_group = pygame.sprite.Group()

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Osticle/gold_bar.png").convert_alpha()
        self.image = pygame.transform.scale(img,(tile_size,tile_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

coin_group = pygame.sprite.Group()

# coin that will show with score
score_coin = Coin(tile_size // 2 ,tile_size -50)
coin_group.add(score_coin)
class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("Portal/portal.png").convert_alpha()
        self.image = pygame.transform.scale(img,(tile_size,tile_size * 1.5))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
exit_group = pygame.sprite.Group()
        
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
                if tile == 4:
                    exit = Exit(col_count * tile_size , row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                if tile == 5:
                    coin = Coin(col_count * tile_size, row_count * tile_size)
                    coin_group.add(coin)
                if tile == 6:
                    platform = Platform(col_count* tile_size, row_count * tile_size,1,0)
                    platform_group.add(platform)
                if tile == 7:
                    platform = Platform(col_count* tile_size, row_count * tile_size,0,1)
                    platform_group.add(platform)
                if tile == 8:
                    platform = Platform(col_count* tile_size, row_count * tile_size,1,1)
                    platform_group.add(platform)
                col_count += 1
            row_count += 1
    
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            
# load data for world
if level == 1:
    world_data = world_data1
    world = World(world_data)   
if level == 2:
    world_data = world_data2
    world = World(world_data)
else:
    world_data = world_data1
    world = World(world_data)

class Player():
    
    def __init__(self,x,y):
        self.reset(x,y)
    def  update(self):
        # variables
        delta_x = 0
        delta_y = 0
        anim_cooldown = 30
        col_threshold = 20
        # global variables
        global game_over
        global score
        if game_over == False:
            # get key input
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                jump_fx.play()
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
                game_over_fx.play()
                game_over = True
            # check for collision with lava
            if pygame.sprite.spritecollide(self,lava_group,False):
                
                game_over = True
            # check for collision with portal
            if pygame.sprite.spritecollide(self,exit_group,False):
                game_over = "Win"
            # check for collision with coin
            if pygame.sprite.spritecollide(self,coin_group,True):
                coin_fx.play()
                score += 1
            # check for collision with platforms
            for platform in platform_group:
                # collision in x direction
                if platform.rect.colliderect(self.rect.x+delta_x, self.rect.y,self.width,self.height):
                    delta_x = 0
                # collision in y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y+delta_y,self.width,self.height):
                    # check if bellow
                    if abs((self.rect.top + delta_y) -platform.rect.bottom ) < col_threshold:
                        self.velocity = 0
                        delta_y = platform.rect.bottom - self.rect.top
                    # check if above platform
                    elif abs((self.rect.bottom + delta_y) -platform.rect.top ) < col_threshold:
                        self.rect.bottom = platform.rect.top - 1
                        delta_y = 0
                        self.in_air = False
                    # move side ways with platform
                    if platform.move_x != 0:
                        self.rect.x += platform.direction
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
            platform_group.update()
        # draw score
        draw_text("  "+ str(score) , font_score , white , tile_size - 10 , 10 )
        # draw enemy spike
        spike_group.draw(screen)
            # draw lava group
        lava_group.draw(screen)
            # draw portal 
        exit_group.draw(screen)
            # draw coins
        coin_group.draw(screen)
            # draw platforms
        platform_group.draw(screen)
        
        if game_over == True:
            draw_text(" GAME OVER ", font , orange , (width // 2 ) -250, height // 2.5)
            if button.draw():
                world_data = []
                world = reset_level(level)
                game_over = False
        # if player completed level
        if game_over == "Win":
            # reset level and go to next level
            level += 1
            if level <= max_level:
                # reset level
                world_data = []
                world = reset_level(level)
                game_over = False
            else:
                draw_text(" YOU WIN" , font , orange , (width // 2 ) -220, height // 2.5 )
                if button.draw():
                    level = 1
                    world_data = []
                    world = reset_level(level)
                    game_over = False
    pygame.display.update()
    # clock
    clock.tick(240)    
pygame.quit()
