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
        self.ship_image = pygame.image.load(ship_image)  # Load the image here
        self.ship_path = ship_image
        self.rotated_image = self.ship_image  # Initial image is not rotated

        self.rotate(90)
        self.update_rotation()
        self.UpdatePosition()

        self.rect = self.ship_image.get_rect(topleft=(self.ship_pos.x, self.ship_pos.y))

    def GetPlayerPosition(self):
        return self.ship_pos

    def UpdatePosition(self):
        self.ship_pos.y += 100 * self.dt