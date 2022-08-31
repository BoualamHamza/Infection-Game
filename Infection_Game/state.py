from settings import *
import random

class State():
	def __init__(self, board, currentPlayer):
		self.board = board
		self.currentPlayer = currentPlayer
		self.rs = 2
		self.bs = 2

	def getCurrentPlayer(self):
		return self.currentPlayer
		
	def isOver(self):
		for i, line in enumerate(self.board):
			if "0" in line:	return False
		return True

	def index_in_list(self, i):
		if i < len(self.board) and i >= 0:
			return True
		return False

	def getMove(self):
		possible_moves = []
		for i, line in enumerate(self.board):
			for j, char in enumerate(line):
				if char == self.currentPlayer:
					for dirx in range(-2, 3):
						for diry in range(-2, 3):
							if(self.index_in_list(i + dirx) and 
								self.index_in_list(j + diry)):
								if self.board[i + dirx][j + diry] == '0':
										possible_moves.append(((i,j), (i + dirx, j + diry)))
		return possible_moves

	def getScore(self, player):
		if player == "B": return self.bs / (self.bs + self.rs)
		if player == "R": return self.rs / (self.bs + self.rs)

	def play(self):
		randomMove = random.choice(self.getMove())
		target = randomMove[1]
		if self.isJump(randomMove):
			self.setPion(target[0], target[1], self.currentPlayer)
			self.setPion(randomMove[0][0], randomMove[0][1], "0")
		else:
			self.setPion(target[0], target[1], self.currentPlayer)
			if self.currentPlayer == "B": self.bs += 1
			else: self.rs += 1
		for x in range(-1, 2):
			for y in range(-1, 2):
				if(self.index_in_list(target[0] + x) and self.index_in_list(target[1] + y)):
					if self.currentPlayer == "R":
						if self.getPion(target[0] + x, target[1] + y) == "B":
							self.setPion(target[0] + x, target[1] + y, "R")
							self.bs -= 1
							self.rs += 1
					if self.currentPlayer == "B":
						if self.getPion(target[0] + x, target[1] + y) == "R":
							self.setPion(target[0] + x, target[1] + y, "B")
							self.bs += 1
							self.rs -= 1

		self.changePlayer()

	def changePlayer(self):
		if self.currentPlayer == "B":
			self.currentPlayer = "R"
		else:
			self.currentPlayer = "B"

	def getBoard(self):
		return self.board

	def setPion(self, x, y, player):
		line = self.board[x]
		self.board[x] = line[:y] + player + line[y + 1:]
	
	def getPion(self, x, y):
		return self.board[x][y]

	def isJump(self, move):
		# ((0, 0), (0, 2))
		if abs(move[1][0] - move[0][0]) > 1 or abs(move[1][1] - move[0][1]) > 1:
			return True
		return False