from ships.ship import Ship
from ammo.bullet import Bullet
import pygame
class PlayerShip(Ship):
    bullets = []
    def __init__(self, speed, colour, size, screen, ship_pos, keys, dt):
        super().__init__(speed, colour, size, screen, ship_pos, ship_image="sprites/player_idle.png")
        self.keys = keys
        self.dt = dt


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

    def SetPlayerRotation(self, angle):
        rotated_surface = pygame.transform.rotate(self.screen, angle)
        return rotated_surface

    def Fire(self):
        bullet_pos = self.ship_pos.copy()
        bullet_pos.x = bullet_pos.x + 30
        new_bullet = Bullet(5, 10, self.screen, bullet_pos)
        self.setBullets(new_bullet)

    def drawBullets(self):
        for bullet in self.bullets:
            bullet.setBulletPos()
            bullet.drawBullet()