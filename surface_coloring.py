import pygame
from pygame import gfxdraw
def colorSurfaces(parda, two_d_points, fill_color, boundary_color):
    x_centre = int((two_d_points[0][0] + two_d_points[1][0] + two_d_points[2][0] + two_d_points[3][0] )/4)
    y_centre = int((two_d_points[0][1] + two_d_points[1][1] + two_d_points[2][1] + two_d_points[3][1] )/4)
