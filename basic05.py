#added boundary to player movement
import pygame
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
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    #adding boudary
    if playerX <=0:
        playerX=0
    elif playerX >= 736:
        playerX=736
    player(playerX, playerY)
    pygame.display.update()