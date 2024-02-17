import pygame
from ships.ship import Ship
from ships.player_ship import PlayerShip
from ships.enemy_ship_one import EnemyShipOne
from ammo.bullet import Bullet
import asyncio

pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.font.init()
font_size = 24
game_font = pygame.font.Font(None, font_size)



clock = pygame.time.Clock()
running = True
dt = 0

async def main():
    enemy_ships = ["sprites/Ship2.png", "sprites/Ship3.png"]
    player_ship = "sprites/player_idle.png"
    global running, dt
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    enemy_pos = pygame.Vector2(screen.get_width() / 2.5, -10)
    player_ship = PlayerShip(100, "blue", screen, player_pos, dt, player_ship)
    second_enemy_ship = EnemyShipOne(100, "blue", screen, enemy_pos, dt, enemy_ships[0])

    all_ships = pygame.sprite.Group()


    all_ships.add(player_ship, second_enemy_ship)

    number_to_display = 0
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



        text_color = (255, 255, 255)

        text_surface = game_font.render("Score: " +  str(number_to_display), True, text_color)

        text_position = (50, 50)  # Example position (x, y)
        screen.blit(text_surface, text_position)



        player_ship.SetPlayerPosition(dt)
        player_ship.drawBullets()

        second_enemy_ship.UpdatePosition(dt)


        # collide = second_enemy_ship.rect.colliderect(player_ship)
        #
        for bullet in player_ship.bullets:
            hit = second_enemy_ship.rect.collidepoint(bullet.bullet_pos.x, bullet.bullet_pos.y)
            if second_enemy_ship.hitbox.colliderect(bullet.rect):
                print("Hit")
                number_to_display += 1
                player_ship.bullets.remove(bullet)
                all_ships.remove(second_enemy_ship)
                break

        # print(player_points)
        all_ships.update()  # Update all sprites in the group
        all_ships.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        await asyncio.sleep(0)

asyncio.run(main())

