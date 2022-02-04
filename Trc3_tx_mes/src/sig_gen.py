#from conf_model import *
from math import sin, cos
"""
AM generator
"""
def sig_gen (param: list,Time)->list:

    ωfc = 6.28*int(param[0])
    ω2fc = 2*ωfc
    ω3fc = 3*ωfc
    A1 = int(param[1])/2
    A2 = A1*0.01
    A3 = A1*0.001
    if int(param[2]) == 0:
        M = 0
        ωfm = 0
    else:
        M = 1
        ωfm = 6.28*int(param[2])

    return([A1*cos(ωfc*t)*(1+ M*cos(ωfm*t))+\
            A2*cos(ω2fc*t)*(1+M*cos(ωfm*t))+\
            A3*cos(ω3fc*t)*(1+ M*cos(ωfm*t)) for t in Time])
