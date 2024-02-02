import pygame
from ships.ship import Ship
from ships.player_ship import PlayerShip
import asyncio

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
async def main():

    global running, dt

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    enemy_pos = pygame.Vector2(screen.get_width() / 2.5, screen.get_height() / 2.5)

    while running:
        keys = pygame.key.get_pressed()

        screen.fill("purple")
        # poll for events
        # pygame.QUIT event means the user clicked X to close your windowdddd
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.Vector2(screen.get_width() < player_pos.x):
                running = False
            if pygame.Vector2(screen.get_height() < player_pos.y):
                running = False
            if player_pos.y < 0 or player_pos.x < 0:
                running = False


        player_ship = PlayerShip(400, "blue", 40, screen, player_pos, keys, dt)
        enemy_ship = Ship(200, "Green", 40, screen, enemy_pos)

        player_ship.SetPlayerPosition()
        player_ship.Fire()

         # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        await asyncio.sleep(0)

asyncio.run(main())

