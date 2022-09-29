
import pygame as pg
from Maze import Maze
from Brain import Uninformed_AI
import time


class App:

    BLACK = (0 ,0 ,0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    (WIDTH, HEIGHT) = (600, 600)

    nx = 5
    ny = 5
      
    dx = 0
    dy = 0
    
    midx = 0
    midy = 0

    window = None 

    scene = None
    
    generated = False
    rerun = False

    def __init__(self):

        pg.init()

        self.window = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        pg.display.set_caption('Maze')
        self.window.fill(self.WHITE)
        self.font = pg.font.SysFont("Ariel", 20)

        self.exit = False
        
        self.start_menu()
        
        self.reset = pg.Surface((self.WIDTH, self.HEIGHT - 90))
        self.reset.fill(self.WHITE)
        
        self.maze =  Maze(self.nx, self.ny, 0, 0)

    def start_menu(self):

        self.scene = 'Start Menu'

        text = self.font.render("Please enter the maze size", True, self.BLACK)
        textRec = text.get_rect()
        textRec.center = (105, 20)

        self.window.blit(text, textRec)

        #Creating the generate button 
        self.generate = self.create_button('Generate Maze', 45, 60, 100, 25)

        #Creating buttons and fields for inputing coordinates 
        self.x_button = self.create_input_button('X:', 20, 30, 75, 25)
        self.y_button = self.create_input_button('Y:', 115, 30, 75, 25)
        
        #Uninformed AI buttons 
        self.BFS = self.create_button("BFS", 220, 30, 50, 25)
        
        self.DFS = self.create_button("DFS", 280, 30, 50, 25)

        #Seperation line
        pg.draw.line(self.window, self.BLACK, (0, 89), (self.WIDTH, 89))

    def create_button(self, string, x, y, w, h):

        button = pg.Rect(x, y, w, h)
        pg.draw.rect(self.window, self.BLACK, button, 1)
        text = self.font.render(string, True, self.BLACK)
        textRec = text.get_rect()
        textRec.center = (x + w // 2, y + h // 2)

        self.window.blit(text, textRec)
        return button

    def create_input_button(self, string, x, y, w, h):

        button = pg.Rect(x, y, w, h)

        pg.draw.rect(self.window, self.BLACK, button, 1)

        text = self.font.render("input....", True, self.GREY)
        textRec = text.get_rect()
        textRec.center = (x + w // 2, y + h // 2)

        self.window.blit(text, textRec)

        text = self.font.render(string, True, self.BLACK)
        textRec = text.get_rect()
        textRec.center = (x - 10, y + h // 2)

        self.window.blit(text, textRec)
        
        return button

    def button_press(self, cord, game):
        

        if self.generate.collidepoint(cord):

            self.maze = Maze(self.nx, self.ny, 0, 0)
            self.maze.generate()

            self.draw_maze(self.maze)
            
            self.generated = True

        elif self.x_button.collidepoint(cord):

           self.input_text(self.x_button.x, self.x_button.y, self.x_button.w, self.x_button.h, self.x_button, 0)

        elif self.y_button.collidepoint(cord):

            self.input_text(self.y_button.x, self.y_button.y, self.y_button.w, self.y_button.h, self.y_button, 1)
            
        elif self.BFS.collidepoint(cord):
            
            
            if self.generated:
                
                self.run("BFS", game)
            
            else:
                
                print("Generate maze first")
                
        elif self.DFS.collidepoint(cord):
            
            
            if self.generated:
                
                self.run("DFS", game)
            
            else:
                
                print("Generate maze first")
        

    def input_text(self, x, y, w, h, button, n):

        eraser = pg.Surface((w - 2, h - 2))
        eraser.fill(self.WHITE)

        input = ''

        done = False
        while not done:

            for event in pg.event.get():
                
                if event.type == pg.KEYDOWN:


                    if event.key == pg.K_BACKSPACE:
                    
                        input = input[:-1]

                    elif len(input) > 2:
                        continue
                    
                    elif event.key == pg.K_RETURN:

                        if n == 0:

                            self.nx = int(input) 
                            if self.nx > 100:
                                self.nx = 100
                                input = '100'
                            print(self.nx)

                        else:

                            self.ny = int(input) 
                            if self.ny > 100:
                                self.ny = 100
                                input = '100'
                            print(self.ny)

                        done = True
                    
                    elif event.unicode.isdigit():

                        input += event.unicode

                elif event.type == pg.MOUSEBUTTONDOWN:

                    if n == 0:

                        self.nx = int(input) 
                        if self.nx > 100:
                            self.nx = 100
                            input = '100'
                        print(self.nx)

                    else:

                        self.ny = int(input) 
                        if self.ny > 100:
                            self.ny = 100
                            input = '100'
                        print(self.ny)

                    done = True

            pg.display.flip()

            text = self.font.render(input, True, self.BLACK, self.WHITE)
            textRec = text.get_rect()
            textRec.center = button.center
            self.window.blit(eraser, (x + 1 , y + 1))
            self.window.blit(text, textRec)

    def draw_maze(self, maze):
        
        self.rerun = False
        
        #Reset 
        self.window.blit(self.reset, (0,90))

        #Finiding out the distance between each point
        self.dx = self.WIDTH / self.nx
        self.dy = (self.HEIGHT - 90) / self.ny
        

        #midpoint for each poitn
        self.midx = self.dx / 2
        self.midy = self.dy / 2
        
        #center of each "block"
        center = [self.midx, 90 + self.midy]


        
        #Start block
        pg.draw.rect(self.window, self.BLUE, [0, 90, self.dx - 2, self.dy - 2])
        #End block
        pg.draw.rect(self.window, self.RED, [(self.WIDTH - self.dx) + 2, (self.HEIGHT - self.dy + 2), self.dx - 2, self.dy - 2])

        for y in range(maze.height):
            
            for x in range(maze.width):
                
                wall = maze.get_cell(x, y).walls
                
         
                if wall['N'] == True or y == 0:
                    
                    pg.draw.line(self.window, self.BLACK, (center[0] - self.midx, center[1] - self.midy), 
                                 (center[0] + self.midx, center[1] - self.midy), 2)
                
                if wall['S'] == True or y == self.ny:
                    
                    pg.draw.line(self.window, self.BLACK, (center[0] - self.midx, center[1] + self.midy), 
                                 (center[0] + self.midx, center[1] + self.midy), 2)
                
                if wall['E'] == True or x == self.nx:
                    
                    pg.draw.line(self.window, self.BLACK, (center[0] + self.midx, center[1] + self.midy), 
                                 (center[0] + self.midx, center[1] - self.midy), 2)
                    
                if wall['W'] == True or x == 0:
                    
                    pg.draw.line(self.window, self.BLACK, (center[0] - self.midx, center[1] + self.midy), 
                                 (center[0] - self.midx, center[1] - self.midy), 2)
                
                center[0] += self.dx
                
            center[1] += self.dy
            center[0] = self.midx
            
    def draw_path(self, paths):
        
        print(paths)
        
        clock = pg.time.Clock()
        
        
        prev_x = paths[0][0]
        prev_y = paths[0][1]
        #Start block
        pg.draw.rect(self.window, self.GREEN, [2, 92, self.dx - 2, self.dy - 2])
        
        if prev_x > 0:
            
            pg.draw.rect(self.window, self.GREEN, [(x * self.dx) + 2, 92, 
                                                    self.dx - 2, self.dy - 2])
        elif prev_y > 0:
            
            pg.draw.rect(self.window, self.GREEN, [0, 92 + (y * self.dy), 
                                                    self.dx - 2, self.dy - 2])
             
        
        for path in paths[1:]: 
            
            x = path[0]
            y = path[1]
            
                
            clock.tick(10)
            if x != prev_x:
                pg.draw.rect(self.window, self.GREEN, [ (x * self.dx) + 2, 92 + (y * self.dy), 
                                                    self.dx - 2, self.dy - 2])
            elif y != prev_y:
                pg.draw.rect(self.window, self.GREEN, [ (x * self.dx) + 2, 92 + (y * self.dy), 
                                                    self.dx - 2, self.dy - 2])
                
            x = prev_x
            y = prev_y
            pg.display.update()
            
        
        
    
    def run(self, type, game):
        
        path = []

        if type == "BFS":
            
            bot = Uninformed_AI.BFS()
            path = bot.start(self.maze)
            
        elif type == "DFS":
            bot = Uninformed_AI.DFS()
            path = bot.start(self.maze)
        
        if not self.rerun:
            
            self.draw_path(path)
            self.rerun = True
            
        else:
            
            self.draw_maze(self.maze)
            time.sleep(1)
            self.draw_path(path)
            self.rerun = True

