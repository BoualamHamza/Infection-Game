import pygame
from settings import *
from state import State

class Game():
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption(SCREEN_NAME)
		self.clock = pygame.time.Clock()
		self.running = True
		pygame.font.init()
		self.state = State(BOARD, "B")

	def run(self):
		self.screen.fill((255, 255, 255))
		self.clock.tick(FPS)
		self.get_events()
		self.draw_board()
		if not self.state.isOver(): self.state.play()
		else:
			font = pygame.font.SysFont('sans-serif', 128)
			if self.state.bs > self.state.rs:
				img = font.render('Bleu a gagné !', True, (0, 0, 0))
			else:
				img = font.render('Rouge a gagné !', True, (0, 0, 0))
			self.screen.blit(img, (SCREEN_WIDTH / 2 - img.get_width() / 2, SCREEN_HEIGHT / 2 - img.get_height() / 2))
			pygame.display.set_caption(SCREEN_NAME + " - Scores (R/B): " + str(round(self.state.getScore("R"), 3)) + "/" + str(round(self.state.getScore("B"), 3)))
		pygame.display.flip()

	def get_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def draw_board(self):
		for i, line in enumerate(BOARD):
			for j, char in enumerate(line):
				color = (255, 255, 255)
				if char == "0":
					color = (255, 255, 255)
				elif char == "B":
					color = (0, 0, 255)
				elif char == "R":
					color = (255, 0, 0)
				pygame.draw.circle(self.screen, color, [i*CELL_SIZE + CELL_SIZE / 2, j*CELL_SIZE + CELL_SIZE / 2], CELL_SIZE / 2.2)
				pygame.draw.line(self.screen, (0, 0, 0), (i*CELL_SIZE, j*CELL_SIZE), (i*CELL_SIZE + CELL_SIZE, j*CELL_SIZE), 1)
				pygame.draw.line(self.screen, (0, 0, 0), (i*CELL_SIZE, j*CELL_SIZE), (i*CELL_SIZE, j*CELL_SIZE + CELL_SIZE), 1)