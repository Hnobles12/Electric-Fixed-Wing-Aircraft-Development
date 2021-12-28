'''
wings.py


This file contains the airfoil and wing classes.
'''

import math as m
from dataclasses import dataclass

from .errors import AirfoilNotLoadedErr


@dataclass
class _Aifoil_data_line:
    alpha: float
    cl: float
    cd: float
    cdp: float
    cm: float
    top_xtr: float
    bot_xtr: float


class Airfoil:
    def __init__(self, name: str = "airfoil", file: str = "airfoil.dat") -> None:
        self.name: str = name
        self.file: str = file
        self.data: list[_Aifoil_data_line] = []
        self.read_data()

    def read_data(self) -> None:

        cl_max = 0
        cl_min = 0

        alpha_stall = 0
        alpha_min = 0

        with open(self.file, "r") as f:
            for i, line in enumerate(f):
                if i == 0:
                    continue
                line = line.split(',')
                line = [float(x) for x in line]

                data_line = _Aifoil_data_line(
                    line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                self.data.append(data_line)

                if data_line.cl >= cl_max:
                    cl_max = data_line.cl
                    alpha_stall = data_line.alpha
                elif data_line.cl <= cl_min:
                    cl_min = data_line.cl
                    alpha_min = data_line.alpha

        self.alpha_stall = alpha_stall
        self.alpha_min = alpha_min
        self.cl_max = cl_max
        self.cl_min = cl_min

    def get_data(self, alpha: float) -> _Aifoil_data_line:
        '''
        Get closest data entry to alpha given.
        '''

        da = 0
        a = 0
        for i, data in enumerate(self.data):
            if abs(data.alpha - alpha) < da:
                da = abs(data.alpha - alpha)
                a = data

        return a


###############################################################################
##############################  Wing Class ####################################
###############################################################################

class Wing:
    def __init__(self,  airfoil_file: str = '', load_foil:bool = False) -> None:
        if load_foil or (airfoil_file != ''):
            self.airfoil: Airfoil = Airfoil(file=airfoil_file)
            self.foil_loaded = True
        else:
            self.foil_loaded = False
        
        self.airspeed: float = 0
        self.span: float = 0
        self.area: float = 0
        self.AR: float = 0
        self.e: float = 0
        self.density: float = 0
        self.aoa: float = 0
        
        

        # Calculated values
        self.lift: float = 0
        self.tot_drag = 0
        self.stall_speed: float = 0
        

    def check_airfoil_loaded(self, raise_err:bool=True)->bool:
        '''
        Check if an airfoil file is loaded and raise an exception if not. Can disable exception by setting arg raise_err to false.
        '''
        if self.foil_loaded:
            return True
        else:
            if raise_err:
                raise AirfoilNotLoadedErr()
            else:
                return False
    
    def load_airfoil(self, file:str):
        '''
        Loads an airfoil file.
        '''
        self.airfoil = Airfoil(file=file)
        self.foil_loaded = True

    def calc_area(self) -> float:
        '''
        Calculate wing area for lift desired.
        '''
        self.check_airfoil_loaded()

        cl = self.airfoil.get_data(self.aoa).cl
        self.area = self.lift / (self.cl*self.density*self.airspeed ** 2 / 2)
        return self.area

    def calc_lift(self) -> float:
        '''
        Calculate lift created by the wing.
        '''
        self.check_airfoil_loaded()

        cl = self.airfoil.get_data(self.aoa).cl
        self.lift = cl * self.area * airspeed ** 2 / 2
        return self.lift

    def calc_drag()->float:
        '''
        Calculate drag created by the wing.
        '''
        self.check_airfoil_loaded()

        cl = self.airfoil.get_data(self.aoa).cl
        cd0 = self.airfoil.get_data(self.aoa).cd
        cd = 0.5*self.density*self.airspeed**2*cd0*self.area
        cdi = cl**2 / (m.pi * self.e * self.AR)
        
        self.tot_drag = cd + cdi
        return self.tot_drag
        