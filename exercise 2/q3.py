'''
Python program to calculate area and perimeters
'''
import numpy

class Shapes(object):
    """
    Class to define shapes
    """
	# Constructor
    def __init__(self, shape):
        '''
		Constructor
		'''
        self.shape_name = shape

	# To get name
    def get_name(self):
        '''
		Function to get name
		'''
        return self.shape_name


# Inherited or Sub class (Note Person in bracket)
class Rectangle(Shapes):
    '''
	Class for rectangle
	'''
	# Constructor
    def __init__(self, shape_name, length, breadth):
        '''
		Function to assign length and breadth
		'''
        Shapes.__init__(self, shape_name)
        self.length = length
        self.breadth = breadth

	# To get name
    def get_perimeter(self):
        '''
		Function to get perimeter
		'''
        perimeter = 2*(self.length + self.breadth)
        return print("Perimeter is", perimeter)

    def get_area(self):
        '''
		Function to get area
		'''
        area = self.length * self.breadth
        return print("Area is", area)

class Square(Shapes):
    '''
	Class for square
	'''

    def __init__(self, shape_name, side):
        '''
		Constructor
		'''
        Shapes.__init__(self, shape_name)
        self.side = side

    def get_perimeter(self):
        '''
		Function to get perimeter
		'''
        perimeter = 4 * self.side
        return print("Perimeter is", perimeter)

    def get_area(self):
        '''
		Function to get area
		'''
        area = self.side * self.side
        return print("Area is", area)

class Circle(Shapes):
    '''
	Class for circles.
	'''

	# Constructor
    def __init__(self, shape_name, radius):
        '''
		Constructor
		'''
        Shapes.__init__(self, shape_name)
        self.radius = radius

    def get_circumference(self):
        '''
		Function to get circumference
		'''
        pi_value = numpy.pi
        circumference = 2 * pi_value * self.radius
        return print("Perimeter is", circumference)

    def get_area(self):
        '''
		Function to get area
		'''
        pi_value = numpy.pi
        area = pi_value * self.radius**2
        return print("Area is", area)

if __name__ == "__main__":
	# Driver code
    a = Circle("circle", 10)
    a.get_area()
