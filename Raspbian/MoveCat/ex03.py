import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Animation Pygame')

WHITE = (255,255,255)
catImg = pygame.image.load('cat.png')
catx = 10; caty = 10
direction = 'right'

while True: #main Loop
    DISPLAYSURF.fill(WHITE)
    if direction == 'right':
        catx += 5
        if catx == 600:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 400:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)