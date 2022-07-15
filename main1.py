import pygame
import os
import math
from matrix import matrix_multiplication
from bresenham_line import lineBanau
import time

os.environ["SDL_VIDEO_CENTERED"] = '1'
black, white, blue, green = (40, 40, 40), (230, 230, 230), (0, 154, 255), (30, 200, 30)
width, height = 1200, 600

pygame.init()
pygame.display.set_caption("Pulchowk Boys Hostel Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
angle = 0
cube_position = [width // 2, height // 2]
scale = 300
speed = 0
points = [n for n in range(9)]

# Setup for camera
camera = {
    'x': 0.,
    'y': 0.,
    'z': 5.0
}

points[0] = [[-1.], [-1], [1]]
points[1] = [[1.], [-1], [1]]
points[2] = [[1.], [1], [1]]
points[3] = [[-1.], [1], [1]]
points[4] = [[-1.], [-1], [-1]]
points[5] = [[1.], [-1], [-1]]
points[6] = [[1.], [1], [-1]]
points[7] = [[-1.], [1], [-1]]
points[8] = [[0.],[0.],[0.]]
loop = 0



def calcDistance(camera, centre):
    return (((camera["x"]- centre[0][0])**2 + (camera["y"]- centre[1][0])**2 + (camera["z"]- centre[2][0])**2)**0.5)

def connect_point(i, j, k):
    a = k[i]
    b = k[j]
    pygame.draw.line(screen, white, (a[0], a[1]), (b[0], b[1]), 1)
    
run = True
projected_points = [j for j in range(len(points))]
distance = calcDistance(camera, points[8])
while run:
    hit = False
    count = 0
    clock.tick(fps)
    screen.fill(black)

    rotation_x = [[1, 0, 0],
                [0, math.cos(angle), -math.sin(angle)],
                [0, math.sin(angle), math.cos(angle)]]

    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                [0, 1, 0],
                [math.sin(angle), 0, math.cos(angle)]]

    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                [math.sin(angle), math.cos(angle), 0],
                [0, 0, 1]]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
                break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        camera['x'] -= 0.5 * 0.01
        angle += 0.1
        # distance = calcDistance(camera, points[8])
        
        hit = True
    elif keys[pygame.K_d]:
        camera['x'] += 0.5 * 0.01
        angle -= 0.1
        # distance = calcDistance(camera, points[8])
        hit = True

    if keys[pygame.K_w]:
        camera['y'] -= 0.5 * 0.01
        angle += 0.01
        # distance = calcDistance(camera, points[8])
        hit = True
    elif keys[pygame.K_s]:
        camera['y'] += 0.5 * 0.01
        angle -= 0.01
        # distance = calcDistance(camera, points[8])
        hit = True
    # print("camera = ",camera)

    if keys[pygame.K_UP]:
        camera['z'] += 0.5 * 0.1
        # distance = calcDistance(camera, points[8])
        hit = True
    elif keys[pygame.K_DOWN]:
        camera['z'] -= 0.5 * 0.1
        # distance = calcDistance(camera, points[8])
        hit = True

    if hit == True:
        index = 0
        pygame.draw.circle(screen, green, (int(camera['x']*scale + cube_position[0]), int(camera['y']*scale + cube_position[1])), 10)
        # pygame.display.update()
        for point in points:
            distance = calcDistance(camera, point)
            z = 1 / (distance - point[2][0])
            projection_matrix = [[z, 0, 0],
                                 [0, z, 0]]
            virtual_point = matrix_multiplication(rotation_x, point)
            projected_2d = matrix_multiplication(projection_matrix, virtual_point)

            x = int((projected_2d[0][0] - camera['x']) * scale) + cube_position[0]
            y = int((projected_2d[1][0] - camera['y']) * scale) + cube_position[1]
            # print(f"x = {x}, y = {y}")
            projected_points[index] = [x, y]
            # print("projected points = ", projected_points)
            pygame.draw.circle(screen, blue, (x, y), 10)
            index += 1
        # draw edges
        for m in range(4):
            connect_point(m, (m + 1) % 4, projected_points)
            # print("this mofo runs")
            # time.sleep(3)
            connect_point(m + 4, (m + 1) % 4 + 4, projected_points)
            connect_point(m, m + 4, projected_points)
        # angle += speed
        pygame.display.update()
        loop = 1

    # for event in pygame.event.get():
        # if keys[pygame.K_SPACE]:
        
# dharkaKor(screen, white, (0, 0), (100, 100), 2)
# pygame.display.update()
# time.sleep(2)
pygame.quit()
