import sys
import pygame
from pygame.locals import *

pygame.init()

FPS = 30
framePerSec = pygame.time.Clock()

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

gameDisplay = pygame.display.set_mode((600, 800))
pygame.display.set_caption("GAME")

positionX = 300
positionY = 750

speed = 20

bullet_speed = 30
bullets = []

while True:
    gameDisplay.fill(WHITE)
    pygame.draw.circle(gameDisplay, BLACK, (positionX, positionY), 20)

    for bullet in bullets:
        bullet[1] -= bullet_speed
        pygame.draw.circle(gameDisplay, RED, bullet, 3)

    pygame.display.update()

    bullets = [bullet for bullet in bullets if bullet[1] > 0]

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
            bullets.append([positionX, positionY])
            continue

    framePerSec.tick(FPS)