"""
Project Title:

    Chess

    
Author:

    Jerry Aska
"""
import pygame, sys
import Pieces
from Pieces import box, screen
from pygame.locals import *
from Chess_Constants import *

BOARD = "custom_board_1.txt"
pygame.init()        

DISPLAYSURF     = pygame.display.set_mode((scr_width, scr_height),pygame.RESIZABLE)
game_screen     = screen(width = scr_width, height = scr_height, grid_factor = GRID_FACTOR)
boxes           = list(game_screen % (GRID_FACTOR,WHITE,BLUE))

king_pos = [0, 0]

set_board(BOARD, boxes)
draw_board(DISPLAYSURF, game_screen, boxes)
active = False


side = 0
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            draw_board(DISPLAYSURF, game_screen, boxes)
            x, y = pygame.mouse.get_pos()
            for z in boxes:
                if z.is_clicked(x, y):
                    if active:
                        if z is store:
                            active = False
                            continue
                        elif store.occupied_by.move(boxes.index(z), boxes, king_pos[(side + 1) % 2]):
                            if type(store) is Pieces.king:
                                king_pos[side] = store.occupied_by.pos
                            active = False
                            draw_board(DISPLAYSURF, game_screen, boxes)
                            side = (side + 1) % 2
                            continue
                        else:
                            active = False
                    if not active:
                        if z.occupied:
                            if z.occupied_by.side == side:
                                z.occupied_by.activate(boxes, king_pos[(side + 1) % 2], DISPLAYSURF)
                                active = True
                                store = z
        if event.type == VIDEORESIZE:
            DISPLAYSURF = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            game_screen.resize(event.w, event.h)
            counter = 0
            for x in list(game_screen % (GRID_FACTOR,WHITE,BLUE)):
                boxes[counter].resize(x)
                if boxes[counter].occupied:
                    boxes[counter].occupied_by.resize(boxes)
                counter += 1
            draw_board(DISPLAYSURF, game_screen, boxes)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


