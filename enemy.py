import pygame
import random

class Enemy:
    def __init__(self):
        self.image = pygame.image.load('assets/images/enemy.png')
        self.rect = self.image.get_rect(center=(random.randint(0, 800), random.randint(0, 600)))

    def update(self):
        # Simple AI movement (for example, move down)
        self.rect.y += 1
        if self.rect.y > 600:  # Reset position if it goes off screen
            self.rect.y = 0
            self.rect.x = random.randint(0, 800)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
