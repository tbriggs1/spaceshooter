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
        self.image = pygame.image.load(ship_image)  # Load the image here
        self.ship_path = ship_image
        # self.rotated_image = self.image  # Initial image is not rotated

        # Initialize self.rect before calling self.rotate
        self.rect = self.image.get_rect(topleft=self.ship_pos)

        # Now it's safe to call self.rotate
        self.rotate(90)

    def rotate(self, angle):
        self.angle += angle
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rotated_image.get_rect(center=self.rect.center)  # Re-center the rect.

    def update_rotation(self):
        # Blit the rotated image onto the screen
        self.screen.blit(self.rotated_image, self.ship_pos)

    def draw(self):
        self.rect.topleft = self.ship_pos  # Ensure the rect position is updated.
        self.screen.blit(self.rotated_image, self.rect)