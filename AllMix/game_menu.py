import pygame
from space_invader import game1
from game_db import game_db
pygame.init()

game_db = game_db()

screen = pygame.display.set_mode((800,600))
BG = pygame.image.load('background.jpg')
BG_fit = pygame.transform.scale(BG,(800,600))

textFont = pygame.font.SysFont('None', 30)
def draw_text(text,font,color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
BLUE=(0,0,255)
WHITE=(255,255,255)
PURPLE =(128,0,128)
def game():
    running = True 
    while running:
        screen.fill((0,0,0))
        draw_text("game",textFont,WHITE,screen,20,20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
        pygame.display.update()
def options():
    running = True 
    while running:
        screen.fill((0,0,0))
        draw_text("options",textFont,WHITE,screen,20,20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
        pygame.display.update()

def main_menu():
    running=True
    while running:
        screen.blit(BG_fit, (-1,-1))
        draw_text("Main menu",textFont,WHITE,screen,20,20)
        mx, my = pygame.mouse.get_pos()
        button1 =pygame.Rect(40,100,200,40)
        button2 =pygame.Rect(40,200,200,40)
        button3 = pygame.Rect(40,300,200,40)
        if button1.collidepoint((mx,my)):
            if click:
                game1()
        if button2.collidepoint((mx,my)):
            if click:
                options()
        if button3.collidepoint((mx,my)):
            if click:
                show_players_list()
                #get_players_list()
        pygame.draw.rect(screen,PURPLE,button3)
        draw_text("Show Players",textFont,WHITE,screen,button3.x+40,button3.y+10)
        pygame.draw.rect(screen,PURPLE,button1)
        draw_text("Start Game",textFont,WHITE,screen,button1.x+40,button1.y+10)
        pygame.draw.rect(screen,PURPLE,button2)
        draw_text("Options",textFont,WHITE,screen,button2.x+40,button2.y+10)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_db.close_db()
                running=False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    click = True
        if running==True: pygame.display.update()

def get_players_list():
    
    players = game_db.player_list()
    print(players)
    return players
def show_players_list():
    running=True
    screen.fill((0,0,0))
    text_space =40
    players_list = get_players_list()
    x,y=300,40
    x_change=100
    draw_text("Players",textFont,WHITE,screen,x,y)
    draw_text("Score",textFont,WHITE,screen,x+x_change,y)
    for player in players_list:
        y+=text_space
        draw_text(player[1],textFont,BLUE,screen,x,y)
        draw_text(str(player[2]),textFont,PURPLE,screen,x+x_change,y)
    while running:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_db.close_db()
                running=False
                
        if running==True: pygame.display.update()
main_menu()
