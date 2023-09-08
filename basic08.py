#bullet movement
import pygame
import random


pygame.init()

screen  = pygame.display.set_mode((800, 600))

running = True

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

backgroundImg = pygame.image.load('background.jpg')

playerImg = pygame.image.load('player.png')
playerX=380
playerY=520
playerX_change=0

#Enemy
enemyImg = pygame.image.load('ufo.png')
enemyX=random.randint(0,736)
enemyY=random.randint(0,150)
enemyX_change=0.3
enemyY_change=40

#Bullet

#Ready - You can't see the bullet on the screen
#Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX= 0
bulletY=480
bulletX_change=0
bulletY_change=1
bullet_state = 'ready'

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #check keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state=='ready':
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
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

    #Bullet movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY-=bulletY_change
        if bulletY<=0:
            bulletY=480
            bullet_state='ready'

        
    


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()