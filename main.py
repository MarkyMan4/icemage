import pygame

pygame.init()
screen = pygame.display.set_mode((640, 640))

clock = pygame.time.Clock()

running = True

x = 10
y = 10
move_speed = 200
delta_time = 0

while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 50))

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
