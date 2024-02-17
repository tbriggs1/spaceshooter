from ships.ship import Ship
from ammo.bullet import Bullet
import pygame
class PlayerShip(Ship):
    bullets = []
    def __init__(self, speed, colour, screen, ship_pos, dt, ship_image):
        super().__init__(speed, colour, screen, ship_pos, ship_image)
        self.dt = dt
        self.angle = 45
        self.original_image = pygame.image.load(ship_image)  # Load the original image
        self.ship_path = ship_image
        self.player_speed = 300
        self.player_count = 0

        # Set the initial image to the original image
        self.image = self.original_image
        # Now, properly call rot_center to rotate the initial image
        self.rot_center(90)

        # The rectangle is set based on the rotated image
        self.rect = self.image.get_rect(center=ship_pos)

    def GetPlayerPosition(self):
        return self.ship_pos

    def SetPlayerPosition(self, dt):
        self.rect.topleft = self.ship_pos
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.ship_pos.y -= self.player_speed * dt
        if keys[pygame.K_s]:
            self.ship_pos.y += self.player_speed * dt
        if keys[pygame.K_a]:
            self.ship_pos.x -= self.player_speed * dt
        if keys[pygame.K_d]:
            self.ship_pos.x += self.player_speed * dt

    def Fire(self):
        bullet_pos = self.ship_pos.copy()
        # Sets bullet starting position at ship mouth
        bullet_pos.x = bullet_pos.x + 40

        # Creates a new bullet and appends it to a list
        new_bullet = Bullet(5, 20, self.screen, bullet_pos)
        self.bullets.append(new_bullet)

    def drawBullets(self):
        for bullet in self.bullets:
            bullet.setBulletPos()
            bullet.drawBullet()

