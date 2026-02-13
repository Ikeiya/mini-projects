import pygame, time, random, sys
sys.setrecursionlimit(1000)


class Maze():
	# fileName = maze file
	# gridSize = size for each cells
	def __init__(self, fileName, colors={}, gridSize=30, FPS=15):
		pygame.init()
		self.running = True
		self.gameScreen = None
		self.mazeData = []
		self.mazeSize = (0,0)
		self.FPS = FPS
		self.fpsClock = pygame.time.Clock()
		self.fileName = fileName
		self.colors = colors
		self.gridSize = gridSize

		self.updateMap()
		self.gameScreen = pygame.display.set_mode((self.mazeSize[1]*self.gridSize, self.mazeSize[0]*self.gridSize))

	# Internal use: update the maze with the updated file content
	def updateMap(self):
		with open(self.fileName) as fo:
			self.mazeData = fo.readlines()
		mazeWidth = 0
		for i in range(len(self.mazeData)-1, -1, -1):
			if self.mazeData[i][-1] == "\n":
				self.mazeData[i] = self.mazeData[i][:-1]
			self.mazeData[i] = list(self.mazeData[i])
			mazeWidth = max(mazeWidth, len(self.mazeData[i]))
			if len(self.mazeData[i]) == 0:
				self.mazeData.pop(i)
		self.mazeSize = (len(self.mazeData), mazeWidth)

	# Find all coordinates for the target symbol
	def findCell(self, target):
		result = []
		for i, row in enumerate(self.mazeData):
			for j, mazeCell in enumerate(row):
				if mazeCell == target:
					result.append((i, j))
		return result

	# Update the specified cell
	def setCell(self, i, j, update):
		self.mazeData[i][j] = update

	# Obtain the specified cell
	def getCell(self, i, j):
		return self.mazeData[i][j]

	# Obtain all the neighbors (coordinates and value) for a specified cell
	def getNeighbors(self, i, j, diagonal = False):
		result = []
		if i > 0:
			result.append((i-1, j, self.mazeData[i-1][j]))
		if j > 0:
			result.append((i, j-1, self.mazeData[i][j-1]))
		if i < self.mazeSize[0]-1:
			result.append((i+1, j, self.mazeData[i+1][j]))
		if j < self.mazeSize[1]-1:
			result.append((i, j+1, self.mazeData[i][j+1]))
		if diagonal:
			if i>0:
				if j>0:
					result.append((i-1, j-1, self.mazeData[i-1][j-1]))
				if j<self.mazeSize[1]-1:
					result.append((i-1, j+1, self.mazeData[i-1][j+1]))
			if i<self.mazeSize[0]-1:
				if j>0:
					result.append((i+1, j-1, self.mazeData[i+1][j-1]))
				if j<self.mazeSize[1]-1:
					result.append((i+1, j+1, self.mazeData[i+1][j+1]))
		return result

	# Internal use: the drawing steps for the whole map
	def drawMaze(self):
		for i in range(self.mazeSize[0]):
			for j in range(self.mazeSize[1]):
				cell = self.mazeData[i][j]
				if cell in self.colors:
					pygame.draw.rect(self.gameScreen, self.colors[cell], pygame.Rect(j*self.gridSize,i*self.gridSize,self.gridSize,self.gridSize))
				else:
					pass

	# Show the maze using pygame surfaces
	# Use self.running to check if the pygame surface is closed already
	def show(self):
		if self.gameScreen != None:
			pygame.display.update()
			self.drawMaze()
			self.fpsClock.tick(self.FPS)
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					quit = True
					del self.gameScreen
					self.gameScreen = None
					self.running = False
					pygame.display.quit()
					break

# Example
if __name__ == "__main__":
	colors = {	# The corresponding color for each symbol (example)
		" ": "#008000", # Road
		"S": "#008000", # Starting Point
		"E": "#008000", # Ending Point
		"0": "#404040", # Wall
		"V": "#808000", # Visited Cells
		"C": "#800000"  # Currently in the stack/queue
	}
	maze = Maze("mazeD0.txt", colors, gridSize=30, FPS=10)
	def nodeCheck(maze, path, coordinate):
		temp = []
		if maze[coordinate[1]+1][coordinate[0]] == ' ' and [coordinate[0],coordinate[1]+1] not in path:
			temp.append([coordinate[0],coordinate[1]+1])
		if maze[coordinate[1]-1][coordinate[0]] == ' ' and [coordinate[0],coordinate[1]-1] not in path:
			temp.append([coordinate[0],coordinate[1]-1])
		if maze[coordinate[1]][coordinate[0]+1] == ' ' and [coordinate[0]+1,coordinate[1]] not in path:
			temp.append([coordinate[0]+1,coordinate[1]])
		if maze[coordinate[1]][coordinate[0]-1] == ' ' and [coordinate[0]-1,coordinate[1]] not in path:
			temp.append([coordinate[0]-1,coordinate[1]])
		if maze[coordinate[1]+1][coordinate[0]] == 'E':
			return ["found", maze[coordinate[0]][coordinate[1]+1]]
		if maze[coordinate[1]-1][coordinate[0]] == 'E':
			return ["found", maze[coordinate[0]][coordinate[1]-1]]
		if maze[coordinate[1]][coordinate[0]+1] == 'E':
			return ["found", maze[coordinate[0]+1][coordinate[1]]]
		if maze[coordinate[1]][coordinate[0]-1] == 'E':
			return ["found", maze[coordinate[0]-1][coordinate[1]]]
		return temp

	def pathfinder(maze, path, coordinate):
		result = nodeCheck(maze, path, coordinate)
		for i in range(len(result)):
			if result[0] == "found":
				print('jjj')
				return path
			path.append(result[i])
			print("r")
			pathfinder(maze, path, result[i])
	start = [maze.findCell("S")[0][1],maze.findCell("S")[0][0]]
	path = pathfinder(maze.mazeData, [start], start)
	print("2",path)
	# while maze.running:
	# 	maze.show() # Show the current maze status

		# if random.randrange(10) <= 5:

		# 	# Make a random non-wall cell into "C"
		# 	i, j = random.randrange(maze.mazeSize[0]), random.randrange(maze.mazeSize[1])
		# 	if maze.getCell(i,j) != "0":
		# 		maze.setCell(i,j,"C")

		# 		# Make nearby non-wall cells into "V"
		# 		for m, n, cell in maze.getNeighbors(i,j):
		# 			if cell != "0":
		# 				maze.setCell(m,n,"V")

