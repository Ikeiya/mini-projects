import pygame, os
from pygame.locals import *
import numpy as np

pygame.init()
pygame.font.init()

width = 1000
height = 800
SURFACE = pygame.display.set_mode((width, height))

currentDir = os.path.dirname(__file__)
wall = pygame.image.load("assets/wall.png")
road = pygame.image.load("assets/road.png")
pacmanImg = pygame.image.load("assets/pacman.png")
BLACK = (0, 0, 0)

GAMEMAP = []


class gameMap:
    global currentDir, GAMEMAP
    def __init__(self, src, *image):
        self.src = os.path.join(currentDir, src)
        self.image = image
        self.x = 0
        self.y = 0
    
    def generate(self):
        global globalMap, globalMapLocation
        with open(self.src, "r") as map:
            for i in map.readlines():
                GAMEMAP.append(i.split())
        for roadNum in range(len(GAMEMAP)):
            for element in GAMEMAP[roadNum]:
                SURFACE.blit(self.image[int(element)], (self.x, self.y))
                self.x += 40
            self.x = 0
            if roadNum == len(GAMEMAP)-1:
                self.y = 0
            else:
                self.y += 40
        globalMap = GAMEMAP.copy()
        MAPLOCATION = []
        for i in range(len(GAMEMAP)):
            MAPLOCATION.append([])
            for i in range(len(MAPLOCATION)):
                for j in range(len(GAMEMAP[i])):
                    MAPLOCATION[i].append((i*40, j*40))
        globalMapLocation = MAPLOCATION.copy()
        GAMEMAP.clear()
        MAPLOCATION.clear()
        
class player:
    def __init__(self, image):
        self.image = image
        self.x = 480
        self.y = 400
        self.direction = "none"
    
    def draw(self):
        offset = 40
        SURFACE.blit(self.image, (self.x, self.y))
        if self.x < 0:
            self.x = 0
        elif self.x > width:
            self.x = width-offset
        if self.y < 0:
            self.y = 0
        elif self.y > height:
            self.y = height-offset
    
    def neutralPos(self, image):
        self.image = image

    def movement(self, speed, image):
        keyLog = pygame.key.get_pressed()
        if keyLog[K_LEFT]:
            for i in range(len(globalMapLocation)):
                try:
                    index = globalMapLocation[i].index(((self.x//40)*40, (self.y//40)*40))
                    index = (i, index)
                except:
                    continue
            if GAMEMAP[index[0]][index[1]] == "0":
                self.direction = "left"
        elif keyLog[K_RIGHT]:
            self.direction = "right"
        elif keyLog[K_UP]:
            self.direction = "up"
        elif keyLog[K_DOWN]:
            self.direction = "down"

        if self.direction == "left":
            self.x -= speed
            self.neutralPos(image)
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.direction == "right":
            self.x += speed
            self.neutralPos(image)
        elif self.direction == "up":
            self.y -= speed
            self.neutralPos(image)
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.direction == "down":
            self.y += speed
            self.neutralPos(image)
            self.image = pygame.transform.rotate(self.image, 270)
        

def main():
    fps = 30
    clock = pygame.time.Clock()
    def update():
        SURFACE.fill(BLACK)
        background.generate()
        pacman.draw()
        pacman.movement(6, pacmanImg)
        pygame.display.update()
    MAPLOCATION = []
    background = gameMap("assets/map.txt", wall, road)
    pacman = player(pacmanImg)
    GAMESTATE = True
    while GAMESTATE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMESTATE = False
        update()
        clock.tick(fps)



if __name__ == "__main__":
    main()