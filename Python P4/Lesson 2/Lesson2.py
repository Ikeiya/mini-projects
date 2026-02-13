import pygame
from pygame.locals import *
Rect = pygame.Rect

pygame.font.init()

pygame.init()
GAMESTATE = True
SCREENSIZE = 800

SURFACE = pygame.display.set_mode(size=(SCREENSIZE, SCREENSIZE))
Rect1 = Rect(250, 400, 300, 200)

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

pygame.display.set_caption("Lesson 2")

text = myText("Rage Italic", 80, False, False, 300, 300)
text2 = myText("Rage Italic", 40, False, False, 370, 620)
rectangle = rectangleClass(300, 600, 200, 70)

while GAMESTATE:
    SURFACE.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMESTATE = False
    text.draw("Lesson 2", (0, 0, 0))
    rectangle.draw((0, 255, 0))
    text2.draw("Play", (0, 0, 0))
    pygame.display.update()