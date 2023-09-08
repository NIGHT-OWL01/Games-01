import pygame,sys
from random import randint

pygame.init()

screen = pygame.display.set_mode((1200,720))
clock = pygame.time.Clock()

camera_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("#71ddee")
    camera_group.update()
    camera_group.draw(screen)
    pygame.display.update()


    clock.tick(60)