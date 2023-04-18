import pygame
import json
import os


# Initialize Pygame
pygame.init()

#getting the screen width and height of device currently running the program
device_screen = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = device_screen.current_w-100, device_screen.current_h-100

# Create the screen
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


IMG_PATH = 'Penguins/TenderBud'

SPRITES = {
    "walk_NE" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_NE/0.png'), (50,50)), 
    pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_NE/1.png'), (50,50)), 
    pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_NE/2.png'), (50,50)),
    pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_NE/3.png'), (50,50))],

    "walk_NW" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_NW/0.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_NW/1.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_NW/2.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_NW/3.png'), (50,50))],

    "walk_SE" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_SE/0.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_SE/1.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_SE/2.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_SE/3.png'), (50,50))],

    "walk_SW" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_SW/0.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_SW/1.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_SW/2.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_SW/3.png'), (50,50))],

    "walk_W" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_W/0.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_W/1.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_W/2.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_W/3.png'), (50,50)),],

    "walk_E" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_E/0.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_E/1.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_E/2.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_E/3.png'), (50,50))],

    "walk_N" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_N/0.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_N/1.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_N/2.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_N/3.png'), (50,50))],

    "walk_S" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_S/0.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_S/1.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_S/2.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/walk_S/3.png'), (50,50))],

    "IDLE" : [pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/0.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/1.png'), (50,50)), 
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/2.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/3.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/4.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/5.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/6.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/7.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/8.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/9.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/10.png'), (50,50)),
        pygame.transform.scale(pygame.image.load(IMG_PATH + '/idle/11.png'), (50,50))]
}

img = SPRITES["IDLE"][0]

# put the image onto the screen
SCREEN.blit(img, (0, 0))

# Update the display
pygame.display.update()

class penguin():
    WALK_DISTANCE = 6

    def __init__(self):
        self.hitbox_x = 50
        self.hitbox_y = 50                              # width and heigh of penguins hitbox 
        self.image = img
        self.cur_x = SCREEN_WIDTH // 2                  # starting position at center of screen
        self.cur_y = SCREEN_HEIGHT // 2

        self.state = "IDLE"                             # keep track of what state we're in 
        self.prev = []                              # used to signal a change of state (i.e prev != state) 

        self.index = 0                                  #index used to set img (animation)

    def update_sprite(self):
        self.image = SPRITES[self.state][self.index]

    #                          y
    #  (0, 0)                  ^
    #                          |
    #                          |   
    #  (0,screen_height)       |------>
    #                                  x

    def handle_movement(self,keys_pressed):
        
        self.prev = keys_pressed

        if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_DOWN] and self.cur_x - self.WALK_DISTANCE - self.hitbox_x > 0 and self.cur_y + self.WALK_DISTANCE + self.hitbox_y < SCREEN_HEIGHT:  # Southwest
            self.cur_x -= self.WALK_DISTANCE
            self.cur_y += self.WALK_DISTANCE
            self.state = "walk_SW"

        elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_DOWN] and self.cur_x + self.WALK_DISTANCE + self.hitbox_x < SCREEN_WIDTH and self.cur_y + self.WALK_DISTANCE + self.hitbox_y < SCREEN_HEIGHT:   # Southeast
            self.cur_x += self.WALK_DISTANCE
            self.cur_y += self.WALK_DISTANCE
            self.state = "walk_SE"

        elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_UP] and self.cur_x + self.WALK_DISTANCE + self.hitbox_x < SCREEN_WIDTH and self.cur_y - self.WALK_DISTANCE - self.hitbox_y > 0:   # Northeast
            self.cur_x += self.WALK_DISTANCE
            self.cur_y -= self.WALK_DISTANCE
            self.state = "walk_NE"

        elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_UP] and self.cur_x - self.WALK_DISTANCE - self.hitbox_x > 0 and self.cur_y - self.WALK_DISTANCE - self.hitbox_y > 0:   # Northwest
            self.cur_x -= self.WALK_DISTANCE
            self.cur_y -= self.WALK_DISTANCE
            self.state = "walk_NW"

        elif keys_pressed[pygame.K_RIGHT] and self.cur_x + self.WALK_DISTANCE + self.hitbox_x < SCREEN_WIDTH:  # EAST
            self.cur_x += self.WALK_DISTANCE
            self.state =  "walk_E"

        elif keys_pressed[pygame.K_UP] and self.cur_y - self.WALK_DISTANCE > 0:  # NORTH
            self.cur_y -= self.WALK_DISTANCE
            self.state = "walk_N"
            self.prev = keys_pressed

        elif keys_pressed[pygame.K_DOWN] and self.cur_y + self.WALK_DISTANCE + self.hitbox_y < SCREEN_HEIGHT:  # SOUTH
            self.cur_y += self.WALK_DISTANCE
            self.state = "walk_S"

        elif keys_pressed[pygame.K_LEFT] and self.cur_x - self.WALK_DISTANCE > 0:  # WEST
            self.cur_x -= self.WALK_DISTANCE
            self.state = "walk_W"
        
        else: 
            self.state = "IDLE"

    def draw(self, screen):
        screen.blit(self.image, (self.cur_x,self.cur_y))          # (surface, (x,y)) 

def main():

    pengy = penguin()
    clock = pygame.time.Clock()
    FPS = 25
    run = True 
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        SCREEN.fill((255,255,255))
        keys_pressed = pygame.key.get_pressed()


        if pengy.prev != keys_pressed:
            pengy.index = 0
        else:
            if pengy.index >= len(SPRITES[pengy.state])-1:
                pengy.index = 0
            else:
                pengy.index += 1

        pengy.handle_movement(keys_pressed)
        pengy.update_sprite()

        pengy.draw(SCREEN)
        clock.tick(FPS)
        pygame.display.update()

main()