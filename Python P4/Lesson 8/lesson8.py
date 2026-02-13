import pygame, os
from pygame.locals import *

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
        GAMEMAP.clear()
        
class player:
    def __init__(self, image):
        self.image = image
        self.x = 480
        self.y = 400
    
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
    
    def movement(self, speed):
        keyLog = pygame.key.get_pressed()
        if keyLog[K_LEFT]:
            self.x -= speed
        elif keyLog[K_RIGHT]:
            self.x += speed
        elif keyLog[K_UP]:
            self.y -= speed
        elif keyLog[K_DOWN]:
            self.y += speed
        

def main():
    fps = 10
    clock = pygame.time.Clock()
    def update():
        SURFACE.fill(BLACK)
        background.generate()
        pacman.draw()
        pacman.movement(4)
        pygame.display.update()
    background = gameMap("assets/map.txt", wall, road)
    pacman = player(pacmanImg)
    GAMESTATE = True
    while GAMESTATE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMESTATE = False
        update()
        


if __name__ == "__main__":
    main()