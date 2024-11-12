import pygame
from player import Player
from enemy import Enemy
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemies = [Enemy() for _ in range(5)]
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.lives = 3

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(BACKGROUND_COLOR)
            self.player.update()
            self.player.draw(self.screen)

            for enemy in self.enemies:
                enemy.update()
                enemy.draw(self.screen)
                if self.player.rect.colliderect(enemy.rect):
                    self.lives -= 1
                    self.score -= 10
                    enemy.reset_position()  # Reset enemy position on collision
                    if self.lives <= 0:
                        running = False  # End game if no lives left

            self.display_score()
            self.display_lives()
            pygame.display.flip()
            self.clock.tick(60)

    def display_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def display_lives(self):
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 50))
