import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
BLOCK_SIZE = 20
SPEED = 15
original_image = pygame.image.load("apple.png")
image = pygame.transform.scale(original_image, (20, 20))


running = True
clock = pygame.time.Clock()

class Snake:

    def __init__(self):
        self.respawn()
        self.snake_body = [[290, 300], [270, 300], [250, 300]]
        self.direction = (BLOCK_SIZE, 0)


    def respawn(self):
        pass

    def apple_collision(self, apple_pos):
        snake_head = self.snake_body[0]
        new_head = snake_head[0] + 20

        if self.snake_head[0] == apple_pos:
            self.snake_body.insert(0, new_head)
    
    def change_direction(self, direction):
        self.direction = direction

    def draw(self):
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
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

pygame.quit()