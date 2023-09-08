#title(pygame.display.set_caption()), icon(icon = pygame.image.load('ufo.png') /n pygame.display.set_icon(icon)) 
# background (screen.fill((255, 0, 0)))
import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

running=True

# Title and ICON->(32x32 px)
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #change background
    screen.fill((255, 0, 0))
    #update display window for any changes
    pygame.display.update()