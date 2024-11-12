import pygame
from game import Game
from menu import Menu

def main():
    pygame.init()
    menu = Menu()
    game = Game()
    
    while True:
        if menu.run():
            game.run()
        else:
            break

    pygame.quit()

if __name__ == "__main__":
    main()
