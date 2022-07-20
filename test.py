import pygame
from pygame import gfxdraw
# import time
pygame.init()
# pygame.display.set_caption("3D cube Projection")
def dharkaKor(parda, color, cordy1, cordy2, motai):
    gfxdraw.pixel(parda, cordy1[0]+10, cordy1[1], color)
    pygame.draw.line(parda, color, cordy1, cordy2, motai)

#yaha taw j gare pani hunxa. this file is under gitignore so any changes made here will be untracted
if __name__ == "__main__":
    print("Holy shit this is not supposed to run")
    width, height = 800, 600
    # screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    fps = 60
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN:
                print("keydown detected")
            elif event.type == pygame.KEYUP:
                print("keyup detected")
        keys = pygame.key.get_pressed() 
        # print("keys =",keys)
        if keys[pygame.K_LEFT]:
            print("key press left detected")
        if keys[pygame.K_RIGHT]:
            print("key press right detected")
