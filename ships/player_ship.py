from ships.ship import Ship
import pygame
class PlayerShip(Ship):
    bullets = []
    def __init__(self, speed, colour, size, screen, ship_pos, keys, dt):
        super().__init__(speed, colour, size, screen, ship_pos)
        self.keys = keys
        self.dt = dt

    def GetPlayerPosition(self):
        return self.ship_pos

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


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullets.append(super().Bullet())