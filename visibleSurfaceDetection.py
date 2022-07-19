
def returnVisibleSurfaces(surfaces, cam):
    #top bottom left right front back
    plane_coefficients = []
    coefficients = []
    return_coefficients = [_ for _ in range(6)]
    for surface in surfaces:
        x1, x2, x3 = surface[0][0][0], surface[1][0][0], surface[2][0][0]
        y1, y2, y3 = surface[0][1][0], surface[1][1][0], surface[2][1][0]
        z1, z2, z3 = surface[0][2][0], surface[1][2][0], surface[2][2][0]
        a = y1*(z2 - z3) + y2*(z3 - z1) + y3*(z1 - z2)
        b = z1*(x2 - x3) + z2*(x3 - x1) + z3*(x1 - x2)
        c = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
        d = x1*(y2*z3 - y3*z2) + x2*(y3*z1 - y1*z3) + x3*(y1*z2 - y2*z1)
        plane_coefficients.append([a, b, c, d])
        coefficients.append(a*cam['x'] + b*cam['y'] + c*cam['z'] + d)
        # print("camera coordinates = ", cam)
    print("plane_coefficients = ",plane_coefficients)
    print("coefficients = ",coefficients)
    
    for i in range(0, 6, 2):
        if abs(coefficients[i]) > abs(coefficients[i+1]):
            return_coefficients[i] = 0
            return_coefficients[i+1] = 1
        elif abs(coefficients[i]) < abs(coefficients[i+1]):
            return_coefficients[i] = 1
            return_coefficients[i+1] = 0
        else:
            return_coefficients[i] = return_coefficients[i+1] = 0

    print("return coefficients = ",return_coefficients)
    return return_coefficients


