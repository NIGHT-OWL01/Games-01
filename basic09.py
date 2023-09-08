#multiple enemies
import pygame
import random
import math

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
enemyImg =[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemy=6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)
#Bullet

#Ready - You can't see the bullet on the screen
#Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX= 0
bulletY=480
bulletX_change=0
bulletY_change=1
bullet_state = 'ready'

score_value=0
def enemy(x, y,i):
    screen.blit(enemyImg[i], (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))
def isCollision(enemyX, enemyY):
    global bulletY
    distance = math.sqrt((math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2)))
    if distance<25:
        bulletY=480
        return True
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
    
    for i in range(num_of_enemy):
        #Enemy movement
        enemyX[i] += enemyX_change[i]
        #adding boudary
        if enemyX[i] <=0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        collision = isCollision(enemyX[i], enemyY[i])
        if collision:
            score_value+=1
            print(score_value)
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(0,150)
        enemy(enemyX[i], enemyY[i], i)
    #Bullet movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY-=bulletY_change
        if bulletY<=0:
            bulletY=480
            bullet_state='ready'
    
    
        

    player(playerX, playerY)
    
    pygame.display.update()