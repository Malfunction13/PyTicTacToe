class Board:
	def __init__(self, p1, p2):
		self.cells = [0 for _ in range(9)]
		self.player1 = p1
		self.player2 = p2