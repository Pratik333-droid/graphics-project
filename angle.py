import numpy as np

def returnAngle(perpendicular, base):
    if base == 0:
        return 1.5707
    ang = np.arctan(perpendicular/base)
    return ang