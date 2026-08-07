import pygame
import time

from display.pages import IconPage


pygame.init()


screen = pygame.display.set_mode(
    (2560,1440),
    pygame.FULLSCREEN
)


from display.config import load_config

config = load_config()

icon_dir = config["assets"]["icon_dir"]
pages = []

for item in config["pages"]:
    pages.append(
        IconPage(
            f"{icon_dir}/{item['icon']}",
            item["name"],
            item["slogan"]
        )
    )


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
