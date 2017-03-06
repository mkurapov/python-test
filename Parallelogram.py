from Shape import Shape

class Parallelogram(Shape):

	def __init__(self, height=-1, width=-1):

		#default values will cause null to be caught
		if (height < 0 or width < 0):
			raise ValueError('Cannot have negative width or height.')

		self.height = height
		self.width = width

	def getArea(self):
		return self.height * self.width
