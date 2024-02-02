import pygame

class Ship:
    def __init__(self, speed, colour, size, screen, ship_pos):
        self.speed = speed
        self.colour = colour
        self.size = size
        self.screen = screen
        self.ship_pos = ship_pos

        pygame.draw.circle(self.screen, self.colour, self.ship_pos, self.size)

    def Bullet(self):
        return pygame.draw.circle(self.screen, "white", self.ship_pos, 5)


