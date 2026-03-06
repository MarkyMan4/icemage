import pygame
from game.config import PLAYER_MOVE_SPEED, PLAYER_IMAGE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load(PLAYER_IMAGE), (64, 64))
        self._is_image_flipped = False

    def update(self, delta_time: float):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += PLAYER_MOVE_SPEED * delta_time
            if self._is_image_flipped:
                self.image = pygame.transform.flip(
                    self.image, flip_x=True, flip_y=False
                )
                self._is_image_flipped = False
        if keys[pygame.K_a]:
            self.x -= PLAYER_MOVE_SPEED * delta_time
            if not self._is_image_flipped:
                self.image = pygame.transform.flip(
                    self.image, flip_x=True, flip_y=False
                )
                self._is_image_flipped = True
        if keys[pygame.K_w]:
            self.y -= PLAYER_MOVE_SPEED * delta_time
        if keys[pygame.K_s]:
            self.y += PLAYER_MOVE_SPEED * delta_time
