import pygame
from ships.ship import Ship
from ships.player_ship import PlayerShip
from ships.enemy_ship_one import EnemyShipOne
from ammo.bullet import Bullet
import asyncio
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.font.init()
font_size = 24
game_font = pygame.font.Font(None, font_size)



clock = pygame.time.Clock()
running = True
dt = 0

async def main():

    player_ship = "sprites/player_idle.png"
    global running, dt
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    player_ship = PlayerShip(100, "blue", screen, player_pos, dt, player_ship)
    # enemy_pos = pygame.Vector2(screen.get_width() / rand_pos, -120)




    all_ships = pygame.sprite.Group()
    all_ships.add(player_ship)

    rand_pos_x = random.uniform(0, screen.get_width())

    bullets_to_remove = set()
    enemy_ships = [

    ]

    for ship in enemy_ships:
        all_ships.add(ship)

    number_to_display = 0
    enemy_spawn_interval = 5.0  # Seconds between enemy spawns
    enemy_spawn_timer = enemy_spawn_interval

    while running:
        screen.fill("black")
        # poll for events
        # pygame.QUIT event means the user clicked X to close your windowdddd
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if pygame.Vector2(screen.get_width() < player_pos.x):
            #     running = False
            # if pygame.Vector2(screen.get_height() < player_pos.y):
            #     running = False
            # if player_pos.y < 0 or player_pos.x < 0:
            #     running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_ship.Fire()

        enemy_spawn_timer -= dt

        if enemy_spawn_timer <= 0:
            enemy_spawn_timer = enemy_spawn_interval

            ship_width = 125  # Assume this is the maximum width of your enemy ships

            random_post_list = []
            for _ in range(30):
                new_rand_pos_xx = random.uniform(0, screen.get_width() - ship_width)
                new_enemy_postx = pygame.Vector2(new_rand_pos_xx, -150)
                random_post_list.append(new_enemy_postx)

            image = pygame.image.load("sprites/Ship1.png")
            print(image.get_size())

            ship_specs = [
                {"speed": 250, "sprite": "sprites/Ship1.png"},
                {"speed": 200, "sprite": "sprites/Ship2.png"},
                {"speed": 150, "sprite": "sprites/Ship3.png"},
                {"speed": 100, "sprite": "sprites/Ship4.png"},
                {"speed": 50, "sprite": "sprites/Ship5.png"}
            ]

            print(random_post_list)

            if number_to_display <= 2:
                spec = random.choice(ship_specs)
                new_rand_pos_x = random.uniform(0,
                                                screen.get_width() - ship_width)  # Assuming ship_width is defined
                new_enemy_pos = pygame.Vector2(new_rand_pos_x, -150)
                new_enemy_ship = EnemyShipOne(spec["speed"], "blue", screen, new_enemy_pos, dt, spec["sprite"])
                new_enemy_ship.UpdatePosition(dt)
                all_ships.add(new_enemy_ship)
                enemy_ships.append(new_enemy_ship)

            if number_to_display >= 3 and number_to_display < 6:
                for _ in range(2):  # Spawn 4 ships
                    spec = random.choice(ship_specs)
                    new_rand_pos_x = random.uniform(0,
                                                    screen.get_width() - ship_width)  # Assuming ship_width is defined
                    new_enemy_pos = pygame.Vector2(new_rand_pos_x, -150)
                    new_enemy_ship = EnemyShipOne(spec["speed"], "blue", screen, new_enemy_pos, dt, spec["sprite"])
                    new_enemy_ship.UpdatePosition(dt)
                    all_ships.add(new_enemy_ship)
                    enemy_ships.append(new_enemy_ship)

            if number_to_display >= 6 and number_to_display < 10:
                for _ in range(4):  # Spawn 4 ships
                    spec = random.choice(ship_specs)
                    new_rand_pos_x = random.uniform(0,
                                                    screen.get_width() - ship_width)  # Assuming ship_width is defined
                    new_enemy_pos = pygame.Vector2(new_rand_pos_x, -150)
                    new_enemy_ship = EnemyShipOne(spec["speed"], "blue", screen, new_enemy_pos, dt, spec["sprite"])
                    new_enemy_ship.UpdatePosition(dt)
                    all_ships.add(new_enemy_ship)
                    enemy_ships.append(new_enemy_ship)

            if number_to_display >= 10 and number_to_display < 20:
                for _ in range(8):  # Spawn 4 ships
                    spec = random.choice(ship_specs)
                    new_rand_pos_x = random.uniform(0,
                                                    screen.get_width() - ship_width)  # Assuming ship_width is defined
                    new_enemy_pos = pygame.Vector2(new_rand_pos_x, -150)
                    new_enemy_ship = EnemyShipOne(spec["speed"], "blue", screen, new_enemy_pos, dt, spec["sprite"])
                    new_enemy_ship.UpdatePosition(dt)
                    all_ships.add(new_enemy_ship)
                    enemy_ships.append(new_enemy_ship)

            if number_to_display >= 20:
                for _ in range(16):  # Spawn 4 ships
                    spec = random.choice(ship_specs)
                    new_rand_pos_x = random.uniform(0,
                                                    screen.get_width() - ship_width)  # Assuming ship_width is defined
                    new_enemy_pos = pygame.Vector2(new_rand_pos_x, -150)
                    new_enemy_ship = EnemyShipOne(spec["speed"], "blue", screen, new_enemy_pos, dt, spec["sprite"])
                    new_enemy_ship.UpdatePosition(dt)
                    all_ships.add(new_enemy_ship)
                    enemy_ships.append(new_enemy_ship)

            if number_to_display >= 50:
                for _ in range(25):  # Spawn 4 ships
                    spec = random.choice(ship_specs)
                    new_rand_pos_x = random.uniform(0,
                                                    screen.get_width() - ship_width)  # Assuming ship_width is defined
                    new_enemy_pos = pygame.Vector2(new_rand_pos_x, -150)
                    new_enemy_ship = EnemyShipOne(spec["speed"], "blue", screen, new_enemy_pos, dt, spec["sprite"])
                    new_enemy_ship.UpdatePosition(dt)
                    all_ships.add(new_enemy_ship)
                    enemy_ships.append(new_enemy_ship)
        text_color = (255, 255, 255)

        text_surface = game_font.render("Score: " +  str(number_to_display), True, text_color)

        text_position = (50, 50)  # Example position (x, y)
        screen.blit(text_surface, text_position)

        player_ship.SetPlayerPosition(dt)
        player_ship.drawBullets()

        # Updates enemy ship for movement
        for ship in enemy_ships:
            ship.UpdatePosition(dt)

        for bullet in player_ship.bullets[:]:  # Iterate over a copy to safely modify the original list
            for ship in enemy_ships[:]:  # Similarly, iterate over a copy if you plan to modify it
                if ship.hitbox.colliderect(bullet.rect):
                    print("hit")
                    number_to_display += 1
                    bullets_to_remove.add(bullet)  # Mark the bullet for removal
                    all_ships.remove(ship)  # Remove the sprite from the drawing group
                    enemy_ships.remove(ship)  # Also remove the ship from the logical list
        # Remove bullets that have been marked for removal
        for bullet in bullets_to_remove:
            if bullet in player_ship.bullets:
                player_ship.bullets.remove(bullet)

        # for ship in enemy_ships:
        #     if player_ship.rect.colliderect(ship.hitbox):
        #         print("Player hit by enemy ship!")
        #         running = False
        #         break  # Exit the loop since the game is over

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

