import sys
import pygame
from pygame.locals import *

pygame.init()

FPS = 30
framePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

gameDisplay = pygame.display.set_mode((600, 800))
pygame.display.set_caption("GAME")

while True:
    gameDisplay.fill(WHITE)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    framePerSec.tick(FPS)