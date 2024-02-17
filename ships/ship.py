import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, speed, colour, screen, ship_pos, ship_image):
        super().__init__()
        self.speed = speed
        self.colour = colour
        self.screen = screen
        self.ship_pos = ship_pos
        self.angle = 45
        self.image = pygame.image.load(ship_image)  # Load the image here
        self.ship_path = ship_image
        # self.rotated_image = self.image  # Initial image is not rotated

        # Initialize self.rect before calling self.rotate
        self.rect = self.image.get_rect(topleft=self.ship_pos)

        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.screen.blit(self.rotated_image, self.ship_pos)

    def rot_center(self, angle):
        """Rotate the ship image around its center and adjust its rectangle."""
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)