import time
class TrafficLight:
	def __init__(self):
		self.color_time = {'yellow': 2, 'green': 5, 'red': 7,}
		self._color = 'red'
		self.iters = 2
		self._running()
	def _running(self):
		print("Running")
		clock = check_time()
		for i in range(self.iters):
			for i in self.color_time:
				print(self._color)
				print(self.color_time[self._color])
				while check_time() < clock + self.color_time[self._color]:
					pass
				self._color = i
				clock = check_time()
xu = TrafficLight()
print(xu._color)


