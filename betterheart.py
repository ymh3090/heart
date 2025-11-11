import pygame
import math
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 1200, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game-Grade Heart ❤️")

clock = pygame.time.Clock()

# Colors
RED = (255, 50, 70)
GLOW = (255, 100, 120)
BLACK = (0, 0, 0)

# Function to draw a heart shape using polar equation
def draw_heart(surface, scale=1.0, alpha=255):
    heart_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for angle in range(0, 360):
        t = math.radians(angle)
        x = 16 * math.sin(t)**3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        x *= 15 * scale
        y *= 15 * scale
        pygame.draw.circle(
            heart_surface,
            (RED[0], RED[1], RED[2], alpha),
            (WIDTH//2 + int(x), HEIGHT//2 - int(y)),
            4
        )
    surface.blit(heart_surface, (0, 0))

# Pulse animation
pulse = 0
grow = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Heart pulse
    if grow:
        pulse += 0.01
        if pulse >= 0.2:
            grow = False
    else:
        pulse -= 0.01
        if pulse <= -0.2:
            grow = True

    # Glow layers
    for i in range(3, 0, -1):
        draw_heart(screen, scale=1 + pulse + i*0.02, alpha=40 * i)

    # Main heart
    draw_heart(screen, scale=1 + pulse)

    # Text
    font = pygame.font.SysFont("Arial", 60, True)
    text = font.render(" ", True, (255, 255, 255))
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 30))

    pygame.display.flip()
    clock.tick(60)
