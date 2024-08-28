#src/main.py

import pygame
from grid import Grid

def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    #Create an instance of Grid
    grid = Grid()

    running = True
    while running:
       screen.fill((0, 0, 0))
       grid.draw(screen)
       pygame.display.flip()

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
