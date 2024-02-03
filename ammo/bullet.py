import pygame

class Bullet():
    def __init__(self, size, speed, screen, bullet_pos):
        self.size = size
        self.speed = speed
        self.screen = screen
        self.bullet_pos = bullet_pos

    def drawBullet(self):
        pygame.draw.circle(self.screen, "white", self.bullet_pos, 5)

    def getBulletPos(self):
        return self.bullet_pos

    def setBulletPos(self):
        print(self.bullet_pos)
        self.bullet_pos.x = self.bullet_pos.x + 3
        self.bullet_pos.y = self.bullet_pos.y + 1