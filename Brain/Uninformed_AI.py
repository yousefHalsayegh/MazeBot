from http.client import FOUND
from operator import truediv
from pickle import FALSE
import pygame as pg

class BFS:

    def __init__(self) -> None:
        self.queue = []
        self.visited = []
        
    def start(self, maze):
        
        
        self.visited.append(maze.get_cell(0,0))
        self.queue.append(maze.get_cell(0,0))
        path = []
        
        while self.queue:
            m = self.queue.pop(0)
            
            path.append((m.x,m.y))
            print(f'x:{m.x}, y:{m.y} , {m.walls}')
            if m.x == len(maze.maze) - 1 and m.y == len(maze.maze[0]) - 1:
                return path
            w = m.walls
            
            if w['N'] == False and m.y != 0:
                
                if(maze.get_cell(m.x, m.y - 1) not in self.visited):
                
                    self.queue.append(maze.get_cell(m.x, m.y - 1))
                    self.visited.append(maze.get_cell(m.x, m.y - 1))
                
            if w['E'] == False and m.x != len(maze.maze) - 1:
                
                if(maze.get_cell(m.x + 1, m.y) not in self.visited):
                    
                    self.queue.append(maze.get_cell(m.x + 1, m.y))
                    self.visited.append(maze.get_cell(m.x + 1, m.y))
                
            if w['S'] == False and m.y != len(maze.maze[0]) - 1:
                
                if(maze.get_cell(m.x, m.y + 1) not in self.visited):
                    
                    self.queue.append(maze.get_cell(m.x, m.y + 1))
                    self.visited.append(maze.get_cell(m.x, m.y + 1))
                
            if w['W'] == False and m.x != 0:
                
                if(maze.get_cell(m.x - 1, m.y) not in self.visited):
                    self.queue.append(maze.get_cell(m.x - 1, m.y ))
                    self.visited.append(maze.get_cell(m.x - 1, m.y))    
                    
        return path
        

class DFS:

    def __init__(self):
        self.stack = []
        self.visited = []
        
    def start(self, maze):
        
        
        self.visited.append(maze.get_cell(0,0))
        self.stack.append(maze.get_cell(0,0))
        path = []
        
        while self.stack:
            m = self.stack.pop(-1)
            
            path.append((m.x,m.y))
            print(f'x:{m.x}, y:{m.y} , {m.walls}')
            if m.x == len(maze.maze) - 1 and m.y == len(maze.maze[0]) - 1:
                return path
            w = m.walls
            
            if w['N'] == False and m.y != 0:
                
                if(maze.get_cell(m.x, m.y - 1) not in self.visited):
                
                    self.stack.append(maze.get_cell(m.x, m.y - 1))
                    self.visited.append(maze.get_cell(m.x, m.y - 1))
                
            if w['E'] == False and m.x != len(maze.maze) - 1:
                
                if(maze.get_cell(m.x + 1, m.y) not in self.visited):
                    
                    self.stack.append(maze.get_cell(m.x + 1, m.y))
                    self.visited.append(maze.get_cell(m.x + 1, m.y))
                
            if w['S'] == False and m.y != len(maze.maze[0]) - 1:
                
                if(maze.get_cell(m.x, m.y + 1) not in self.visited):
                    
                    self.stack.append(maze.get_cell(m.x, m.y + 1))
                    self.visited.append(maze.get_cell(m.x, m.y + 1))
                
            if w['W'] == False and m.x != 0:
                
                if(maze.get_cell(m.x - 1, m.y) not in self.visited):
                    self.stack.append(maze.get_cell(m.x - 1, m.y ))
                    self.visited.append(maze.get_cell(m.x - 1, m.y))    
                    
        return path

class DLS:
    def __init__(self) -> None:
        pass

class IDS:
    
    def __init__(self):
        
        self.maxDepth = 20
        
        
    def start(self, maze):
        
        for i in range(self.maxDepth):
            
            if self.DLS(maze, i) :
                return True
            
        return False
            
    def DLS(self, maze, depth):
        
        stack = []
        visited = []
        
        visited.append(maze.get_cell(0,0))
        stack.append(maze.get_cell(0,0))
        
        for i in range(depth):
            m = stack.pop(-1)
            
            if m.x == len(maze.maze) - 1 and m.y == len(maze.maze[0]) - 1:
                return True
            w = m.walls
            
            if w['N'] == False and m.y != 0:
                
                if(maze.get_cell(m.x, m.y - 1) not in visited):
                
                    stack.append(maze.get_cell(m.x, m.y - 1))
                    visited.append(maze.get_cell(m.x, m.y - 1))
                
            if w['E'] == False and m.x != len(maze.maze) - 1:
                
                if(maze.get_cell(m.x + 1, m.y) not in visited):
                    
                    stack.append(maze.get_cell(m.x + 1, m.y))
                    visited.append(maze.get_cell(m.x + 1, m.y))
                
            if w['S'] == False and m.y != len(maze.maze[0]) - 1:
                
                if(maze.get_cell(m.x, m.y + 1) not in visited):
                    
                    stack.append(maze.get_cell(m.x, m.y + 1))
                    visited.append(maze.get_cell(m.x, m.y + 1))
                
            if w['W'] == False and m.x != 0:
                
                if(maze.get_cell(m.x - 1, m.y) not in visited):
                    stack.append(maze.get_cell(m.x - 1, m.y ))
                    visited.append(maze.get_cell(m.x - 1, m.y))    
                    
        return False
        

class UCS:
    
    def __init__(self):
        pass 