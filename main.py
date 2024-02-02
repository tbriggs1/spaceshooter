import pygame
from ship import Ship


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.Vector2(screen.get_width() < player_pos.x):
                running = False
            if pygame.Vector2(screen.get_height() < player_pos.y):
                running = False
            if player_pos.y < 0 or player_pos.x < 0:
                running = False


        screen.fill("purple")

        pygame.display.Info()

        pygame.draw.circle(screen, "red", player_pos, 40)

        print(Ship(200, keys).speed)


        if keys[pygame.K_w]:
            player_pos.y -= 500 * dt
        if keys[pygame.K_s]:
            player_pos.y += 500 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 500 * dt
        if keys[pygame.K_d]:
            player_pos.x += 500 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()

main()