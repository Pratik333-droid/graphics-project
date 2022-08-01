from itertools import count
import pygame
from pygame import gfxdraw
def colorSurfaces(parda, two_d_points, fill_color, boundary_color):
    x_centre = int((two_d_points[0][0] + two_d_points[1][0] + two_d_points[2][0] + two_d_points[3][0] )/4)
    y_centre = int((two_d_points[0][1] + two_d_points[1][1] + two_d_points[2][1] + two_d_points[3][1] )/4)
    global county 
    county = 0

    def colorPixel(x, y):
        # global county
        # county = county + 1
        # print("no of recursions = ", county)
        print(county == 0)
        
        # county = 1
        # print("county = ",county)
        # county+= 1
        # print("county = ",county)
        current_color = parda.get_at((x, y))
        if current_color != fill_color and current_color != boundary_color:
            gfxdraw.pixel(parda, x, y, fill_color)
            colorPixel(x-1, y)
            colorPixel(x, y-1)
            colorPixel(x, y+1)
            colorPixel(x+1, y)


            
    # def colorPixel2(x, y):
    #     current_color = parda.get_at((x, y))
    #     if current_color != fill_color and current_color != boundary_color:
    #         gfxdraw.pixel(parda, x, y, fill_color)
    #         colorPixel2(x, y+1)
    #         colorPixel2(x+1, y)

    colorPixel(x_centre, y_centre)
    # print("county = ",county)
    # colorPixel2(x_centre+1, y_centre+1)