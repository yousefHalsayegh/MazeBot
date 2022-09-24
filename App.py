import pygame as pg
from UI import UI

game = UI()


while not game.exit:

    for event in pg.event.get():

        if event.type == pg.QUIT:

            game.exit = True

        elif event.type == pg.MOUSEBUTTONDOWN:
    
            game.button_press(event.pos)

    pg.display.update()
