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
        self.ship_image = ship_image

        self.screen.blit(pygame.image.load(self.ship_image), self.ship_pos)

    # def draw(self, surface):
    #     surface.blit(pygame.image.load(self.ship_image), self.ship_pos)

    def rot_center(self, image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect