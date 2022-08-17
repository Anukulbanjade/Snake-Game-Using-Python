import random
import pygame

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("----Snakes----")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0
score = 0
snake_size = 30
fps = 30
food_x=0
food_y=0


clock = pygame.time.Clock()

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 5
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = - 5
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - 5
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 5
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x) < 6 and abs(snake_y - food_y < 6):
        score += 1
        print("Score= ", score)
        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)

    gameWindow.fill(black)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow,white, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
