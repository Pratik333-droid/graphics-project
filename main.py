import pygame
import math
from matrix import matrix_multiplication
from visibleSurfaceDetection import returnVisibleSurfaces
from angle import returnAngle, returnDistance
from bresenham_line import lineBanau
import time
import os

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.display.set_caption("Pulchowk Boys Hostel Projection")

width, height = 1200, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
black, white, blue, green = (40, 40, 40), (230, 230, 230), (0, 154, 255), (30, 200, 30)
cube_position = [width//2, height//2]
scale = 400
points = [n for n in range(16)]
angle_x, angle_y = 0.0, 0.0
projected_points = [_ for _ in range(16)]
run = True
x_cordy = 2
camera = {'x': 0.0,'y': 0.0,'z': 6.0}
x, y, z = 1, 1, 1.5
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


def connect_point(x_index, y_index, projected_2d_coordinates):
    coordinate_x = projected_2d_coordinates[x_index]
    coordinate_y = projected_2d_coordinates[y_index]
    # pygame.draw.line(screen, white, (a[0], a[1]), (b[0], b[1]), 1)
    lineBanau(screen, coordinate_x, coordinate_y, white)

def buildShape():
    # the following piece of code draws lines between all the vertices
    # ---------------------------------------------------------------------------------
    # for m in range(4):
    #     connect_point(m, (m+1)%4, projected_points)
    #     connect_point(m+4, (m+1)%4 + 4, projected_points)
    #     connect_point(m, m+4, projected_points)
    # for m in range(4):
    #     connect_point(m + 8, (m+1)%4 + 8, projected_points)
    #     connect_point(m+4 + 8, (m+1)%4 + 4 +8, projected_points)
    #     connect_point(m + 8, m+4 + 8, projected_points)
    # print ("faces = ",faces)
    # ---------------------------------------------------------------------------------

    visible_surfaces = returnVisibleSurfaces(faces, camera)
    if visible_surfaces[0] == 1:
        drawTop()
        print("top drawn")
    elif visible_surfaces[1] == 1:
        drawBottom()
        print("bottom drawn")
    if visible_surfaces[2] == 1:
        drawLeft()
        print("left drawn")
    elif visible_surfaces[3] == 1:
        drawRight()
        print("right drawn")
    if visible_surfaces[4] == 1:
        print("front drawn")
        drawFront()
    elif visible_surfaces[5] == 1:
        print("back drawn")
        drawBack()
    

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

def drawRight():
        connect_point(9, 10, projected_points)
        connect_point(10, 14, projected_points)
        connect_point(14, 13, projected_points)
        connect_point(13, 9, projected_points)
def drawFront():
        connect_point(8, 9, projected_points)
        connect_point(9, 13, projected_points)
        connect_point(13, 12, projected_points)
        connect_point(12, 8, projected_points)
def drawBack():
        connect_point(11, 10, projected_points)
        connect_point(10, 14, projected_points)
        connect_point(14, 15, projected_points)
        connect_point(15, 11, projected_points)

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
        angle_y = returnAngle(camera['x'], camera['z'] - z)
        # if angle_y < -1.4:
        #     angle_y = -1.4
        # angle_y, angle_z = 0.0, 0.0
        # distance = calcDistance(camera, points[8])
        
        hit = True
    elif keys[pygame.K_d]:
        camera['x'] += 0.5 * 0.05
        angle_y = returnAngle(camera['x'], camera['z'] - z)
        # if angle_y > 1.4:
        #     angle_y = 1.4
        # angle_y, angle_z = 0.0, 0.0
        # distance = calcDistance(camera, points[8])
        hit = True

    if keys[pygame.K_w]:
        camera['y'] -= 0.5 * 0.05
        angle_x = returnAngle(camera['y'], camera['z'] - z)
        # angle_x, angle_z = 0.0, 0.0
        # distance = calcDistance(camera, points[8])
        hit = True
    elif keys[pygame.K_s]:
        camera['y'] += 0.5 * 0.05
        angle_x = returnAngle(camera['y'], camera['z'] - z)
        # angle_x, angle_z = 0.0, 0.0
        # distance = calcDistance(camera, points[8])
        hit = True
    # print("camera = ",camera)

    if keys[pygame.K_UP]:
        camera['z'] += 0.5 * 0.05
        angle_x = returnAngle(camera['y'], camera['z'] - z)
        angle_y = returnAngle(camera['x'], camera['z'] - z)
        # angle_z += 0.05
        # distance = calcDistance(camera, points[8])
        hit = True
    elif keys[pygame.K_DOWN]:
        camera['z'] -= 0.5 * 0.05
        if camera['z'] < 1.55:
            camera['z'] = 1.55
        angle_x = returnAngle(camera['y'], camera['z'] - z)
        angle_y = returnAngle(camera['x'], camera['z'] - z)
        # angle_z -= 0.05
        # distance = calcDistance(camera, points[8])
        hit = True
    if keys[pygame.K_n]:
        angle_x, angle_y = 0.0, 0.0
        initializePoints()
        print("Points initialized")
        print("points = ", points)
        camera = {'x': 0.,'y': 0.,'z': 6.0}
        hit = True

    if hit == True:
        tamper_points = []
        unscaled_projected_2d = []
        index = 0
        
        for point in points:
            q_value = returnDistance(camera)
            z_cord = 1/(q_value - 0.05*point[2][0]) #point[2][0] means z coordinate of the point
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
            x_cord = int((projected_2d[0][0] - camera['x'])* scale) + cube_position[0]
            y_cord = int((projected_2d[1][0] - camera['y'])* scale) + cube_position[1]
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
        print("unscaled projected 2d = ", unscaled_projected_2d)
        print("")
        print("actual points = ",tamper_points)
        print("")
        print("scaled projected points = ",projected_points)
        print("angle_x = ", angle_x, "angle_y = ", angle_y)
        print("camera = ",camera)
        buildShape()
        pygame.draw.circle(screen, green, (int(camera['x']*scale + cube_position[0]), int(camera['y']*scale + cube_position[1])), 10)
        pygame.display.update()

# time.sleep(15)