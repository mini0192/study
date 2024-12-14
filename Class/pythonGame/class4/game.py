import sys
import pygame
from pygame.locals import *
import random
from typing import List, Final

class Enemy:
    def __init__(self, speed: int, x: int) -> None:
        self.size: int = 20
        self.speed: int = speed
        self.x: int = x
        self.y: int = 0
    
    def getPosition(self) -> List[int]:
        return [self.x, self.y]
    
    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
    
    def move(self) -> None:
        self.y += self.speed

class Bullet:
    def __init__(self, x: int, y: int) -> None:
        self.size: int = 5
        self.speed: int = 30
        self.x: int = x
        self.y: int = y
    
    def move(self) -> None:
        self.y -= self.speed
    
    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
    
    def getPosition(self) -> List[int]:
        return [self.x, self.y]
    
class Player:
    def __init__(self, x: int, y: int) -> None:
        self.size: int = 20
        self.speed: int = 5
        self.x: int = x
        self.y: int = y
    
    def move(self, move: str) -> None:
        if(move == "r"):
            self.x += self.speed
            return
        
        if(move == "l"):
            self.x -= self.speed
            return
        
    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
    
    def getPosition(self) -> List[int]:
        return [self.x, self.y]

pygame.init()

FPS: Final = 60
framePerSec: Final = pygame.time.Clock()

font: Final = pygame.font.SysFont('Arial', 30)
pygame.display.set_caption("GAME")

gameDisplay: Final = pygame.display.set_mode((600, 800))

BLUE: Final = (0,0,255)
RED: Final = (255,0,0)
GREEN: Final = (0,255,0)

WHITE: Final = (255, 255, 255)
BLACK: Final = (0, 0, 0)

player = Player(300 ,700)
bullets: List[Bullet] = list()
enemys: List[Enemy] = list()

count: int = 0
gameOut: bool = False
score: int = 0

while True:
    if gameOut:
        break

    count += 1
    gameDisplay.fill(WHITE)

    text = font.render("Score: {}".format(score), True, BLACK)
    gameDisplay.blit(text, text.get_rect(topleft = (10, 10)))
    pygame.draw.circle(gameDisplay, BLACK, player.getPosition(), player.size)

    for enemy in enemys:
        enemy.move()
        pygame.draw.circle(gameDisplay, RED, enemy.getPosition(), enemy.size)
    enemys = [enemy for enemy in enemys if enemy.y < 800]

    for bullet in bullets:
        bullet.move()
        pygame.draw.circle(gameDisplay, BLUE, bullet.getPosition(), bullet.size)
    bullets = [bullet for bullet in bullets if bullet.y > 0]

    for enemy in enemys:
        if player.getRect().colliderect(enemy.getRect()):
            print("게임 아웃")
            gameOut = True
            
        for bullet in bullets:
            if enemy.getRect().colliderect(bullet.getRect()):
                enemys.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("l")

    if keys[pygame.K_RIGHT]:
        player.move("r")

    if keys[pygame.K_SPACE]:
        bullets.append(Bullet(player.x, player.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if(count % 30 == 0):
        enemySpeed: int = random.randint(1, 10)
        enemyX: int = random.randint(1, 600)
        enemys.append(Enemy(enemySpeed, enemyX))

    framePerSec.tick(FPS)