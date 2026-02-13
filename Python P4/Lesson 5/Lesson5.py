import random
import pygame
import operator
from pygame.locals import *
Rect = pygame.Rect
import math

pygame.font.init()
pygame.mixer.init()

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
animationLoop2 = 0
animationLoop3 = 0

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

crash = [pygame.mixer.Sound('assets/crashSound.mp3'),
         pygame.mixer.Sound('assets/crashSound2.mp3'),
         pygame.mixer.Sound('assets/crashSound3.mp3'),]

save = pygame.mixer.Sound('assets/bonk.mp3')

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
        state = pygame.mouse.get_pressed()
        pygame.draw.rect(SURFACE, color, self.locations)
    
    def mouseHover(self):
        self.mousePos = pygame.mouse.get_pos()
        if self.mousePos[0] > 300 and self.mousePos[1] > 600 and self.mousePos[0] < 500 and self.mousePos[1] < 670:
            return True
        

class ball:
    def __init__(self, x, y):
        self.image = [pygame.image.load('assets/circle.png'),
                      pygame.image.load('assets/redCircle.png')]
        self.location = [x, y]
    
    def draw(self, height, width, animationLoop):
        self.image[animationLoop] = pygame.transform.scale(self.image[animationLoop], (width, height))
        SURFACE.blit(self.image[animationLoop], self.location)
pygame.display.set_caption("Lesson 2")

text = myText("Rage Italic", 80, False, False, 280, 300)
text2 = myText("Rage Italic", 40, False, False, 370, 620)
text3 = myText("Rage Italic", 40, False, False, 30, 30)
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
        if rectangle.mouseHover():
            rectangle.draw((255, 0, 0))
            text2.draw("Play", (0, 0, 0))
        if state == (True, False, False):
            if rectangle.mouseHover():
                GAMESTATE2 = 1
        animationLoop = animationLoop + 1
        SURFACE.blit(dinoImgs[animationLoop], (x, 400))
        x = x+10
        if x == 800:
            x = -50
        clock.tick(fps)
    if GAMESTATE2 == 1:
        SURFACE.fill((255, 255, 255))
        pressed = pygame.key.get_pressed()
        text3.draw("Score: " + str(score), (0, 0, 0))
        ballY = ballY + 10 + (score*5)

        # if event.type == pygame.KEYDOWN:
        #     moveLeft = False
        #     moveRight = False
        #     if pressed[pygame.K_RIGHT] == True:
        #         moveRight = True
        #     if pressed[pygame.K_LEFT] == True:
        #         moveLeft = True
        if ballState == False:
            ballX = random.randint(50, 750)
            ballState = True
        if pressed[pygame.K_RIGHT] and x < 700:
            SURFACE.blit(dinoImgs[animationLoop], (x, 600))
            x += 15 + (score*3)
            animationLoop = animationLoop + 1
        elif pressed[pygame.K_LEFT] and x > 0:
            SURFACE.blit(pygame.transform.flip(dinoImgs[animationLoop], True, False), (x, 600))
            x -= 15 + (score*3)
            animationLoop = animationLoop + 1
        else:
            SURFACE.blit(dinoImgs[animationLoop], (x, 600))
        if ballY > 570 and ballY < 800 and ballX+ballWidth > x and ballX < x+100:
            ballY = -150
            ballState = False
            score = score + 1
            save.play()
        if ballY > 850:
            crash[animationLoop3].play()
            animationLoop3 += 1
            ballState = False
            score = score - 1
            ballY = -150
        ball1 = ball(ballX, ballY)
        ball.draw(ball1, 60, 60, math.floor(animationLoop2))
        if ballY > 570:
            animationLoop2 += 0.4
        clock.tick(fps2)
        if score == 15:
            GAMESTATE2 = 2
        if score < 0:
            GAMESTATE2 = 3
    if GAMESTATE2 == 2:
        SURFACE.fill((255, 255, 255))
        text.draw("You win", (0, 255, 0))
        rectangle.draw((0, 255, 0))
        text2.draw("Restart", (0, 0, 0))
        if rectangle.mouseHover():
            rectangle.draw((255, 0, 0))
            text2.draw("Restart", (0, 0, 0))
        if state == (True, False, False):
            if rectangle.mouseHover():
                GAMESTATE2 = 1
                animationLoop = 0
                counter = 0
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
                animationLoop2 = 0
                animationLoop3 = 0
    if GAMESTATE2 == 3:
        mousePos = pygame.mouse.get_pos()
        state = pygame.mouse.get_pressed()
        SURFACE.fill((255, 255, 255))
        text.draw("You lose", (255, 0, 0))
        rectangle.draw((0, 255, 0))
        text2.draw("Restart", (0, 0, 0))
        if mousePos[0] > 300 and mousePos[1] > 600 and mousePos[0] < 500 and mousePos[1] < 670:
            rectangle.draw((255, 0, 0))
            text2.draw("Restart", (0, 0, 0))
        if state == (True, False, False):
            if mousePos[0] > 300 and mousePos[1] > 600 and mousePos[0] < 500 and mousePos[1] < 670:
                GAMESTATE2 = 0
                animationLoop = 0
                counter = 0
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
                animationLoop2 = 0
                animationLoop3 = 0
    if animationLoop == 7:
        animationLoop = 0
    if animationLoop2 == 2:
        animationLoop2 = 0      
    if animationLoop3 == 3:
        animationLoop3 = 0
 
    pygame.display.update()
    