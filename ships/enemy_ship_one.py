from ships.ship import Ship
import pygame
class EnemyShipOne(Ship):
    bullets = []
    def __init__(self, speed, colour, screen, ship_pos, dt, ship_image="sprites/Ship2.png"):
        super().__init__(speed, colour, screen, ship_pos, ship_image)
        self.speed = 20
        self.keys = pygame.key.get_pressed()
        self.dt = dt
        self.original_image = pygame.image.load(ship_image)  # Load the image here
        self.ship_path = ship_image
        self.rotated_image = self.image  # Initial image is not rotated

        # Set the initial image to the original image
        self.image = self.original_image
        # Now, properly call rot_center to rotate the initial image
        self.rot_center(90)

        # The rectangle is set based on the rotated image
        self.rect = self.image.get_rect(center=ship_pos)
    def GetPlayerPosition(self):
        return self.ship_pos

    def UpdatePosition(self, dt):
        self.rect.y += int(100 * dt)
        self.ship_pos = pygame.Vector2(self.rect.topleft)
