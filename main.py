import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cybersecurity Awareness Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 7

# Threat settings
threat_size = 50
threat_pos = [random.randint(0, WIDTH - threat_size), 0]
threat_speed = 5
threats = [threat_pos]

# Shield settings
shield_size = 30
shield_pos = [random.randint(0, WIDTH - shield_size), 0]
shield_speed = 5
shields = [shield_pos]

# Score
score = 0

# Set the frame rate
clock = pygame.time.Clock()
FPS = 30

# Load fonts
font = pygame.font.SysFont("monospace", 35)

# Load character images
player_image = pygame.image.load("player.png")  # Ensure you have a player.png
player_image = pygame.transform.scale(player_image, (player_size, player_size))

# Load threat image
threat_image = pygame.image.load("virus.png")  # Ensure you have a virus.png
threat_image = pygame.transform.scale(threat_image, (threat_size, threat_size))

# Load shield image
shield_image = pygame.image.load("shield.png")  # Ensure you have a shield.png
shield_image = pygame.transform.scale(shield_image, (shield_size, shield_size))

# Check for collisions
def detect_collision(player_pos, obj_pos, obj_size):
    p_x, p_y = player_pos
    o_x, o_y = obj_pos

    if (o_x < p_x < o_x + obj_size) or (o_x < p_x + player_size < o_x + obj_size):
        if (o_y < p_y < o_y + obj_size) or (o_y < p_y + player_size < o_y + obj_size):
            return True
    return False

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Update threats
    for threat in threats:
        threat[1] += threat_speed
        if threat[1] >= HEIGHT:
            threat[0] = random.randint(0, WIDTH - threat_size)
            threat[1] = 0

    # Update shields
    for shield in shields:
        shield[1] += shield_speed
        if shield[1] >= HEIGHT:
            shield[0] = random.randint(0, WIDTH - shield_size)
            shield[1] = 0
    
    # Draw player
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    # Draw threats
    for threat in threats:
        screen.blit(threat_image, (threat[0], threat[1]))

    # Draw shields
    for shield in shields:
        screen.blit(shield_image, (shield[0], shield[1]))

    # Check for collisions with threats
    for threat in threats:
        if detect_collision(player_pos, threat, threat_size):
            print(f"Game Over! Your score: {score}")
            running = False
    
    # Check for collisions with shields
    for shield in shields:
        if detect_collision(player_pos, shield, shield_size):
            score += 10
            shields.remove(shield)
            new_shield = [random.randint(0, WIDTH - shield_size), 0]
            shields.append(new_shield)

    # Display score
    score_text = font.render("Score: {0}".format(score), True, WHITE)
    screen.blit(score_text, (WIDTH - 200, HEIGHT - 40))
    
    # Update the screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()