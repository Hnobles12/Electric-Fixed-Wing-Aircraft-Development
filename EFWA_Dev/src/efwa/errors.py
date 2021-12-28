'''
errors.py

This file contains the error classes used in other parts of this library.
'''


# Wing Exceptions

class AirfoilNotLoadedErr(Exception):
    '''
    AirfoilNotLoadedErr is raised when an airfoil file is not loaded.
    '''

    def __init__(self, *args, **kwargs):
        self.message = "Airfoil file not loaded. Please load an airfoil file using wing.load_airfoil()."
        super().__init__(self.message)
