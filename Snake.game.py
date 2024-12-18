import pygame
import random

pygame.init()

# Create game window
game_window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Devoloped by Genius_Aarush ")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# FPS and clock
fps = 60
clock = pygame.time.Clock()

# Font for displaying score
font = pygame.font.SysFont(None, 45)

def score_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, (x, y))

def snake_plot(game_window, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(black)
        score_screen("Welcome to Snakes!", green, 260, 250)
        score_screen("Press Spacebar to Start", green, 239, 279)
        score_screen("Game Devoloper: @Aarush", green, 217, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start game on SPACE key press
                    return
        pygame.display.update()

def game_loop():
    # Game variables
    snake_x = 50
    snake_y = 30
    snake_size = 23
    velocity_x = 0
    velocity_y = 0
    score = 0

    # Food variables
    screen_width = 800
    screen_height = 500
    food_size = 24
    food_x = random.randint(0, screen_width - food_size)
    food_y = random.randint(0, screen_height - food_size)


    snk_list = []
    snk_length = 1
    game_over = False
    exit_game = False

    while not exit_game:
        if game_over:
            game_window.fill(black)
            score_screen(f"Game Over! Score: {score}", red, 250, 200)
            score_screen("Press Enter to Restart or Esc to Exit", red, 150, 240)
            score_screen("Game Devoloper: @Aarush", green, 217, 100)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Restart on Enter key press
                        game_loop()
                    if event.key == pygame.K_ESCAPE:  # Exit on Escape key press
                        exit_game = True

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and velocity_x != -2:
                        velocity_x = 6
                        velocity_y = 0
                    if event.key == pygame.K_LEFT and velocity_x != 2:
                        velocity_x = -6
                        velocity_y = 0
                    if event.key == pygame.K_UP and velocity_y != 2:
                        velocity_y = -6
                        velocity_x = 0
                    if event.key == pygame.K_DOWN and velocity_y != -2:
                        velocity_y = 6
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            # Check for collision with food
            if abs(snake_x - food_x) < food_size and abs(snake_y - food_y) < food_size:
                score += 1
                snk_length += 5
                food_x = random.randint(0, screen_width - food_size)
                food_y = random.randint(0, screen_height - food_size)

            # Clear the screen
            game_window.fill(black)

            # Display score
            score_screen(f"Score: {score}", red, 5, 5)

            # Update snake head and body
            head = [snake_x, snake_y]
            snk_list.append(head)

            # Keep snake length under control
            if len(snk_list) > snk_length:
                del snk_list[0]

            # Check for collision with itself or boundaries
            if head in snk_list[:-1] or snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            # Draw food and snake
            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
            snake_plot(game_window, green, snk_list, snake_size)

            # Update the display
            pygame.display.update()

            # Control frame rate
            clock.tick(fps)

# Run the game
welcome()
game_loop()

pygame.quit()
quit()
