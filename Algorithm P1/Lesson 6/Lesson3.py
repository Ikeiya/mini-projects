import random

vertical = int(input("Input vertical height of maze: "))
horizontal = int(input("Input horizontal length of maze: "))

maze = [[1 for x in range(horizontal+2)] for y in range(vertical+2)]

print(maze, horizontal, vertical)

maze[1][0] = "S"
maze[vertical][horizontal+1] = "E"
path = True

def changeDirection():
    return random.randint(0,3)

def checkBoundaries(direction, maze, x, y):
    if direction == 0:
        if y-1 != 0 and maze[y-2][x] != 0 and maze[y-1][x-1] != 0 and maze[y-1][x+1] != 0:
            return True
        else:
            return False
    elif direction == 1:
        if x != horizontal and maze[y][x+2] != 0 and maze[y-1][x+1] != 0 and maze[y+1][x+1] != 0:
            if maze[y][x+2] != 0:
                return True
            else:
                return False
    elif direction == 2:
        if y != vertical:
            if maze[y+2][x] != 0 and maze[y+2][x] != 0 and maze[y+1][x+1] != 0  and maze[y+1][x-1] != 0:
                return True
            else:
                return False
    else:
        if x-1 != 0 and maze[y][x-2] != 0 and maze[y][x-2] != 0 and maze[y+1][x-1] != 0 and maze[y-1][x-1] != 0:
            return True
        else:
            return False

def replaceRoad(direction, maze, x, y):
    if direction == 0:
        y = y-1
    elif direction == 1:
        x = x+1
    elif direction == 2:
        y = y+1
    else:
        x = x-1
    maze[y][x] = 0
    return [maze,x,y]

list = [maze, 0, 1]
counter = 0
counter2 = 0
direction = 1

while path:
    if random.randint(1,2) == 2 and counter > 1:
        direction = changeDirection()
        counter = 0 
    if checkBoundaries(direction, list[0], list[1], list[2]):
        list = replaceRoad(direction, list[0], list[1], list[2])
    else:
        direction = changeDirection()
        counter = 0 
    counter = counter+1
    counter2 = counter2+1
    if list[1] == horizontal and list[2] == vertical:
        print("end")
        break
    if counter2 == 40000:
        maze = [[1 for x in range(horizontal+2)] for y in range(vertical+2)]
        maze[1][0] = "S"
        maze[vertical][horizontal+1] = "E"
        counter2 = 0
        direction = 1
        list = [maze, 0, 1]
        print("fail")


file = open('maze.txt','w')
for row in list[0]:
    file.write(''.join(str(x) for x in row)+"\n")
file.close
print("end2")


            


file = open('maze.txt','w')
for row in list[0]:
    file.write(''.join(str(x) for x in row)+"\n")
file.close