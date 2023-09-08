#initialize and game loop
import pygame
#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((900,700))


#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False