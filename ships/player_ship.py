from ships.ship import Ship
from ammo.bullet import Bullet
import pygame
class PlayerShip(Ship):
    bullets = []
    def __init__(self, speed, colour, size, screen, ship_pos, dt, ship_image="sprites/player_idle.png"):
        super().__init__(speed, colour, size, screen, ship_pos, ship_image=ship_image)
        self.keys = pygame.key.get_pressed()
        self.dt = dt
        self.angle = 45
        self.ship_image = pygame.image.load(ship_image)  # Load the image here
        self.ship_path = ship_image
        self.rotated_image = self.ship_image  # Initial image is not rotated

        self.rotate(self.angle)
        self.update_rotation()

        self.rect = self.ship_image.get_rect(topleft = (self.ship_pos.x, self.ship_pos.y))

    def GetPlayerPosition(self):
        return self.ship_pos

    def setBullets(self, bullet):
        self.bullets.append(bullet)

    def SetPlayerPosition(self):
        if self.keys[pygame.K_w]:
            self.ship_pos.y -= 500 * self.dt
        if self.keys[pygame.K_s]:
            self.ship_pos.y += 500 * self.dt
        if self.keys[pygame.K_a]:
            self.ship_pos.x -= 500 * self.dt
        if self.keys[pygame.K_d]:
            self.ship_pos.x += 500 * self.dt

    def Fire(self):
        bullet_pos = self.ship_pos.copy()
        bullet_pos.x = bullet_pos.x + 40
        new_bullet = Bullet(5, 20, self.screen, bullet_pos)
        self.setBullets(new_bullet)

    def drawBullets(self):
        for bullet in self.bullets:
            bullet.setBulletPos()
            bullet.drawBullet()

    def printBullets(self):
        for bullet in self.bullets:
            print(bullet.bullet_pos.x)