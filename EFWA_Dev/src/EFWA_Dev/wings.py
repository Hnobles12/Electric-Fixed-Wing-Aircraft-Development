'''
airfoil.py


This file contains the airfoil class.
'''

from dataclasses import dataclass


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
    def __init__(self, name: str = "airfoil", file: str = "airfoil.dat"):
        self.name: str = name
        self.file: str = file
        self.data: list[_Aifoil_data_line] = []
        self.read_data()

    def read_data(self):

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
                elif dataline.cl <= cl_min:
                    cl_min = data_line.cl
                    alpha_min = data_line.alpha

        self.alpha_stall = alpha_stall
        self.alpha_min = alpha_min

    def get_data(self, alpha: float):
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