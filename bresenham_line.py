
# import pygame
from pygame import gfxdraw
# import time
boundary_color = (230, 230, 230)
def lineBanau(parda, cordy1, cordy2, color):
    
    x1 = cordy1[0]
    y1 = cordy1[1]
    x2 = cordy2[0]
    y2 = cordy2[1]
    k = 0
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    if x2>x1:
        lx = 1
    else:
        lx = -1
    if y2>y1:
        ly = 1
    else:
        ly = -1

    xk, yk = x1, y1
    # img.putpixel((x1,y1), (255, 255, 255, 255))
    # print("color = ",color)
    gfxdraw.pixel(parda, x1, y1, color)
    # pygame.display.update()

    if dx>= dy: #slope is less than or equal to 1
        pk = 2*dy - dx
        while k<=dx:
            
            if pk<0:
                xk += lx
                pk += 2*dy
            else:
                xk += lx
                yk += ly
                pk += 2*(dy - dx)
            
            # img.putpixel((xk,yk), (255, 255, 255, 255))
            gfxdraw.pixel(parda, xk, yk, color)
            # pygame.display.update()
            k += 1

    else:
        pk = 2*dx - dy
        while k<=dy:
            
            if pk<0:
                yk += ly
                pk += 2*dx
            else:
                xk += lx
                yk += ly
                pk += 2*(dx - dy)
            
            # img.putpixel((xk,yk), (255, 255, 255, 255))
            gfxdraw.pixel(parda, xk, yk, color)
            # pygame.display.update()
            k += 1
    
    # pygame.display.update()
