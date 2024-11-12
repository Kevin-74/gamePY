import pygame

class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 74)
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            title_text = self.font.render("My Game", True, (255, 255, 255))
            start_text = self.font.render("Press Enter to Start", True, (255, 255, 255))
            self.screen.blit(title_text, (250, 200))
            self.screen.blit(start_text, (150, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True  # Start the game

            pygame.display.flip()
        return False  # Exit the game
