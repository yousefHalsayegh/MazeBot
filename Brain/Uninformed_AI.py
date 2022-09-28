import pygame as pg

class BFS:

    def __init__(self) -> None:
        self.queue = []
        self.visited = []
        
    def start(self, maze, app):
        
        
        self.visited.append(maze.get_cell(0,0))
        self.queue.append(maze.get_cell(0,0))
        
        while self.queue:
            m = self.queue.pop(0)
            
            print(f'x:{m.x}, y:{m.y} , {m.walls}')
            w = m.walls
            
            if w['N'] == True and m.y != 0:
                
                if(maze.get_cell(m.x, m.y - 1) not in self.visited):
                
                    self.queue.append(maze.get_cell(m.x, m.y - 1))
                    self.visited.append(maze.get_cell(m.x, m.y - 1))
                    app.draw_path(m.x, m.y)
                
            if w['E'] == True and m.x != len(maze.maze) - 1:
                
                if(maze.get_cell(m.x + 1, m.y) not in self.visited):
                    
                    self.queue.append(maze.get_cell(m.x + 1, m.y))
                    self.visited.append(maze.get_cell(m.x + 1, m.y))
                    app.draw_path(m.x, m.y)
                
            if w['S'] == True and m.y != len(maze.maze[0]) - 1:
                
                if(maze.get_cell(m.x, m.y + 1) not in self.visited):
                    
                    self.queue.append(maze.get_cell(m.x, m.y + 1))
                    self.visited.append(maze.get_cell(m.x, m.y + 1))
                    app.draw_path(m.x, m.y)
                
            if w['W'] == True and m.x != 0:
                
                if(maze.get_cell(m.x - 1, m.y) not in self.visited):
                    self.queue.append(maze.get_cell(m.x - 1, m.y ))
                    self.visited.append(maze.get_cell(m.x - 1, m.y))
                    app.draw_path(m.x, m.y)
        

class DFS:

    def __init__(self) -> None:
        pass

class DLS:
    def __init__(self) -> None:
        pass

class IDS:
    def __init__(self) -> None:
        pass