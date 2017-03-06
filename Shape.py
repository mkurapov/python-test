class Shape():

	def __init__(self): pass

	def getArea(self):
	 	raise NotImplementedError('Shape.getArea is not overridden')

	def printArea(self):
		print("\tArea of a [%s] is [%s]" % (self.__class__.__name__, round(self.getArea(),2)))
