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
    
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def player_input(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                self.snake.change_direction((BLOCK_SIZE, 0))

            elif event.key == pygame.K_LEFT:
                self.snake.change_direction((-BLOCK_SIZE, 0))

            elif event.key == pygame.K_UP:
                self.snake.change_direction((0, -BLOCK_SIZE))

            elif event.key == pygame.K_DOWN:
                self.snake.change_direction((0, BLOCK_SIZE))

    def draw(self):
        #self.snake.draw()
        self.apple.draw()
        pygame.display.update()

game = Game()

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        game.player_input(event)

    game.draw()

pygame.quit()