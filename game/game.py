import pygame
from game import config
from game import colors

colors.SKY_BLUE


class Game:
    def __init__(self):
        pass

    def run(self):
        pygame.init()
        # screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        clock = pygame.time.Clock()
        background_image = pygame.image.load(config.ASSETS_PATH / "background.png")
        background_image = pygame.transform.scale(
            background_image, pygame.display.get_window_size()
        )

        running = True

        x = 10
        y = 10
        move_speed = 200
        delta_time = 0

        while running:
            # screen.blit(background_image)
            screen.fill(colors.SKY_BLUE)

            pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                x += move_speed * delta_time
            if keys[pygame.K_a]:
                x -= move_speed * delta_time
            if keys[pygame.K_w]:
                y -= move_speed * delta_time
            if keys[pygame.K_s]:
                y += move_speed * delta_time

            pygame.display.flip()
            delta_time = clock.tick(60) / 1000

        pygame.quit()
