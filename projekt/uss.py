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
        self.snake_body = [[200, 300], [180, 300], [160, 300]]
        self.direction = (BLOCK_SIZE, 0)
        self.grow = False

    def change_direction(self, direction):
        self.direction = direction

    def apple_collision(self, apple_pos):
        if self.snake_body[0] == apple_pos:
            self.grow = True

    def move(self):
        head = self.snake_body[0].copy()

        head[0] += self.direction[0]
        head[1] += self.direction[1]

        self.snake_body.insert(0, head)

        if self.grow:
            self.grow = False
        else:
            self.snake_body.pop()

    def draw(self):
        for part in self.snake_body:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (part[0], part[1], BLOCK_SIZE, BLOCK_SIZE)
            )


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

    def update(self):
        self.snake.move()

        apple_pos = [self.apple.x, self.apple.y]
        self.snake.apple_collision(apple_pos)

        if self.snake.grow:
            self.apple.respawn()

    def draw(self):
        screen.fill((0, 0, 0))
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()


game = Game()

while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        game.player_input(event)

    game.update()
    game.draw()

pygame.quit()