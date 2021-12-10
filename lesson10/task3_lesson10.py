class Cell:
	def __init__(self, cells):
		self.cells = cells
	def __add__(self, other):
		return Cell(self.cells + other.cells)
	def __sub__(self, other):
		if self.cells - other.cells > 0:
			return Cell(self.cells - other.cells)
		else:
			print('Impossible')
	def __mul__(self, other):
		return Cell(self.cells * other.cells)
	def __floordiv__(self, other):
		return Cell(self.cells // other.cells)
	def __truediv__(self, other):
		return Cell(self.cells // other.cells)
	def make_order(self, str_cells):
		cells_str = ''
		for i in range(self.cells // str_cells):
			cells_str_small = '*' * str_cells + '\n'
			cells_str = cells_str + cells_str_small
		cells_str = cells_str + '*' * (self.cells % str_cells)
		return cells_str
cell1 = Cell(100)
cell2 = Cell(100)
print(cell1.make_order(5))