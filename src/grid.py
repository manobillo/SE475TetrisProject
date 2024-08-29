# src/grid.py
# the grid is a core part of the 1010! app game that handles the board logic

import pygame 

class Grid:
    def __init__(self, rows=10, cols=10):
    #grid is initalized as 10 x 10 matrix filled with zeros (empty cells)
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def add_shape(self, shape, position):
        """Add a shape to the grid at the given position."""
        x, y = position
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    self.grid[x+i][y+j] = 1 #Mark cell as filled

    def check_and_clear_lines(self):
        """Check and clear full lines and columns, returning the number of cleared lines."""

        lines_cleared = 0

        #Check and clear full rows
        for i in range(self.rows):
            if all(self.grid[i]):
                lines_cleared += 1
                for i in range(self.rows):
                    self.grid[i][j] = 0


        #can be used to update the score
        return lines_cleared
    

    def is_valid_position(self, shape, position):
        """Check if the shape can be placed at the given position."""
        x, y = position
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    if x + i >= self.rows or y + j >= self.cols or self.grid[x+i][y+j]:
                        return False
            return True
        
    def draw(self, surface):
        """Draw the grid and shapes onto the screen."""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j]:
                    pygame.draw.rect(surface, (200, 200, 200), (j * 30, i * 30, 30, 30))
                pygame.draw.rect(surface, (100, 100, 100), (j * 30, i * 30, 30, 30), 1)