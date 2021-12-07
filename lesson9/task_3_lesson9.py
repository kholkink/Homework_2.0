class Worker:
	def __init__(self):
		self.name = 'Ivan'
		self.surename = 'Popov'
		self.position = 'Cook'
		self.__income = {'wage': 100000, 'bonus': 50000}
class Position(Worker):
	def get_full_name(self):
		return self.name, self.surename
	def get_total_income(self):
		return self._Worker__income['wage'] + self._Worker__income['bonus']
position1 = Position()
print(position1.get_full_name())
print(position1.get_total_income())