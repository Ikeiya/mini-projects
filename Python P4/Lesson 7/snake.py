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
score = 0
oldLocation = [(160, 224), (160, 224)]
new = False

SURFACE = pygame.display.set_mode(size=(542, 477))

class snake:
    def __init__(self, x, y):
        self.rect1 = pygame.Rect(x, y, 32, 32)
        self.x = x
        self.y = y
    

    def draw(self, oldLocation, color=(0, 153, 51)):
        tempx = self.x
        tempy = self.y
        for i in range(len(oldLocation)-1):
            print(oldLocation)
            pygame.draw.rect(SURFACE, color, [oldLocation[i][0], oldLocation[i][1], 32, 32])
            
    def movement(self, newCommand):
        if newCommand == "right":
            self.x += 4
        elif newCommand == "left":
            self.x -= 4
        elif newCommand == "up":
            self.y -= 4
        elif newCommand == "down":
            self.y += 4
        
class apple:
    def __init__(self, x, y):
        self.rect1 = pygame.Rect(x, y, 32, 32)
        self.x = x
        self.y = y

    def draw(self):
        SURFACE.blit(pygame.image.load('assets/apple.png'), (self.x, self.y))
        
    def collision(self, x, y):
        print("haha")
    
snake1 = snake(160, 224)
apple1 = apple(310, 212)
background = pygame.image.load('assets/background.jpg')

while GAMESTATE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMESTATE = False
    if GAMESTATE2 == 0:
        pressed = pygame.key.get_pressed()
        SURFACE.blit(background, (0, 0))
        if pressed[pygame.K_RIGHT] == 1 and snake1.x < 526:
            if oldCommand != "left":
                newCommand = "right"
        elif pressed[pygame.K_LEFT] == 1 and snake1.x > 16:
            if oldCommand != "right":
                newCommand = "left"
        elif pressed[pygame.K_UP] == 1 and snake1.y > 16:
            if oldCommand != "down":
                newCommand = "up"
        elif pressed[pygame.K_DOWN] == 1 and snake1.y < 461:
            if oldCommand != "up":
                newCommand = "down"
        if snake1.x%32 == 0 and snake1.y%32 == 0 and newCommand != "none":
            oldCommand = newCommand
            newCommand = "none"
        oldLocation.append((snake1.x, snake1.y))
        oldLocation.pop(0)
        if snake1.x == apple1.x+10 and snake1.y == apple1.y+12:
            apple1 = apple(random.randint(0, 15)*32+22, random.randint(0, 13)*32+20)
            new = True
            score += 1
            tempx = snake1.x
            tempy = snake1.y
            counter = 0
        if new:
            counter += 1
        print(oldLocation)
        snake1.movement(oldCommand)
        apple1.draw()
        snake1.draw(oldLocation)
        clock.tick(fps)
    pygame.display.update()