class Car:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police
	def go(self):
		print('Started')
	def stop(self):
		print('Stopped')
	def turn(self, direction):
		print(direction)
	def show_speed(self):
		print(self.speed, 'km/h')
class TownCar(Car):
	def show_speed(self):
		if self.speed > 60:
			print('overspeed')
class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40:
			print('overspeed')
car1 = Car(100, 'red', 'volvo', False)
car1.turn('right')
workcar1 = WorkCar(100, 'red', 'volvo', False)
workcar1.show_speed()