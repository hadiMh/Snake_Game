import pygame
from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SQUARE_LENGTH
from constants import Colors

from game_classes import Snake, Food

pygame.init()
main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()


def draw_grid(surface):
    square_length = SQUARE_LENGTH
    square_color = None

    for i in range(int(SCREEN_WIDTH / square_length)):
        for j in range(int(SCREEN_HEIGHT / square_length)):
            if (i + j) % 2 == 0:
                square_color = Colors.M_BLUE_LIGHT
            else:
                square_color = Colors.WHITE

            rect = pygame.Rect((i * square_length, j * square_length), (square_length,) * 2)
            pygame.draw.rect(surface, square_color, rect)


snake = Snake()
food = Food()

running = True
while running:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pressed_keys = pygame.key.get_pressed()

    main_screen.fill(Colors.WHITE)
    draw_grid(main_screen)

    main_screen.blit(food.surface, food.rect)

    snake.update(pressed_keys)
    # main_screen.blit(snake.surface, snake.rect)
    snake.draw(main_screen)

    pygame.display.flip()

    clock.tick(10)

pygame.quit()
