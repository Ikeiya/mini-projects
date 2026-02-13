import random
import pygame
from pygame.locals import *


pygame.init()
pygame.font.init()

GAMESTATE = True
GAMESTATE2 = 0
oldCommand = "Non existent"
newCommand = "None"
clock = pygame.time.Clock()
fps = 50


SURFACE = pygame.display.set_mode(size=(544, 480))

class snake:
    def __init__(self, x, y):
        self.rect1 = pygame.Rect(x, y, 32, 32)
        self.x = x
        self.y = y
    
    def draw(self, color=(0, 153, 51)):
        pygame.draw.rect(SURFACE, color, [self.x, self.y, 32, 32])
    
    def movement(self, newCommand):
        if newCommand == "right":
            self.x += 4
        elif newCommand == "left":
            self.x -= 4
        elif newCommand == "up":
            self.y -= 4
        elif newCommand == "down":
            self.y += 4
        

snake1 = snake(234, 170)
background = pygame.image.load('assets/background.jpg')

while GAMESTATE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMESTATE = False
    if GAMESTATE2 == 0:
        pressed = pygame.key.get_pressed()        
        SURFACE.blit(background, (0, 0))
        if pressed[pygame.K_RIGHT] == 1 and snake1.x < 512:
            if oldCommand != "left":
                newCommand = "right"
        elif pressed[pygame.K_LEFT] == 1 and snake1.x > 0:
            if oldCommand != "right":
                newCommand = "left"
        elif pressed[pygame.K_UP] == 1 and snake1.y > 0:
            if oldCommand != "down":
                newCommand = "up"
        elif pressed[pygame.K_DOWN] == 1 and snake1.y < 480:
            if oldCommand != "up":
                newCommand = "down"
        
        print(snake1.x%32 == 10, newCommand)
        if snake1.x%32 == 10 and snake1.y%32 == 10 and newCommand != "None":
            oldCommand = newCommand
            newCommand = "None"
        snake1.movement(oldCommand)
        snake1.draw()
        clock.tick(fps)
    pygame.display.update()