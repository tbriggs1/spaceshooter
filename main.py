import pygame
from ships.ship import Ship
from ships.player_ship import PlayerShip
from ammo.bullet import Bullet
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
    enemy_ship = Ship(200, "green", 40, screen, enemy_pos)


    angle = 0
    while running:
        screen.fill("black")
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_ship.Fire()

        player_ship = PlayerShip(400, "blue", 40, screen, player_pos, dt)

        player_ship.SetPlayerPosition()

        player_ship.drawBullets()

        enemy_ship.rotate(1)

        enemy_ship.update_rotation()

        player_ship.rotate(player_ship.angle)
        player_ship.update_rotation()

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        await asyncio.sleep(0)

asyncio.run(main())

