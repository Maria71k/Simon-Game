import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLORS = [RED, GREEN, BLUE, YELLOW]
SQUARE_SIZE = 150
PADDING = 50
DELAY = 1

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simon Game")

# Initialize variables
sequence = []
player_sequence = []
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate a new color and add it to the sequence
    new_color = random.choice(COLORS)
    sequence.append(new_color)

    # Display the sequence
    screen.fill((0, 0, 0))
    pygame.display.update()
    time.sleep(DELAY)

    for color in sequence:
        pygame.draw.rect(screen, color, (WIDTH // 2 - SQUARE_SIZE // 2, HEIGHT // 2 - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE))
        pygame.display.update()
        time.sleep(DELAY)
        screen.fill((0, 0, 0))
        pygame.display.update()
        time.sleep(DELAY)

    # Player's turn
    player_sequence.clear()
    for i in range(len(sequence)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH // 2 - SQUARE_SIZE // 2 <= x <= WIDTH // 2 + SQUARE_SIZE // 2 and HEIGHT // 2 - SQUARE_SIZE // 2 <= y <= HEIGHT // 2 + SQUARE_SIZE // 2:
                    player_sequence.append(COLORS.index(new_color))
                    pygame.draw.rect(screen, new_color, (WIDTH // 2 - SQUARE_SIZE // 2, HEIGHT // 2 - SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE))
                    pygame.display.update()
                    time.sleep(DELAY)
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    time.sleep(DELAY)

    # Check if player's sequence matches the original sequence
    if player_sequence != sequence:
        print("Game Over! Your sequence:", player_sequence, "Correct sequence:", sequence)
        break

# Quit Pygame
pygame.quit()
