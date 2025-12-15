import pygame
from enum import Enum

pygame.init()

TILESIZE = 32
GRID_WIDTH = 32
GRID_HEIGHT = 20
SCREEN_WIDTH = GRID_WIDTH * TILESIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILESIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, 48)

clock = pygame.time.Clock()

score = 0

class State(Enum):
    IDLE = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([32, 32])
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect()

        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2

        self.speed = 8
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()