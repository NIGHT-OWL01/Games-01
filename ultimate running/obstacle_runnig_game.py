import pygame
pygame.init()

screen  = pygame.display.set_mode((800,600))

running = True
pygame.display.set_caption('ultimate running')

#background
background = pygame.image.load('background.jpg')

#player
playerImg=pygame.image.load('player.png')
playerX=50
playerY=536
player_action = 'idle'
playerY_change =150 #jump

playerWidth = 50

def player(x,y):
    screen.blit(playerImg, (x,y))

playerRect = playerImg.get_rect()
playerRect.x = playerX
playerRect.w = playerWidth
print(playerRect)

#score
score_value=0
scoreFont = pygame.font.Font('freesansbold.ttf',32)

def show_score():
    scoreText = scoreFont.render('Score :'+ str(score_value), True, (0, 255, 0))
    screen.blit(scoreText, (0,0))
#Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX=736
enemyY=536
enemyX_change=0.5

enemyRect = enemyImg.get_rect()
enemyRect.y=enemyY
def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#enemy 2
enemy2Img = pygame.image.load('enemy2.png')
enemy2X=736
enemy2Y=436
enemy2X_change=0.5

enemy2Rect = enemy2Img.get_rect()
enemy2Rect.y=enemyY
def enemy2(x,y):
    screen.blit(enemy2Img,(x,y))

#check collision
overFont=pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over_text = overFont.render('GAME OVER',True,(255,0,0))
    screen.blit(over_text,(200,250))

#difficulties list
difficulties = ['easy','medium', 'hard', 'very hard' , 'very very hard', 'extreme']
difficultyFont = pygame.font.Font('freesansbold.ttf',32)
difficulty_level=0
def show_difficulty(i):
    difficultyText = difficultyFont.render('Level : '+difficulties[i], True, (250,100,100))
    screen.blit(difficultyText, (300,0))

current_speed=0
while running:
    screen.fill([255,255,255])
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if player_action=='idle':
                    print('jump')
                    player_action='jumped'
                    playerY -= playerY_change
            if event.key == pygame.K_DOWN:
                playerY=536
            if event.key == pygame.K_F5:
                enemyX=736
                enemyX_change=current_speed
                print('refresh')
    #gravity
    if playerY<536:
        playerY+=0.2

    if playerY>=535:
        player_action='idle'
    #Enemy movement
    enemyX -=enemyX_change
    enemy2X -=enemy2X_change
    
    if enemyX <=0:
        enemyX=736
        score_value += 1
        #Increse difficulty
        if score_value%5==0:
            enemyX_change+=.1
            if difficulty_level<len(difficulties)-1:
                difficulty_level+=1
            else:
                difficulty_level=len(difficulties)-1
            current_speed=enemyX_change
            print(enemyX_change)
    enemyRect.x=enemyX
    playerRect.y=playerY

    
    #detect collision
    if playerRect.colliderect(enemyRect):
        enemyX_change=0
        game_over_text()
        
    show_score()
    show_difficulty(difficulty_level)
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    enemy2(enemy2X,enemy2Y)
    pygame.display.update()

