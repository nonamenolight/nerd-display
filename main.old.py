import pygame
import time

pygame.init()

screen = pygame.display.set_mode(
    (800, 600)
)

pygame.display.set_caption(
    "Nerd Display"
)

font = pygame.font.Font(
    None,
    80
)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    text = font.render(
        "NERD LAB",
        True,
        (255, 255, 255)
    )

    rect = text.get_rect(
        center=(400,300)
    )

    screen.blit(
        text,
        rect
    )

    pygame.display.flip()

pygame.quit()
