import pygame


class IconPage:
    def __init__(self, image_path, title, subtitle=""):
        self.image_path = image_path
        self.title = title
        self.subtitle = subtitle

        self.image = pygame.image.load(
            image_path
        ).convert_alpha()


    def fit_image(self, max_size=512):

        width, height = self.image.get_size()

        ratio = min(
            max_size / width,
            max_size / height
        )

        new_size = (
            int(width * ratio),
            int(height * ratio)
        )

        return pygame.transform.smoothscale(
            self.image,
            new_size
        )


    def render(self, screen):

        screen.fill((0, 0, 0))

        width, height = screen.get_size()


        # logo
        image = self.fit_image(512)

        rect = image.get_rect(
            center=(width // 2, height // 2 - 100)
        )

        screen.blit(
            image,
            rect
        )


        # title
        title_font = pygame.font.SysFont(
            "DejaVu Sans",
            90
        )

        title = title_font.render(
            self.title,
            True,
            (255,255,255)
        )

        title_rect = title.get_rect(
            center=(width//2, height//2 + 250)
        )

        screen.blit(
            title,
            title_rect
        )


        # subtitle
        if self.subtitle:

            sub_font = pygame.font.SysFont(
                "DejaVu Sans",
                45
            )

            sub = sub_font.render(
                self.subtitle,
                True,
                (180,180,180)
            )

            sub_rect = sub.get_rect(
                center=(width//2, height//2 + 330)
            )

            screen.blit(
                sub,
                sub_rect
            )