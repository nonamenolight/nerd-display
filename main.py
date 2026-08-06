import pygame
import time

from display.pages import IconPage


pygame.init()


screen = pygame.display.set_mode(
    (2560,1440),
    pygame.FULLSCREEN
)


pages = [

    IconPage(
        "assets/png/tux.png",
        "Linux",
        "The foundation of everything"
    ),

    IconPage(
        "assets/png/docker.png",
        "Docker",
        "Container Runtime"
    ),

    IconPage(
        "assets/png/kubernetes.png",
        "Kubernetes",
        "Container Orchestration"
    ),

]


index = 0


clock = pygame.time.Clock()


while True:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


    pages[index].render(screen)

    pygame.display.flip()


    time.sleep(5)


    index = (
        index + 1
    ) % len(pages)
