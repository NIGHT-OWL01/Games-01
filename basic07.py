#enemy movements

import pygame
import random


pygame.init()

screen  = pygame.display.set_mode((800, 600))

running = True

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX=380
playerY=520
playerX_change=0

enemyImg = pygame.image.load('ufo.png')
enemyX=random.randint(0,736)
enemyY=random.randint(0,150)
enemyX_change=0.3
enemyY_change=40

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #check keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    #adding boudary
    if playerX <=0:
        playerX=0
    elif playerX >= 736:
        playerX=736
    
    #Enemy movement
    enemyX += enemyX_change
    #adding boudary
    if enemyX <=0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()