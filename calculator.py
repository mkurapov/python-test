#!/usr/bin/python
import argparse
from Rectangle import Rectangle
from Parallelogram import Parallelogram
from Triangle import Triangle
from Circle import Circle
from Shape import Shape


def help_message():
	print """[Calculate Triangle]
calculator.py -s triangle -b [BASE] -i [HEIGHT]

[Calculate Rectangle]
calculatory.py -s rectangle -w [WIDTH] -i [HEIGHT]

[Calculate Parallelogram]
calculator.py -s parallelogram -b [BASE] -i [HEIGHT]

[Calculate Circle]
calculator.py -s circle -r [RADIUS] or -d [DIAMETER]"""

parser = argparse.ArgumentParser(description="""
	[Calculate Triangle]
	calculator.py -s triangle -b [BASE] -i [HEIGHT]
	\r\n\r\n
	[Calculate Rectangle]
	calculatory.py -s rectangle -w [WIDTH] -i [HEIGHT]
	\r\n\r\n
	[Calculate Parallelogram]
	calculator.py -s parallelogram -b [BASE] -i [HEIGHT]
	\r\n\r\n
	[Calculate Circle]
	calculator.py -s circle -r [RADIUS] or -d [DIAMETER]
	""")
parser.add_argument('-s','--shape', help='Shape to calculate',required=True)
parser.add_argument('-b','--base',type=float ,help='Base of a shape', required=False)
parser.add_argument('-i','--height',type=float ,help='Height of a shape', required=False)
parser.add_argument('-w','--width',type=float ,help='Width of a shape', required=False)
parser.add_argument('-r','--radius',type=float ,help='Radius of a circle', required=False)
parser.add_argument('-d','--diameter',type=float ,help='Diameter of a circle', required=False)

args = parser.parse_args()

print ("******************************************")

try:
	shape = Shape()

	if args.shape == "triangle":
		shape = Triangle(args.base, args.height)

	elif args.shape == "rectangle":
		shape = Rectangle(args.height, args.width)

	elif args.shape == "parallelogram":
		shape = Parallelogram(args.base, args.height)

	elif args.shape == "circle":
		if (args.diameter is not None and args.radius is not None):
			print("Please specify radius or diameter, not both.")
		else:
			if (args.radius is not None):
				shape = Circle(args.radius)
			else:
				shape = Circle(args.diameter/2)

	else:
		raise Exception("Please enter valid shape name.")

	shape.printArea()

except Exception as e:
	print(e)


print ("******************************************")
