import pygame
from enum import Enum 


FPS = 60
CELL_SIZE = 50


class Cell(Enum):
	VOID = 0
	CROSS = 1
	ZERO = 2






class Player:
	'''
	Класс игрока, содержащий тип значков и имя.
	'''
	def __init__(self, name, cell_type):
		self.name = name
		self.cell_type = cell_type
	pass

class GameField:
	def __init__(self):
		self.height = 3
		self.width = 3
		self.cells = [[Cell.VOID]*self.height for i in range(self.width)]


class GameFieldView:
	"""
	Game field widget which display the field and
	find out the place of the click
	"""
	def __init__(self, field):
	#load images of cell's sign	
	#display the initial state of the field
		self._field = field
		self._height = field.height + CELL_SIZE
		self._width = field.width + CELL_SIZE


	def draw(self):
		pass

	def check_coords_correct(self, x, y):
		return True # TODO: self._height  учесть

	def get_coords(self, x, y):
		return 0, 0 # TODO:  реально вычислить клетку клика




class GameRoundManager:
	'''
	Менеджер игры, запускающий все процессы.
	'''
	def __init__(self, player1: Player, player2: Player):
		self._players = [player1, player2]
		self._current_player = 0
		self.field = GameField()	

	def handle_click(self, i, j):
		player = self._players[self._current_player]
			# Игрок делает клик на поле. 
		print("click_handled", i, j)


class GameWndow:
	"""
	Содержит виджет поля,
	а также менеджер игрового раунда.
	"""
	def __init__(self):
		# Иициальзация pygame
		pygame.init()
		self._width = 800
		self._height = 600
		self._title = "Cross & Zeroes"
		self._screen = pygame.display.set_mode((self._width, self._height))
		pygame.display.set_caption(self._title)

		player1 = Player('Петя', Cell.CROSS)
		player2 = Player('Вася', Cell.ZERO)
		self._game_manger = GameRoundManager(player1, player2)
		self._field_widget = GameFieldView(self._game_manger.field)

	def main_loop(self):
		finished = False
		clock = pygame.time.Clock()
		while not finished:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					finished = True	
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = pygame.mouse.get_pos()
					x, y = mouse_pos
					if self._field_widget.check_coords_correct(x, y):
						i, j = self._field_widget.get_coords(x, y)
						self._game_manger.handle_click(i, j)
			pygame.display.flip()
			clock.tick(FPS)			

def main():
	window = GameWndow()
	window.main_loop()
	print('Game Over')

if __name__ == "__main__":
	main()	

