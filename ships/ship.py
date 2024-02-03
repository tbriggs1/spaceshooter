import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self, speed, colour, size, screen, ship_pos, ship_image="sprites/enemy_one.png"):
        super().__init__()
        self.speed = speed
        self.colour = colour
        self.size = size
        self.screen = screen
        self.ship_pos = ship_pos
        self.ship_image = ship_image



    # def update(self):
    #     self.position = (self.ship_pos)

    def draw(self, surface):
        surface.blit(pygame.image.load(self.ship_image), self.ship_pos)

    # def setShipImage(self):
    #     self.ship_image = "sprites/player_idle.png"