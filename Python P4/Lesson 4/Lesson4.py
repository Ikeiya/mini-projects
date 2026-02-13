import random
import pygame
import operator
from pygame.locals import *
Rect = pygame.Rect

pygame.font.init()

pygame.init()
GAMESTATE = True
GAMESTATE2 = 0
SCREENSIZE = 800
animationLoop = 0
counter = 0
clock = pygame.time.Clock()
x = -50
ballX = 0
ballY = 0
ballState = False
ballHeight = 60
ballWidth = 60
fps = 10
fps2 = 20
moveRight = False
moveLeft = False
score = 0

SURFACE = pygame.display.set_mode(size=(SCREENSIZE, SCREENSIZE))
Rect1 = Rect(250, 400, 300, 200)

dinoImgs = [pygame.image.load('assets/animationDino/tile003.png'),
            pygame.image.load('assets/animationDino/tile004.png'),
            pygame.image.load('assets/animationDino/tile005.png'),
            pygame.image.load('assets/animationDino/tile006.png'),
            pygame.image.load('assets/animationDino/tile007.png'),
            pygame.image.load('assets/animationDino/tile008.png'),
            pygame.image.load('assets/animationDino/tile009.png'),
            pygame.image.load('assets/animationDino/tile010.png')
]
myFont = pygame.font.SysFont("Rage Italic", 80, bold=False, italic=False)

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

class ball:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/circle.png')
        self.location = [x, y]
    
    def draw(self, height, width):
        self.image = pygame.image.load('assets/circle.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        SURFACE.blit(self.image, self.location)
pygame.display.set_caption("Lesson 2")

text = myText("Rage Italic", 80, False, False, 280, 300)
text2 = myText("Rage Italic", 40, False, False, 370, 620)
rectangle = rectangleClass(300, 600, 200, 70)

while GAMESTATE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMESTATE = False
    if GAMESTATE2 == 0:
        SURFACE.fill((255, 255, 255))
        mousePos = pygame.mouse.get_pos()
        text.draw("Lesson 2", (0, 0, 0))
        rectangle.draw((0, 255, 0))
        text2.draw("Play", (0, 0, 0))
        state = pygame.mouse.get_pressed()
        if mousePos[0] > 300 and mousePos[1] > 600 and mousePos[0] < 500 and mousePos[1] < 670:
            rectangle.draw((255, 0, 0))
            text2.draw("Play", (0, 0, 0))
        if state == (True, False, False):
            if mousePos[0] > 300 and mousePos[1] > 600 and mousePos[0] < 500 and mousePos[1] < 670:
                GAMESTATE2 = 1
        animationLoop = animationLoop + 1
        SURFACE.blit(dinoImgs[animationLoop], (x, 400))
        x = x+10
        if x == 800:
            x = -50
        clock.tick(fps)
    if GAMESTATE2 == 1:
        text3 = myText("Rage Italic", 40, False, False, 370, 620)
        text3.draw(str(score), (0, 0, 0))
        SURFACE.fill((255, 255, 255))
        pressed = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            moveLeft = False
            moveRight = False
            if pressed[pygame.K_RIGHT] == True:
                moveRight = True
            if pressed[pygame.K_LEFT] == True:
                moveLeft = True
        if ballState == False:
            ballX = random.randint(50, 750)
            ballState = True
        if moveRight and x < 700:
            SURFACE.blit(dinoImgs[animationLoop], (x, 600))
            x = x + 15
            animationLoop = animationLoop + 1
        elif moveLeft and x > 0:
            SURFACE.blit(pygame.transform.flip(dinoImgs[animationLoop], True, False), (x, 600))
            x = x - 15
            animationLoop = animationLoop + 1
        else:
            SURFACE.blit(dinoImgs[animationLoop], (x, 600))
        
        if ballY > 570 and ballX+ballWidth > x and ballX < x+100:
            ballY = -150
            ballState = False
            score = score + 1
            print("Work")
        elif ballY>900:
            ballState = False
        ball1 = ball(ballX, ballY)
        ball.draw(ball1, 60, 60)
        ballY = ballY + 10
        clock.tick(fps2)
        
    if animationLoop == 7:
        animationLoop = 0      
    pygame.display.update()