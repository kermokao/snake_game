import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
BLOCK_SIZE = 20
original_image = pygame.image.load("apple.png")
image = pygame.transform.scale(original_image, (20, 20))

running = True
clock = pygame.time.Clock()

class Snake:

    def __init__(self):
        pass

class Apple:

    def __init__(self):
        self.respawn()
    
    def respawn(self):
        self.x = random.randrange(0, WIDTH, BLOCK_SIZE)
        self.y = random.randrange(0, HEIGHT, BLOCK_SIZE)

    def draw(self):
        screen.blit(image, (self.x, self.y))


class Game:
    pass


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()