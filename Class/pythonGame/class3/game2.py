import sys
import pygame
from pygame.locals import *

pygame.init()

FPS = 30
framePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

gameDisplay = pygame.display.set_mode((600, 800))
pygame.display.set_caption("GAME")

positionX = 300
positionY = 750

bulletPositionX = 0
bulletPositionY = 0
bullet_speed = 30

speed = 20
while True:
    bulletPositionY -= bullet_speed
    gameDisplay.fill(WHITE)
    pygame.draw.circle(gameDisplay, BLACK, (positionX, positionY), 20)
    pygame.draw.circle(gameDisplay, RED, (bulletPositionX, bulletPositionY), 3)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            positionX -= speed
            continue

        if keys[pygame.K_RIGHT]:
            positionX += speed
            continue

        if keys[pygame.K_SPACE]:
            bulletPositionX = positionX
            bulletPositionY = positionY - 3
            continue

    framePerSec.tick(FPS)