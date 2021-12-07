class Road:
	def __init__(self, lenght, width):
		self.__width = width
		self.__lenght = lenght
		self.__weight = 720
	def calculate(self):
		return self.__width * self.__lenght * self.__weight
road1 = Road(100, 200)
print(road1.calculate(), 'T')
