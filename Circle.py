import math
from Shape import Shape

class Circle(Shape):

	def __init__(self, radius=-1):

		#default value will cause null to be caught
		if (radius < 0):
			raise ValueError('Radius or diamater cannot be null or negative.')

		self.radius = radius;

	def getArea(self):
		return (math.pi * self.radius * self.radius)
