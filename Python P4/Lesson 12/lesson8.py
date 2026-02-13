import pygame, os
from pygame.locals import *
import math
import random

pygame.init()
pygame.font.init()

width = 1000
height = 800
SURFACE = pygame.display.set_mode((width, height))

currentDir = os.path.dirname(__file__)
wall = pygame.image.load("assets/wall.png")
road = pygame.image.load("assets/road.png")
pacmanImg = pygame.image.load("assets/pacman.png")
pointImg = pygame.image.load("assets/dot.png")
ghost1Img = pygame.image.load("assets/ghost1.png")
ghost2Img = pygame.image.load("assets/ghost2.png")
pillImg = pygame.image.load("assets/pill.png")
scoreText = pygame.display.set_caption('Show Text')
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

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

class ghost:
    def __init__(self, image):
        self.image = image
        self.x = 480
        self.y = 440
        self.direction = ["up", "down", "left", "right"]
        self.index = 0
        self.death = False
        self.counter = 0

    def draw(self):
        offset = 40
        self.counter += 1
        SURFACE.blit(self.image, (self.x, self.y))
        if self.x < 0:
            self.x = 0
        elif self.x > width:
            self.x = width-offset
        if self.y < 0:
            self.y = 0
        elif self.y > height:
            self.y = height-offset
        if self.death == True:
            self.x = 480
            self.y = 440

    def neutralPos(self, image):
        self.image = image
    
    def movement(self, speed, image):
        while self.counter > 30:
            left = globalMap[math.floor((self.y)/40)][math.floor((self.x)/40)-1] == "1"
            right = globalMap[math.floor((self.y)/40)][math.floor((self.x)/40)+1] == "1"
            up = globalMap[math.floor((self.y)/40)-1][math.floor((self.x)/40)] == "1"
            down = globalMap[math.floor((self.y)/40)+1][math.floor((self.x)/40)] == "1"
            if (up or down)and(left or right):
                self.index = random.randint(0, 3)
            if self.direction[self.index] == "left":
                if left:
                    self.x -= speed
                    self.neutralPos(image)
                    self.image = pygame.transform.flip(self.image, True, False)
                    break
            elif self.direction[self.index] == "right":
                if right:
                    self.x += speed
                    self.neutralPos(image)
                    break
            elif self.direction[self.index] == "up":
                if up:
                    self.y -= speed
                    break
            elif self.direction[self.index] == "down":
                if down:
                    self.y += speed
                    break
    
    def collisionCheck(self):
        if (self.x, self.y) == (x*40, y*40):
            if pillActive == False:
                global SCENE
                SCENE = 1
            else:
                self.x = 480
                self.y = 440
                self.counter = 0



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
            self.direction = "left"
        elif keyLog[K_RIGHT]:
            self.direction = "right"
        elif keyLog[K_UP]:
            self.direction = "up"
        elif keyLog[K_DOWN]:
            self.direction = "down"

        if self.direction == "left":
            if globalMap[math.floor((self.y)/40)][math.floor((self.x)/40)-1] == "1":
                self.x -= speed
                self.neutralPos(image)
                self.image = pygame.transform.flip(self.image, True, False)
        elif self.direction == "right":
            if globalMap[math.floor((self.y)/40)][math.floor((self.x)/40)+1] == "1":
                self.x += speed
                self.neutralPos(image)
        elif self.direction == "up":
            if globalMap[math.floor((self.y)/40)-1][math.floor((self.x)/40)] == "1":
                self.y -= speed
                self.neutralPos(image)
                self.image = pygame.transform.rotate(self.image, 90)
        elif self.direction == "down":
            if globalMap[math.floor((self.y)/40)+1][math.floor((self.x)/40)] == "1":
                self.y += speed
                self.neutralPos(image)
                self.image = pygame.transform.rotate(self.image, 270)
        global x, y
        x = math.floor((self.x)/40)
        y = math.floor((self.y)/40)

class pill:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.status = True
        self.counter = 0
    
    def draw(self):
        self.counter -= 1
        if self.status == True:
            SURFACE.blit(self.image, (self.x, self.y))
    
    def remove(self, x, y):
        if self.x == x*40 and self.y == y*40:
            global pillActive
            pillActive = True
            self.status = False
            self.x = 1000
            self.image = ("assets/road.png")
        if self.counter < 0:
            pillActive = False


class pointClass:
    def __init__(self, image, globalMap):
        self.image = image
        self.map = globalMap
        self.score = 0

    def draw(self):
        for i in range(len(self.map)):
            for index, j in enumerate(self.map[i]):
                if j == "1":
                    SURFACE.blit(self.image, (index*40+20, i*40+20))
    
    def remove(self, x, y):
        global score
        if self.map[y][x] == "1":
            self.map[y][x] = "0"
            self.score += 1
            score = self.score

class myText:
    def __init__(self, fontType, size, myBold, myItalic, x, y):
        self.myFont = pygame.font.SysFont(fontType, size, bold=myBold, italic=myItalic)
        self.x = x
        self.y = y
    def draw(self, randomText, color):
        SURFACE.blit(self.myFont.render(randomText, 0, color), (self.x, self.y))

class rectangleClass:
    def __init__(self, x, y, width, height):
        self.rect1 = pygame.Rect(x, y, width, height)
        self.locations = [x, y, width, height]

    def draw(self, color=(0, 0, 255)):
        pygame.draw.rect(SURFACE, color, self.locations)

def main():
    fps = 10
    clock = pygame.time.Clock()
    def update():
        SURFACE.fill(BLACK)
        text = font.render('Score is :' +str(score), True, (255, 255, 255))
        background.generate()
        pacman.movement(40, pacmanImg)
        pacman.draw()
        if counter > 30:
            ghost1.collisionCheck()
            ghost2.collisionCheck()
            ghost1.movement(40, ghost1Img)
            ghost2.movement(40, ghost2Img)  
        ghost1.draw()
        ghost2.draw()
        point.draw()
        pill1.remove(x, y)
        pill2.remove(x, y)
        pill1.draw()
        pill2.draw()
        point.remove(x, y)
        SURFACE.blit(text, (0,0))
    MAPLOCATION = []
    background = gameMap("assets/map.txt", wall, road)
    background.generate()
    point = pointClass(pointImg, globalMap)
    pacman = player(pacmanImg)
    ghost1 = ghost(ghost1Img)
    ghost2 = ghost(ghost2Img)
    pill1 = pill(pillImg, 80, 40)
    pill2 = pill(pillImg, 880, 40)
    counter = 0
    GAMESTATE = True
    global SCENE
    SCENE = 0
    text = myText("Rage Italic", 80, False, False, 375, 220)
    text2 = myText("Rage Italic", 80, False, False, 400, 510)
    rectangle = rectangleClass(400, 500, 200, 70)
    while GAMESTATE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAMESTATE = False
        if SCENE == 0:
            update()
            counter += 1
            clock.tick(fps)
        elif SCENE == 1:
            SURFACE.fill((0, 0, 0))
            state = pygame.mouse.get_pressed()
            mousePos = pygame.mouse.get_pos()
            text.draw("You Died", (255, 0, 0))
            rectangle.draw((0, 255, 0))
            text2.draw("Restart", (0, 0, 0))
            if state == (True, False, False):
                if mousePos[0] > 400 and mousePos[1] > 500 and mousePos[0] < 600 and mousePos[1] < 570:
                    SCENE = 0
                    GAMESTATE = False
                    main()
        pygame.display.update()

    



if __name__ == "__main__":
    main()