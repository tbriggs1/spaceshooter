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
        self.rotated_image = self.ship_image  # Initial image is not rotated

    def rotate(self, angle):
        # Rotate the ship image and update the angle
        self.angle += angle
        self.rotated_image = pygame.transform.rotate(self.ship_image, self.angle)

    def update(self):
        # Blit the rotated image onto the screen
        self.screen.blit(self.rotated_image, self.ship_pos)