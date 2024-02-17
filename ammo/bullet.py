import pygame

class Bullet():
    def __init__(self, size, speed, screen, bullet_pos):
        self.size = size
        self.speed = speed
        self.screen = screen
        self.bullet_pos = pygame.Vector2(bullet_pos)  # Ensure this is a Vector2 for consistency
        # Adjust the initial position as needed
        self.bullet_pos.x += 24
        self.bullet_pos.y += 20
        # Create a rect for collision detection; use a dummy size for now
        self.rect = pygame.Rect(self.bullet_pos.x, self.bullet_pos.y, 10, 10)  # Adjust size as needed

    def drawBullet(self):
        pygame.draw.circle(self.screen, "white", (int(self.bullet_pos.x), int(self.bullet_pos.y)), self.size)

    def setBulletPos(self):
        # Update bullet position
        self.bullet_pos.x += 0  # This line seems redundant, as the x position doesn't change
        self.bullet_pos.y += -self.speed
        # Update rect to follow the bullet position
        self.rect.center = (int(self.bullet_pos.x), int(self.bullet_pos.y))

    def update(self):
        # This method could be used to update the bullet's position and rect each frame
        self.setBulletPos()
