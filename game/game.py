import pygame
from game import config
from game import colors
from game.player import Player


class Game:
    def __init__(self):
        self._player = Player()
        self._enemies = pygame.sprite.Group()

    def run(self):
        pygame.init()
        # screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self._player.x = screen.width / 2
        self._player.y = screen.height / 2

        clock = pygame.time.Clock()
        # background_image = pygame.image.load(config.ASSETS_PATH / "background.png")
        # background_image = pygame.transform.scale(
        #     background_image, pygame.display.get_window_size()
        # )

        running = True
        delta_time = 0

        while running:
            # screen.blit(background_image)
            screen.fill(colors.SKY_BLUE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.blit(self._player.image, (self._player.x, self._player.y))
            self._player.update(delta_time)

            pygame.display.flip()
            delta_time = clock.tick(60) / 1000

        pygame.quit()
