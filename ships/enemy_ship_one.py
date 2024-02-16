from ships.ship import Ship
import pygame
class EnemyShipOne(Ship):
    bullets = []
    def __init__(self, speed, colour, size, screen, ship_pos, dt, ship_image="sprites/Ship2.png"):
        super().__init__(speed, colour, size, screen, ship_pos, ship_image=ship_image)
        self.speed = 20
        self.keys = pygame.key.get_pressed()
        self.dt = dt
        self.angle = 0
        self.image = pygame.image.load(ship_image)  # Load the image here
        self.ship_path = ship_image
        self.rotated_image = self.image  # Initial image is not rotated

        self.rotate(90)
        self.update_rotation()

        # self.rect = self.image.get_rect(topleft=(self.ship_pos.x, self.ship_pos.y))

    def GetPlayerPosition(self):
        return self.ship_pos

    def UpdatePosition(self, dt):
        self.rect.y += int(100 * dt)
        self.ship_pos = pygame.Vector2(self.rect.topleft)
