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