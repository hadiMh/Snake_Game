import pygame
from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import Colors

pygame.init()
main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

running = True
while running:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    main_screen.fill(Colors.WHITE)

    pygame.display.flip()

    clock.tick(20)

pygame.quit()
