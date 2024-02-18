import pygame
from ships.ship import Ship
from ships.player_ship import PlayerShip
from ships.enemy_ship_one import EnemyShipOne
from ammo.bullet import Bullet
import asyncio
import random
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))

pygame.font.init()
font_size = 24
title_font = pygame.font.Font(None, 36)
game_font = pygame.font.Font(None, font_size)



clock = pygame.time.Clock()
running = True
dt = 0

def draw_start_button(text, pos):
    button_color = (0, 0, 0)
    button_rect = pygame.Rect(1280 // 2 - 50, pos // 2 - 25, 100, 50)

    pygame.draw.rect(screen, button_color, button_rect)
    text_surf = title_font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=button_rect.center)

    screen.blit(text_surf, text_rect)
    return button_rect


def display_leaderboard():
    running = True
    while running:
        screen.fill((0, 0, 0))
        # Display leaderboard contents here
        # Example: Display "Tom: 100"
        text_surf = title_font.render("Tom: 100", True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(640, 360))
        screen.blit(text_surf, text_rect)

        # Draw a "Back" button
        back_button_rect = draw_start_button("Back", 900)  # Adjust position as needed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    running = False  # Exit this loop to return to the main menu

        pygame.display.flip()

def draw_input_box(text, box_rect, cursor_visible):
    # Draw the prompt text
    prompt_text = "Enter name:"
    prompt_surf = title_font.render(prompt_text, True, (255, 255, 255))
    prompt_rect = prompt_surf.get_rect(right=box_rect.left - 10, centery=box_rect.centery)
    screen.blit(prompt_surf, prompt_rect)

    # Input box and text
    background_color = (255, 255, 255)
    pygame.draw.rect(screen, background_color, box_rect)  # Fill the rectangle with white
    pygame.draw.rect(screen, (0, 0, 0), box_rect, 2)  # Draw the border
    text_surf = title_font.render(text, True, (0, 0, 0))
    screen.blit(text_surf, (box_rect.x + 5, box_rect.y + 5))

    # Cursor
    if cursor_visible:
        cursor_x = box_rect.x + 5 + text_surf.get_width() + 2
        cursor_y = box_rect.y + 5
        cursor_height = text_surf.get_height()
        pygame.draw.rect(screen, (0, 0, 0), (cursor_x, cursor_y, 2, cursor_height))
async def start_menu():
    running = True
    player_name = ""
    input_box = pygame.Rect(1280 // 2 - 100, 200, 200, 50)
    active = False
    cursor_visible = False
    cursor_blink_time = 0

    while running:
        screen.fill((0, 0, 0))
        start_button_rect = draw_start_button("Play", 600)
        leader_board_button = draw_start_button("Leaderboard", 720)

        if pygame.time.get_ticks() - cursor_blink_time > 500:  # Toggle cursor every 500ms
            cursor_blink_time = pygame.time.get_ticks()
            cursor_visible = not cursor_visible

        draw_input_box(player_name, input_box, cursor_visible)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                elif start_button_rect.collidepoint(event.pos) and player_name:
                    return player_name  # Proceed to game with player name
                elif leader_board_button.collidepoint(event.pos):
                    display_leaderboard()
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        pygame.display.flip()
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
                {"speed": 100, "sprite": "sprites/Ship4.png"}
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

        for ship in enemy_ships:
            if player_ship.hitbox.colliderect(ship.hitbox):
                print("Player hit by enemy ship!")
                running = False
                break  # Exit the loop since the game is over

        all_ships.update()  # Update all sprites in the group
        all_ships.draw(screen)



        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

        await asyncio.sleep(0)


# Simplify your main loop initiation
if __name__ == "__main__":
    player_name = asyncio.run(start_menu())
    if len(player_name) > 0:
        asyncio.run(main())


