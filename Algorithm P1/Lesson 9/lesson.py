import math
import copy

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

def minimax(board, player):
    if player == "O":
        for i in range(len(board)):
            print(board[i])
        x = int(input("Which x coordinate do you want to place 'O': "))-1
        y = int(input("Which y coordinate do you want to place 'O': "))-1
        board[y][x] = "O"
        counter = -10
        toPlay=[0,0]
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
            return 
        if winCondition(board,"X") == "win":
            for i in range(len(board)):
                print(board[i])
            print("AI Win")
            return
        minimax(board, "O")
    if player == "X":
        counter = -10
        toPlay=[0,0]
        for x in range(len(board)):
            for y in range(len(board)):
                if board[y][x] == " ":
                    temp = copy.deepcopy(board)
                    temp[y][x] = "O"
                    if possibleOutcome(temp, "X", "X", 0) > counter:
                        toPlay = [x,y]
        if selfWin(board, "X") != "none":
            toPlay = selfWin(board, "X")
        if selfWin(board, "O") != "none":
            toPlay = selfWin(board, "O")
        print("toplay", toPlay)
        board[toPlay[1]][toPlay[0]] = "O"
        for i in range(len(board)):
            print(board[i])
        x = int(input("Which x coordinate do you want to place 'X': "))-1
        y = int(input("Which y coordinate do you want to place 'X': "))-1
        board[y][x] = "X"
        minimax(board, "O")

minimax(board, "O")