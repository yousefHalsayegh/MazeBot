import numpy as np
import random 


class Cell:
    """A cell in the maze.

    A maze "Cell" is a point in the grid which may be surrounded by walls to
    the north, east, south or west.

    """

    # A wall separates a pair of cells in the N-S or W-E directions.
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""

        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def has_all_walls(self):
        """Does this cell still have all its walls?"""

        return all(self.walls.values())

    def knock_down_wall(self, other, wall):
        """Knock down the wall between cells self and other."""

        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False

class Maze:

    def __init__(self, width, height, ix, iy):

        self.width, self.height = width, height

        self.ix, self.iy = ix, iy

        self.maze = [[Cell(x, y) for y in range(height)] for x in range(width)]

    def get_cell(self, x, y):

        return self.maze[x][y]

    def unvisited_neighbours(self, cell):

        neighbours = []

        move = [('W', (-1, 0)),
                ('E', (1, 0)),
                ('S', (0, 1)), 
                ('N', (0, -1))]

        for direction, (mx, my) in move:

            x, y = cell.x + mx, cell.y + my 

            if ( 0 <= x < self.width) and (0 <= y < self.height):

                neighbour = self.get_cell(x, y)

                if neighbour.has_all_walls():

                    neighbours.append((direction, neighbour))

        return neighbours

    def generate(self):

        n = self.width * self.height
        stack = []
        current_cell = self.get_cell(self.ix, self.iy)

        #number of visited cells
        nv = 1

        while nv < n:

            neighbours = self.unvisited_neighbours(current_cell)

            if not neighbours :

                current_cell = stack.pop()
                
                continue
            
            direction, next = random.choice(neighbours)
            current_cell.knock_down_wall(next, direction)
            stack.append(current_cell)
            current_cell = next 
            nv += 1
    
    def __str__(self):
        """Return a (crude) string representation of the maze."""

        maze_rows = ['-' * self.width * 2]
        for y in range(self.height):
            maze_row = ['|']
            for x in range(self.width):
                if self.maze[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.width):
                if self.maze[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

        