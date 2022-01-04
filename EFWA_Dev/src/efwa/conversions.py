'''
conversions.py

Houses helper functions to convert between units.
'''

import math as m

###### Length Conversions ######


def f2m(f: float) -> float:
    '''
    Converts feet to meters.
    '''
    return f * 0.3048


def m2f(m: float) -> float:
    '''
    Converts meters to feet.
    '''
    return m * 3.28084


def in2m(in_: float) -> float:
    '''
    Converts inches to meters.
    '''
    return in_ * 0.0254


def m2in(m: float) -> float:
    '''
    Converts meters to inches.
    '''
    return m * 39.3701

###### Mass Conversions ######


def lb2kg(lb: float) -> float:
    '''
    Converts pounds to kilograms.
    '''
    return lb * 0.453592


def kg2lb(kg: float) -> float:
    '''
    Converts kilograms to pounds.
    '''
    return kg * 2.20462

###### Speed Conversions ######


def kts2mps(kts: float) -> float:
    '''
    Converts knots to meters per second.
    '''
    return kts * 0.514444


def mph2mps(mph: float) -> float:
    '''
    Converts miles per hour to meters per second.
    '''
    return mph * 0.44704


def fts2mps(fts: float) -> float:
    '''
    Converts feet per second to meters per second.
    '''
    return fts * 0.3048


def rpm2rads(rpm: float) -> float:
    '''
    Converts revolutions per minute to radians per second.
    '''
    return rpm * 2*m.pi/60


def rads2rpm(rads: float) -> float:
    '''
    Converts radians per second to revolutions per minute.
    '''
    return rads * 60/(2*m.pi)
