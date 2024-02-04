import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, speed, colour, size, screen, ship_pos, ship_image="sprites/enemy_one.png"):
        super().__init__()
        self.speed = speed
        self.colour = colour
        self.size = size
        self.screen = screen
        self.ship_pos = ship_pos
        self.angle = 0
        self.ship_image = pygame.image.load(ship_image)  # Load the image here
        self.ship_path = ship_image
        self.rotated_image = self.ship_image  # Initial image is not rotated

    def rotate(self, angle):
        # Rotate the ship image and update the angle
        self.angle += angle
        self.rotated_image = pygame.transform.rotate(self.ship_image, self.angle)

    def update_rotation(self):
        # Blit the rotated image onto the screen
        self.screen.blit(self.rotated_image, self.ship_pos)

    def update(self):
        self.screen.blit(pygame.image.load(self.ship_path), self.ship_pos)