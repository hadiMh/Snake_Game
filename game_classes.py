import pygame
import random
from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_ESCAPE
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SQUARE_LENGTH
from constants import Colors


class Snake(pygame.sprite.Sprite):
    SNAKE_SQUARES_LENGTH = SQUARE_LENGTH
    SNAKE_SQUARES_COLOR = Colors.M_PINK
    DIRECTIONS = {
        'UP': (0, -1 * SNAKE_SQUARES_LENGTH),
        'DOWN': (0, SNAKE_SQUARES_LENGTH),
        'RIGHT': (SNAKE_SQUARES_LENGTH, 0),
        'LEFT': (-1 * SNAKE_SQUARES_LENGTH, 0),
    }

    def __init__(self):
        super(Snake, self).__init__()

        self.surface = pygame.Surface((Snake.SNAKE_SQUARES_LENGTH, Snake.SNAKE_SQUARES_LENGTH))
        self.surface.fill(Snake.SNAKE_SQUARES_COLOR)
        self.rect = self.surface.get_rect(
            center=(
                (SCREEN_WIDTH / 2) - Snake.SNAKE_SQUARES_LENGTH / 2,
                (SCREEN_HEIGHT / 2) - Snake.SNAKE_SQUARES_LENGTH / 2,
            )
        )
        self.direction = 'UP'
        self.snake_body = [self.rect.copy()]

    def update(self, keys_pressed):
        if keys_pressed[K_UP]:
            self.direction = 'UP'
        elif keys_pressed[K_DOWN]:
            self.direction = 'DOWN'
        elif keys_pressed[K_LEFT]:
            self.direction = 'LEFT'
        elif keys_pressed[K_RIGHT]:
            self.direction = 'RIGHT'

        self.rect.move_ip(Snake.DIRECTIONS[self.direction])
        self.snake_body.insert(0, self.rect.copy())
        self.snake_body.pop()

        if self.rect.x < 0:
            self.rect.x += SCREEN_WIDTH
        if self.rect.y < 0:
            self.rect.y += SCREEN_HEIGHT
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x -= SCREEN_WIDTH + SQUARE_LENGTH
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y -= SCREEN_HEIGHT + SQUARE_LENGTH

    def draw(self, surface):
        for rect in self.snake_body:
            pygame.draw.rect(surface, Snake.SNAKE_SQUARES_COLOR, rect)


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super(Food, self).__init__()

        self.surface = pygame.Surface((Snake.SNAKE_SQUARES_LENGTH, Snake.SNAKE_SQUARES_LENGTH))
        self.surface.fill(Colors.WHITE)
        pygame.draw.circle(self.surface, Colors.RED, (Snake.SNAKE_SQUARES_LENGTH / 2,) * 2, 5)
        self.rect = self.surface.get_rect(
            center=(
                (random.randint(0, SCREEN_WIDTH) // SQUARE_LENGTH + 0.5) * SQUARE_LENGTH,
                (random.randint(0, SCREEN_HEIGHT) // SQUARE_LENGTH + 0.5) * SQUARE_LENGTH,
            )
        )