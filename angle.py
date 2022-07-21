import numpy as np

def returnAngle(perpendicular, base):
    if base == 0:
        return 1.5707
    ang = np.arctan(perpendicular/base)
    return ang

def returnDistance (cam):
    distance = (cam['x']**2 + cam['y']**2 + cam['z']**2)**0.5
    return distance