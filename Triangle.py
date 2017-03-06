from Shape import Shape

class Triangle(Shape):
	def __init__(self, base=-1, height=-1):

		#default values will cause null to be caught
		if (base < 0 or height < 0):
			raise ValueError('Base or height cannot be null or negative.')

		self.base = base
		self.height = height

	def getArea(self):
		return ((.5 * self.base) * self.height)
