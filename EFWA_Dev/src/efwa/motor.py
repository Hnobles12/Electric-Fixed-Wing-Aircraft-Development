from .conversions import *

import math as m


class Motor:
    def __init__(self, rpm: float = 0, diameter: float = 0, pitch: float = 0, density: float = 0):
        self.rpm: float = rpm
        self.diameter: float = diameter
        self.pitch: float = pitch
        self.density: float = density

    def calc_thrust(self, rpm: float = None) -> float:
        self.rpm = rpm or self.rpm
        rads = rpm2rads(rpm=self.rpm)
        self.thrust = self.density*(m.pi*self.diameter**2)/(4)*rads*self.pitch
        return self.thrust

    def calc_rpm(self, thrust: float = None) -> float:
        self.thrust = thrust or self.thrust
        rads = self.thrust/(self.density*(m.pi*self.diameter**2)/4*self.pitch)
        self.rpm = rads2rpm(rads=rads)
        return self.rpm
