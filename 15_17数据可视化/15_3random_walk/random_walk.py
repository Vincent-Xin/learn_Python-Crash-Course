from random import choice

class RandomWalk():
	def __init__(self,points_number=1000,max_distance=4):
		self.points_number=points_number
		self.max_distance=max_distance

		self.x_value=[0]
		self.y_value=[0]

	def fill_walk(self):
		while len(self.x_value) < self.points_number:
			x_direction=choice([1,-1])
			x_distance=choice(list(range(self.max_distance)))
			x_walk=x_direction*x_distance

			y_direction=choice([1,-1])
			y_distance=choice(list(range(self.max_distance)))
			y_walk=y_direction*y_distance

			if y_walk == 0 and x_walk == 0:
				continue
			else:
				next_x=self.x_value[-1]+x_walk
				next_y=self.y_value[-1]+y_walk
				self.x_value.append(next_x)
				self.y_value.append(next_y)

