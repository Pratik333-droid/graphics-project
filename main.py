import pygame
import math
from matrix import matrix_multiplication
from visibleSurfaceDetection import returnVisibleSurfaces
# from surface_coloring import colorSurfaces
from angle import returnAngle, returnDistance
from bresenham_line import lineBanau, returnLineCoordinates
import time
import os
# import sys
# sys.setrecursionlimit(10**6)
pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.display.set_caption("Skeletal Representation of Pulchowk Boys Hostel Lite")

width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
black, boundary_color, blue, green = (40, 40, 40), (230, 230, 230), (0, 154, 255), (30, 200, 30)
cube_position = [width//2, height//2]
scale = 400
points = [n for n in range(24)]
angle_x, angle_y, angle_z = 0.0, 0.0, 0.0
projected_points = [_ for _ in range(24)]
run = True
x_cordy = 2
camera = {'x': 0.0,'y': 0.0,'z': 6.0}
x, y, z = 1, 1, 2
x2, y2 = 2, 2
tamper_points = []
faces = []
def declareFaces(tampered_points):
    """ assignes coordinates to faces"""
    global faces
    top = [tampered_points[8], tampered_points[9], tampered_points[10], tampered_points[11]]
    bottom = [tampered_points[12], tampered_points[13], tampered_points[14], tampered_points[15]]
    left = [tampered_points[8], tampered_points[11], tampered_points[15], tampered_points[12]]
    right = [tampered_points[9], tampered_points[10], tampered_points[14], tampered_points[13]]
    front = [tampered_points[8], tampered_points[9], tampered_points[13], tampered_points[12]]
    back = [tampered_points[11], tampered_points[10], tampered_points[14], tampered_points[15]]
    faces = [top, bottom, left, right, front, back]
def initializePoints():
    global points
    points[0] = [[-x], [-y], [z]]
    points[1] = [[x], [-y], [z]]
    points[2] = [[x], [y], [z]]
    points[3] = [[-x], [y], [z]]
    points[4] = [[-x], [-y], [-z]]
    points[5] = [[x], [-y], [-z]]
    points[6] = [[x], [y], [-z]]
    points[7] = [[-x], [y], [-z]]

    points[8] = [[-x2], [-y2], [z]]
    points[9] = [[x2], [-y2], [z]]
    points[10] = [[x2], [y2], [z]]
    points[11] = [[-x2], [y2], [z]]
    points[12] = [[-x2], [-y2], [-z]]
    points[13] = [[x2], [-y2], [-z]]
    points[14] = [[x2], [y2], [-z]]
    points[15] = [[-x2], [y2], [-z]]

    points[16] = [[-x2], [-y2], [-z + 2/3*2*z]]
    points[17] = [[x2], [-y2], [-z + 2/3*2*z]]
    points[18] = [[x2], [y2], [-z + 2/3*2*z]]
    points[19] = [[-x2], [y2], [-z + 2/3*2*z]]
    points[20] = [[-x2], [-y2], [-z + 1/3*2*z]]
    points[21] = [[x2], [-y2], [-z + 1/3*2*z]]
    points[22] = [[x2], [y2], [-z + 1/3*2*z]]
    points[23] = [[-x2], [y2], [-z + 1/3*2*z]]


def connect_point(first_coordinate_index, second_coordinate_index, projected_2d_coordinates):
    first_coordinate = projected_2d_coordinates[first_coordinate_index]
    second_coordinate = projected_2d_coordinates[second_coordinate_index]
    # pygame.draw.line(screen, white, (a[0], a[1]), (b[0], b[1]), 1)
    lineBanau(screen, first_coordinate, second_coordinate, boundary_color)

def buildShape():
    visible_surfaces = returnVisibleSurfaces(faces, camera)
    if visible_surfaces[0] == 1:
        drawTop()
        # print("top drawn")
    elif visible_surfaces[1] == 1:
        drawBottom()
        # print("bottom drawn")
    if visible_surfaces[2] == 1 and (abs(camera['x']) > 0.173):
        drawLeft()
        # print("left drawn")
    elif visible_surfaces[3] == 1 and (camera['x'] > 0.173):
        drawRight()
        # print("right drawn")
    if visible_surfaces[4] == 1 and (abs(camera['y']) > 0.173):
        # print("front drawn")
        drawFront()
    elif visible_surfaces[5] == 1 and (camera['y'] > 0.173):
        # print("back drawn")
        drawBack()
    

def colorSurface (surface, fill_color):
        arr1 = returnLineCoordinates(surface[0], surface[2])
        arr2 = returnLineCoordinates(surface[1], surface[3])
        len1 = len(arr1)
        len2 = len(arr2)
        n = len1 if len1 < len2 else len2
        for i in range(n):
            lineBanau(screen, arr1[i], arr2[i], fill_color)


def drawTop():
    for m in range(4):
        connect_point(m, (m+1)%4, projected_points)
        connect_point(m + 8, (m+1)%4 + 8, projected_points)
def drawBottom():
    for m in range(0, 4):
        connect_point(m+12, (m+1)%4 + 12, projected_points)
def drawLeft():
        connect_point(8, 11, projected_points)
        connect_point(11, 15, projected_points)
        connect_point(15, 12, projected_points)
        connect_point(12, 8, projected_points)

        connect_point(19, 16, projected_points)
        connect_point(23, 20, projected_points)
        fill_color = (150, 75, 30)
        layer1 = [projected_points[11], projected_points[8], projected_points[19], projected_points[16]]
        layer2 = [projected_points[19], projected_points[16], projected_points[23], projected_points[20]]
        layer3 = [projected_points[23], projected_points[20], projected_points[15], projected_points[12]]
        colorSurface(layer1, fill_color)
        colorSurface(layer2, fill_color)
        colorSurface(layer3, fill_color)

def drawRight():
        
        connect_point(9, 10, projected_points)
        connect_point(10, 14, projected_points)
        connect_point(14, 13, projected_points)
        connect_point(13, 9, projected_points)

        connect_point(17, 18, projected_points)
        connect_point(21, 22, projected_points)
        fill_color = (150, 75, 30)
        layer1 = [projected_points[9], projected_points[10], projected_points[17], projected_points[18]]
        layer2 = [projected_points[17], projected_points[18], projected_points[21], projected_points[22]]
        layer3 = [projected_points[21], projected_points[22], projected_points[13], projected_points[14]]
        colorSurface(layer1, fill_color)
        colorSurface(layer2, fill_color)
        colorSurface(layer3, fill_color)

def drawFront():
        connect_point(8, 9, projected_points)
        connect_point(9, 13, projected_points)
        connect_point(13, 12, projected_points)
        connect_point(12, 8, projected_points)

        connect_point(16, 17, projected_points)
        connect_point(20, 21, projected_points)

        fill_color = (150, 75, 30)
        layer1 = [projected_points[8], projected_points[9], projected_points[16], projected_points[17]]
        layer2 = [projected_points[16], projected_points[17], projected_points[20], projected_points[21]]
        layer3 = [projected_points[20], projected_points[21], projected_points[12], projected_points[13]]
    
        colorSurface(layer1, fill_color)
        colorSurface(layer2, fill_color)
        colorSurface(layer3, fill_color)


def drawBack():
        connect_point(11, 10, projected_points)
        connect_point(10, 14, projected_points)
        connect_point(14, 15, projected_points)
        connect_point(15, 11, projected_points)

        connect_point(18, 19, projected_points)
        connect_point(22, 23, projected_points)

        fill_color = (150, 75, 30)
        layer1 = [projected_points[10], projected_points[11], projected_points[18], projected_points[19]]
        layer2 = [projected_points[18], projected_points[19], projected_points[22], projected_points[23]]
        layer3 = [projected_points[22], projected_points[23], projected_points[14], projected_points[15]]
        colorSurface(layer1, fill_color)
        colorSurface(layer2, fill_color)
        colorSurface(layer3, fill_color)

def returnRotationMatrices(x, y):
    return_matrix = [[[1, 0, 0],
                [0, round(math.cos(x), 4), round(-math.sin(x), 4)],
                [0, round(math.sin(x), 4), round(math.cos(x), 4)]], 
                [[round(math.cos(y), 4), 0, round(-math.sin(y), 4)],
                [0, 1, 0],
                [round(math.sin(y), 4), 0, round(math.cos(y), 4)]]]
    return return_matrix


initializePoints()
while run:
    hit = False
    clock.tick(fps)
    screen.fill(black)
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
        camera['x'] -= 0.5 * 0.05
        angle_y = returnAngle(camera['x'], camera['z'] - z)*1.2
        # if angle_y < -1.4:
        #     angle_y = -1.4
        # angle_y, angle_z = 0.0, 0.0
        # distance = calcDistance(camera, points[8])
        
        hit = True
    elif keys[pygame.K_d]:
        camera['x'] += 0.5 * 0.05
        angle_y = returnAngle(camera['x'], camera['z'] - z)*1.2
        # if angle_y > 1.4:
        #     angle_y = 1.4
        # angle_y, angle_z = 0.0, 0.0
        # distance = calcDistance(camera, points[8])
        hit = True

    if keys[pygame.K_w]:
        camera['y'] -= 0.5 * 0.05
        angle_x = returnAngle(camera['y'], camera['z'] - z)*1.2
        # angle_x, angle_z = 0.0, 0.0
        # distance = calcDistance(camera, points[8])
        hit = True
    elif keys[pygame.K_s]:
        camera['y'] += 0.5 * 0.05
        angle_x = returnAngle(camera['y'], camera['z'] - z)*1.2
        # angle_x, angle_z = 0.0, 0.0
        # distance = calcDistance(camera, points[8])
        hit = True
    # print("camera = ",camera)

    if keys[pygame.K_UP]:
        camera['z'] += 0.5 * 0.05
        angle_x = returnAngle(camera['y'], camera['z'] - z)*1.2
        angle_y = returnAngle(camera['x'], camera['z'] - z)*1.2
        # angle_z += 0.05
        # distance = calcDistance(camera, points[8])
        hit = True
    elif keys[pygame.K_DOWN]:
        camera['z'] -= 0.5 * 0.05
        if camera['z'] < 1.55:
            camera['z'] = 1.55
        angle_x = returnAngle(camera['y'], camera['z'] - z)*1.2
        angle_y = returnAngle(camera['x'], camera['z'] - z)*1.2
        # angle_z -= 0.05
        # distance = calcDistance(camera, points[8])
        hit = True
    if keys[pygame.K_n]:
        angle_x, angle_y = 0.0, 0.0
        initializePoints()
        # print("Points initialized")
        # print("points = ", points)
        camera = {'x': 0.,'y': 0.,'z': 6.0}
        hit = True

    if hit == True:
        tamper_points = []
        unscaled_projected_2d = []
        index = 0
        
        for point in points:
            q_value = returnDistance(camera)
            z_cord = 1/(q_value - 0.15*point[2][0]) #point[2][0] means z coordinate of the point
            # z_cord = 1/point[2][0]
            projection_matrix = [[z_cord, 0, 0], [0, z_cord, 0]]
            rotation_matrix = returnRotationMatrices(angle_x, angle_y)
            rotated_point = matrix_multiplication(rotation_matrix[0], point)
            rotated_point = matrix_multiplication(rotation_matrix[1], rotated_point)
            # rotated_point = matrix_multiplication(rotation_matrix[2], rotated_point)
            projected_2d = matrix_multiplication(projection_matrix, rotated_point)
            tamper_points.append(rotated_point)
            unscaled_projected_2d.append(projected_2d)
            # print("projected 2d = ", projected_2d)
            # print("rotated points = ", rotated_point)
            x_cord = int((projected_2d[0][0] - 0.7*camera['x'])* scale) + cube_position[0]
            y_cord = int((projected_2d[1][0] - 0.7*camera['y'])* scale) + cube_position[1]
            # x = int((projected_2d[0][0] -camera["x"])* scale) + cube_position[0]
            # y = int((projected_2d[1][0] - camera["y"])* scale) + cube_position[1]
            # print(f"x = {x_cord}, y = {y_cord}")
            # print("index =",index)
            projected_points[index] = [x_cord, y_cord]
            index += 1
            # print("projected points = ", projected_points)
            # pygame.draw.circle(screen, blue, (x_cord, y_cord), 10)
            # print ("This")
        declareFaces(tamper_points)
        # print("faces = ",faces)
        # print("unscaled projected 2d = ", unscaled_projected_2d)
        # print("")
        # print("actual points = ",tamper_points)
        # print("")
        # print("scaled projected points = ",projected_points)
        # print("angle_x = ", angle_x, "angle_y = ", angle_y)
        # print("camera = ",camera)
        buildShape()
        pygame.draw.circle(screen, green, (int(camera['x']*scale + cube_position[0]), int(camera['y']*scale + cube_position[1])), 10)
        pygame.display.update()
