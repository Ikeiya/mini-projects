import math
import copy
import pygame

pygame.init()
screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
running = True

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def winCondition(board, player):
    for i in range(len(board)):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return "win"
        elif board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return "win"
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return "win"
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return "win"
        

def possibleOutcome(board, botPlay, player, points):
    if botPlay == "O":
        if winCondition(board, "O") == "win":
            return points+1
        elif winCondition(board, "X") == "win":
            return points-1
    if botPlay == "X":
        if winCondition(board, "X") == "win":
            return points+1
        elif winCondition(board, "O") == "win":
            return points-1
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == " ":
                board[y][x] = player
                if player == "O":
                    points = possibleOutcome(board, botPlay, "X", points)
                if botPlay == "X":
                    points = possibleOutcome(board, botPlay, "O", points)
    return points

def selfWin(board2, botPlay):
    temp = copy.deepcopy(board2)
    if botPlay == "O":
        for x in range(len(temp)):
            for y in range(len(temp)):
                if temp[y][x] == ' ':
                    temp[y][x] = "O"
                    if winCondition(temp, "O") == "win":
                        return [x,y]
                    temp[y][x] = ' '
        return "none"
    if botPlay == "X":
        for x in range(len(temp)):
            for y in range(len(temp)):
                if temp[y][x] == ' ':
                    temp[y][x] = "X"
                    if winCondition(temp, "X") == "win":
                        return [x,y]
                    temp[y][x] = ' '
        return "none"

def minimax(board, player, x, y):
    if player == "O" and x != -1 and board[y][x] == " ":
        for i in range(len(board)):
            print(board[i])
        board[y][x] = "O"
        counter = -10
        toPlay=[0,0]
        if winCondition(board,"O") == "win":
            for i in range(len(board)):
                print(board[i])
                print("Player Win")
            for i in range(5000):
                screen.fill((255, 255, 255))
                text_surface = my_font.render('Player Win', False, (0, 0, 0))
                screen.blit(text_surface, (200,230))
                pygame.display.flip()
            return
        if winCondition(board,"X") == "win":
            for i in range(len(board)):
                print(board[i])
            for i in range(5000):
                screen.fill((255, 255, 255))
                text_surface = my_font.render('AI win', False, (0, 0, 0))
                screen.blit(text_surface, (200, 230))
                pygame.display.flip()
            return
        elif " " in board[0] or " " in board[1] or " " in board[2]:
            print("filler")
        else:
            for i in range(5000):
                screen.fill((255, 255, 255))
                text_surface = my_font.render('Draw', False, (0, 0, 0))
                screen.blit(text_surface, (200, 240))
                pygame.display.flip()
            return
        for x in range(len(board)):
            for y in range(len(board)):
                if board[y][x] == " ":
                    temp = copy.deepcopy(board)
                    temp[y][x] = "X"
                    if possibleOutcome(temp, "O", "O", 0) > counter:
                        toPlay = [x,y]
        if selfWin(board, "O") != "none":
            toPlay = selfWin(board, "O")
        if selfWin(board, "X") != "none":
            toPlay = selfWin(board, "X")
        board[toPlay[1]][toPlay[0]] = "X"
        if winCondition(board,"O") == "win":
            for i in range(len(board)):
                print(board[i])
            print("Player Win")
            for i in range(5000):
                screen.fill((255, 255, 255))
                text_surface = my_font.render('Player Win', False, (0, 0, 0))
                screen.blit(text_surface, (200,230))
                pygame.display.flip()
            return
        if winCondition(board,"X") == "win":
            for i in range(len(board)):
                print(board[i])
            for i in range(5000):
                screen.fill((255, 255, 255))
                text_surface = my_font.render('AI win', False, (0, 0, 0))
                screen.blit(text_surface, (200, 230))
                pygame.display.flip()
            return
        return board
    elif " " in board[0] or " " in board[1] or " " in board[2]:
        return board
    else:
        for i in range(5000):
                screen.fill((255, 255, 255))
                text_surface = my_font.render('Draw', False, (0, 0, 0))
                screen.blit(text_surface, (200, 240))
                pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    board = minimax(board, "O", -1, -1)

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if pos[0] < 160:
            x = 0
        elif pos[0] > 320:
            x = 2
        else:
            x = 1
        if pos[1] < 160:
            y = 0
        elif pos[1] > 320:
            y = 2
        else:
            y = 1
        board = minimax(board, "O", x, y)
        print(board)
    screen.fill("white")
    circle = pygame.image.load("circle.png")
    cross = pygame.image.load("cross.png")

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[j][i] == "O":
                screen.blit(circle, (i*160+10, j*160+10))
            if board[j][i] == "X":
                screen.blit(cross, (i*160+10, j*160+10))

    grid = pygame.image.load("grid.png")
    screen.blit(grid, (0,0))
    pygame.display.flip()
    
    clock.tick(60)