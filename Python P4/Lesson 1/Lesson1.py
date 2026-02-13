import pygame, sys
from pygame.locals import *

pygame.init()

GAMESTATE = True
SCREENSIZE = 800
RED = (255, 0, 0)
GREEN = (0, 214, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
flipped = "right"
colorList = [BLACK, RED, BLUE, GREEN]
colorIndex = 0
SURFACE = pygame.display.set_mode(size=(SCREENSIZE, SCREENSIZE))
pygame.display.set_caption("Catching Game")
character = pygame.image.load("character.png")

class Pikachu:
    def __init__(self, x, y, height, width, image):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = image
    def draw(self):
        SURFACE.blit(self.image, (self.x, self.y))

pokemon = Pikachu(170, 200, 230, 200, character)

while GAMESTATE:
    SURFACE.fill(colorList[colorIndex])
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_c:
                if colorIndex == 3:
                    colorIndex = 0
                else:
                    colorIndex += 1
                SURFACE.fill(colorList[colorIndex])
            # if event.key == K_UP and pokemon.y >= 20:
            #     pokemon.y -= 20
            # if event.key == K_DOWN and pokemon.y <= 780-pokemon.height:
            #     pokemon.y += 20
            # if event.key == K_LEFT and pokemon.x >= 20:
            #     pokemon.x -= 20
            # if event.key == K_RIGHT and pokemon.x <= 780-pokemon.width:
            #     pokemon.x += 20
        if event.type == pygame.QUIT:
            GAMESTATE = False

    keys = pygame.key.get_pressed()
    if keys[K_UP] and pokemon.y >= 20:
        pokemon.y -= 1
    if keys[K_DOWN] and pokemon.y <= 780-pokemon.height:
        pokemon.y += 1
    if keys[K_LEFT] and pokemon.x >= 20:
        if flipped == "left":
            pokemon.image = pygame.transform.flip(pokemon.image, True, False)
            print(pokemon.image)
            flipped = "right"
            pokemon.x += 75
        pokemon.x -= 1
    if keys[K_RIGHT] and pokemon.x <= 780-pokemon.width:
        if flipped == "right":
            pokemon.image = pygame.transform.flip(pokemon.image, True, False)
            flipped = "left"
            pokemon.x -= 75
        pokemon.x += 1
        

    pokemon.draw()
    pygame.display.update()