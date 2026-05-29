import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLOCK_SIZE = 20
SPEED = 10

original_image = pygame.image.load("apple.png")
image = pygame.transform.scale(original_image, (20, 20))

score = 0
font = pygame.font.SysFont(None, 40)

running = True

clock = pygame.time.Clock()



class Snake:

    def __init__(self):
        self.snake_body = [[200, 300], [180, 300], [160, 300]]
        self.direction = (BLOCK_SIZE, 0)
        self.grow = False
        self.reset = False

    def change_direction(self, direction):
        if (
        self.direction[0] == -direction[0]
        and self.direction[1] == -direction[1]
        ):
            return

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
        
        if self.snake_body[0] in self.snake_body[1:]:
            self.reset = True

        if (head[0] >= WIDTH or
            head[0] < 0 or
            head[1] >= HEIGHT or
            head[1] < 0
        ): 
            self.reset = True

    def draw(self):
        for part in self.snake_body:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (part[0], part[1], BLOCK_SIZE, BLOCK_SIZE)
            )
    
    def snake_respawn(self):
        self.snake = Snake()

class Apple:

    def __init__(self):
        self.respawn()
    
    def respawn(self):
        self.x = random.randrange(0, WIDTH, BLOCK_SIZE)
        self.y = random.randrange(0, HEIGHT, BLOCK_SIZE)

    def draw(self):
        screen.blit(image, (self.x, self.y))

class Game:

    def pause_game(self):
        paused = True

        while paused:

            self.draw()

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    paused = False
    
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()

    def player_input(self, event):
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT and self.snake.direction != ((-BLOCK_SIZE, 0)):
                self.snake.change_direction((BLOCK_SIZE, 0))

            elif event.key == pygame.K_LEFT and self.snake.direction != ((BLOCK_SIZE, 0)):
                self.snake.change_direction((-BLOCK_SIZE, 0))

            elif event.key == pygame.K_UP and self.snake.direction != ((0, BLOCK_SIZE)):
                self.snake.change_direction((0, -BLOCK_SIZE))

            elif event.key == pygame.K_DOWN and self.snake.direction != ((0, -BLOCK_SIZE)):
                self.snake.change_direction((0, BLOCK_SIZE))

    def update(self):
        global score
        self.snake.move()

        apple_pos = [self.apple.x, self.apple.y]
        self.snake.apple_collision(apple_pos)
  

        if self.snake.grow:
            self.apple.respawn()

        if self.snake.reset:
            self.game_over()


        if self.snake.snake_body[0] == apple_pos:
            score += 10
        
        if self.snake.reset:
            self.game_over()

            self.snake = Snake()
            self.apple = Apple()
            self.snake.reset = False
            score = 0

    def game_over(self):
        screen.fill((0, 0, 0))

        text1 = font.render("GAME OVER", True, (255, 0, 0))
        text2 = font.render(f"Score: {score}", True, (255, 255, 255))

        screen.blit(text1, (200, 250))
        screen.blit(text2, (220, 300))

        pygame.display.update()

        pygame.time.delay(2000)

    def draw(self):
        screen.fill((0, 0, 0))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        self.snake.draw()
        self.apple.draw()
        pygame.display.update()

game = Game()

game.pause_game()

while running:

    clock.tick(SPEED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        game.player_input(event)
        

    game.draw()
    game.update()

pygame.quit()
