from tokenize import String
import pygame as pg
from Maze import Maze
from tabulate import tabulate

class UI:

    BLACK = (0 ,0 ,0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    (WIDTH, HEIGHT) = (600, 600)

    nx = 5
    ny = 5
    
    window = None 

    scene = None

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

    def button_press(self, cord):

        if self.generate.collidepoint(cord):

            maze = Maze(self.nx, self.ny, 0, 0)
            maze.generate()

            self.draw_maze(maze)

        elif self.x_button.collidepoint(cord):

           self.input_text(self.x_button.x, self.x_button.y, self.x_button.w, self.x_button.h, self.x_button, 0)

        elif self.y_button.collidepoint(cord):

            self.input_text(self.y_button.x, self.y_button.y, self.y_button.w, self.y_button.h, self.y_button, 1)

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
                            print(self.nx)

                        else:

                            self.ny = int(input) 
                            print(self.ny)

                        done = True
                    
                    elif event.unicode.isdigit():

                        input += event.unicode

                elif event.type == pg.MOUSEBUTTONDOWN:

                    if n == 0:

                        self.nx = int(input) 
                        print(self.nx)

                    else:

                        self.ny = int(input) 
                        print(self.ny)

                    done = True

            pg.display.flip()

            text = self.font.render(input, True, self.BLACK, self.WHITE)
            textRec = text.get_rect()
            textRec.center = button.center
            self.window.blit(eraser, (x + 1 , y + 1))
            self.window.blit(text, textRec)

    def draw_maze(self, maze):
        
        #Reset 
        self.window.blit(self.reset, (0,90))
        
        center = [30, 100]

        for i in range(maze.height):
            
            for j in range(maze.width):
                
                wall = maze.get_cell(j, i).walls
                if (j == 0 and i == 0):
                    print(f'i:{i}, j:{j}')
                    print(f'wall?{wall}')
         
                if wall['N'] == True:
                    
                    pg.draw.line(self.window, self.BLACK, (center[0] - 5, center[1] - 5), (center[0] + 5, center[1] - 5))
                
                if wall['S'] == True:
                    
                    pg.draw.line(self.window, self.RED, (center[0] - 5, center[1] + 5), (center[0] + 5, center[1] + 5))
                
                if wall['E'] == True:
                    
                    pg.draw.line(self.window, self.GREEN, (center[0] + 5, center[1] + 5), (center[0] + 5, center[1] - 5))
                    
                if wall['W'] == True:
                    
                    pg.draw.line(self.window, self.BLUE, (center[0] - 5, center[1] + 5), (center[0] - 5, center[1] + 5))
                
                center[0] += 10
                
            center[1] += 10
            center[0] = 30
            
        print(maze.get_cell(0,0).walls)
        print(maze)
