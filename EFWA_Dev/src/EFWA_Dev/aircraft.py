'''
aircraft.py


This file contains the aircraft class.
'''


class Aircraft:
    '''
    Aircraft class.
    '''

    def __init__(self, id: int = None):
        self.id = id or id(self)
        self.mass = 0  # kg

        # Wing Properties
        self.wing = Wing()
