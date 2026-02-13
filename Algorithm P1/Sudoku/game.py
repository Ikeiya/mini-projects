import math
import pygame

pygame.init()
screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 53)
running = True
x = -1
y = -1

def checkValid(reference, board, x, y):
    for i in range(len(board)):
        if board[y][x] == reference[i][x] or board[y][x] == board[i][x] and i != y:
            print("1")
            return False
        if board[y][x] == reference[y][i] or board[y][x] == board[y][i] and i != x:
            print("2")
            return False
    for i in range(3):
        for j in range(3):
            if board[y][x] == reference[math.floor((y+1)/3)*3+i][math.floor((x+1)/3)*3+j] or board[y][x] == board[math.floor((y+1)/3)*3+i][math.floor((x+1)/3)*3+j] and y != math.floor((y+1)/3)*3+i and x != math.floor((x+1)/3)*3+j:
                print("3")
                return False
    return True

reference = [['5','3',' ',' ','7',' ',' ',' ',' '],
         ['6',' ',' ','1','9','5',' ',' ',' '],
         [' ','9','8',' ',' ',' ',' ','6',' '],
         ['8',' ',' ',' ','6',' ',' ',' ','3'],
         ['4',' ',' ','8',' ','3',' ',' ','1'],
         ['7',' ',' ',' ','2',' ',' ',' ','6'],
         [' ','6',' ',' ',' ',' ','2','8',' '],
         [' ',' ',' ','4','1','9',' ',' ','5'],
         [' ',' ',' ',' ','8',' ',' ','7','9']]

board = [[' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' ',' ']]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if x >= 0:
                if event.key == pygame.K_1:
                    board[y][x] = "1"
                if event.key == pygame.K_2:
                    board[y][x] = "2"
                if event.key == pygame.K_3:
                    board[y][x] = "3"
                if event.key == pygame.K_4:
                    board[y][x] = "4"
                if event.key == pygame.K_5:
                    board[y][x] = "5"
                if event.key == pygame.K_6:
                    board[y][x] = "6"
                if event.key == pygame.K_7:
                    board[y][x] = "7"
                if event.key == pygame.K_8:
                    board[y][x] = "8"
                if event.key == pygame.K_9:
                    board[y][x] = "9"
                x = -1
                y = -1
    if reference[y][x] != " ":
        x = -1
        y = -1
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if pos[0] < 53:
            x = 0
        elif pos[0] < 107:
            x = 1
        elif pos[0] < 160:
            x = 2
        elif pos[0] < 213:
            x = 3
        elif pos[0] < 257:
            x = 4
        elif pos[0] < 310:
            x = 5
        elif pos[0] < 363:
            x = 6
        elif pos[0] < 416:
            x = 7
        else:
            x = 8

        if pos[1] < 53:
            y = 0
        elif pos[1] < 107:
            y = 1
        elif pos[1] < 160:
            y = 2
        elif pos[1] < 213:
            y = 3
        elif pos[1] < 257:
            y = 4
        elif pos[1] < 310:
            y = 5
        elif pos[1] < 363:
            y = 6
        elif pos[1] < 416:
            y = 7
        else:
            y = 8   
        
    grid = pygame.image.load("puzzle.jpg")
    screen.blit(grid, (0,0))
    for i in range(9):
        for j in range(9):
            if board[j][i] != " ":
                if checkValid(reference, board, i, j) == False:
                    label = myfont.render(board[j][i], False, (255, 0, 0))
                elif checkValid(reference, board, i, j) == True:
                    label = myfont.render(board[j][i], False, (0, 255, 0))
                screen.blit(label, (round(53*i+10), round(53*j-10)))

    pygame.display.flip()
    clock.tick(60)