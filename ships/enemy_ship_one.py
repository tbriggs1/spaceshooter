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

        self.update_hitbox()

    def GetPlayerPosition(self):
        return self.ship_pos

    def UpdatePosition(self, dt):
        self.rect.y += int(100 * dt)
        self.ship_pos = pygame.Vector2(self.rect.topleft)
        self.update_hitbox()

    def update_hitbox(self):
        padding_horizontal = 50  # Use the existing horizontal padding
        padding_vertical = 20  # Adjust this value to increase the hitbox height

        # Adjust the hitbox size. Increase height by reducing vertical padding, if needed.
        self.hitbox = self.rect.inflate(-padding_horizontal * 2, -padding_vertical * 2)

        # Ensure the hitbox is properly positioned
        # If you need to adjust the position further due to changes in dimensions, do it here
        self.hitbox.center = self.rect.center