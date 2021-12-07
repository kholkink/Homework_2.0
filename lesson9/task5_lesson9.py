class Stationery:
	def __init__(self, title):
		self.title = title
		self.draw()
	def draw(self):
		print('Запуск отрисовки')
class Pen(Stationery):
	def draw(self):
		print('Pen is here!')
class Pencil(Stationery):
	def draw(self):
		print('Pencil is here!')
class Handle(Stationery):
	def draw(self):
		print('Handle is here!')
stationery1 = Stationery('Something')
pen1 = Pen('Something')
pencil = Pencil('Something')
handle = Handle('Something')
