from ships.ship import Ship
import pygame
class EnemyShipOne(Ship):
    bullets = []
    def __init__(self, speed, colour, size, screen, ship_pos, dt, ship_image="sprites/Ship2.png"):
        super().__init__(speed, colour, size, screen, ship_pos, ship_image=ship_image)
        self.speed = 20
        self.keys = pygame.key.get_pressed()
        self.dt = dt
        self.image = pygame.image.load(ship_image)  # Load the image here
        self.ship_path = ship_image
        self.rotated_image = self.image  # Initial image is not rotated

        self.rot_center(90)

    def GetPlayerPosition(self):
        return self.ship_pos

    def UpdatePosition(self, dt):
        self.rect.y += int(100 * dt)
        self.ship_pos = pygame.Vector2(self.rect.topleft)

    def rot_center(self, angle):
        """Rotate the ship image around its center and adjust its rectangle."""
        original_center = self.rect.center
        self.rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = self.rotated_image.get_rect(center=original_center)