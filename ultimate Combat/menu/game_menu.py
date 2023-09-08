import pygame
from space_invader import game1
pygame.init()

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
    while True:
        screen.blit(BG_fit, (-1,-1))
        draw_text("Main menu",textFont,WHITE,screen,20,20)
        mx, my = pygame.mouse.get_pos()
        button1 =pygame.Rect(40,100,200,40)
        button2 =pygame.Rect(40,200,200,40)

        if button1.collidepoint((mx,my)):
            if click:
                game1()
        if button2.collidepoint((mx,my)):
            if click:
                options()
        pygame.draw.rect(screen,PURPLE,button1)
        draw_text("Start Game",textFont,WHITE,screen,button1.x+40,button1.y+10)
        pygame.draw.rect(screen,PURPLE,button2)
        draw_text("Options",textFont,WHITE,screen,button2.x+40,button2.y+10)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    click = True
        pygame.display.update()


main_menu()