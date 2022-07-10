import pygame
from matrix import matrix_multiplication
pygame.init()
pygame.display.set_caption("Pulchowk Boys Hostel Projection")
width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
black, white, blue  = (40, 40, 40), (230, 230, 230), (0, 154, 255)
cube_position = [width//2, height//2]
scale = 400
points = [n for n in range(16)]
x = 2
points[0] = [[-1], [-1], [1]]
points[1] = [[1], [-1], [1]]
points[2] = [[1], [1], [1]]
points[3] = [[-1], [1], [1]]
points[4] = [[-1], [-1], [-1]]
points[5] = [[1], [-1], [-1]]
points[6] = [[1], [1], [-1]]
points[7] = [[-1], [1], [-1]]

points[8] = [[-x], [-x], [1]]
points[9] = [[x], [-x], [1]]
points[10] = [[x], [x], [1]]
points[11] = [[-x], [x], [1]]
points[12] = [[-x], [-x], [-1]]
points[13] = [[x], [-x], [-1]]
points[14] = [[x], [x], [-1]]
points[15] = [[-x], [x], [-1]]

def connect_point(i, j, k):
    a = k[i]
    b = k[j]
    pygame.draw.line(screen, white, (a[0], a[1]), (b[0], b[1]), 1)

for point in points:
    distance = 5
    z = 1/(distance - point[2][0])
    projection_matrix = [[z, 0, 0], [0, z, 0]]
    projected_2d = matrix_multiplication(projection_matrix, point)
    x = int(projected_2d[0][0] * scale) + cube_position[0]
    y = int(projected_2d[1][0] * scale) + cube_position[1]
    print(f"x = {x}, y = {y}")
    # projected_points[index] = [x, y]
    # print("projected points = ", projected_points)
    pygame.draw.circle(screen, blue, (x, y), 10)