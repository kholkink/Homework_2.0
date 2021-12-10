class Clothes:
	def __init__(self, name):
		self.name = name
		self.clothes_mass = []
	def add_coat(self, size):
		self.clothes_mass.append(Coat(size))
	def add_tux(self, size):
		self.clothes_mass.append(Tux(size))
	def count_clothes(self):
		full_size = 0
		for cl in self.clothes_mass:
			print(cl.formula_size)
			full_size += cl.formula_size
		return full_size
class Coat:
	def __init__(self, size):
		self.size = size
	@property
	def formula_size(self):
		return self.size / 6.5 + 0.5
class Tux:
	def __init__(self, size):
		self.size = size
	@property
	def formula_size(self):
		return 2 * self.size + 0.3
cl = Clothes('Nothing')
cl.add_coat(100)
cl.add_coat(100)
cl.add_coat(100)
cl.add_tux(100)
print(cl.count_clothes())