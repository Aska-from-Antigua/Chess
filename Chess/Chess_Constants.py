import pygame
import Pieces
# colours        R    G    B

WHITE          = (255, 255, 255)
GREY           = (125, 125, 125)
BLACK          = (  0,   0,   0)
RED            = (255,   0,   0)
ORANGE         = (255, 125,   0)
YELLOW         = (255, 255,   0)
GREEN          = (  0, 255,   0)
BLUE           = (  0,   0, 255)
PURPLE         = (255,   0, 255)

list_of_colors         = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, BLACK,
                          WHITE]
list_of_colors_names   = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE",
                          "PURPLE", "BLACK", "WHITE"]

SCREEN_COLOR     = GREEN
SCREEN_RATIO     = 1
GRID_FACTOR      = 8

scr_height             = 700
scr_width              = 600

white_pawn   = pygame.image.load("white_pawn.png")
white_rook   = pygame.image.load("white_rook.png")
white_knight = pygame.image.load("white_knight.png")
white_bishop = pygame.image.load("white_bishop.png")
white_queen  = pygame.image.load("white_queen.png")
white_king   = pygame.image.load("white_king.png")
black_pawn   = pygame.image.load("black_pawn.png")
black_rook   = pygame.image.load("black_rook.png")
black_knight = pygame.image.load("black_knight.png")
black_bishop = pygame.image.load("black_bishop.png")
black_queen  = pygame.image.load("black_queen.png")
black_king   = pygame.image.load("black_king.png")


pictures = [[white_pawn, white_rook, white_knight, white_bishop, white_queen, white_king],
            [black_pawn, black_rook, black_knight, black_bishop, black_queen, black_king]]
pictures = [pictures[0],pictures[1]]

pieces = {
    'P':(Pieces.pawn, 0, 0),
    'R':(Pieces.rook, 1, 0),
    'N':(Pieces.knight, 2, 0),
    'B':(Pieces.bishop, 3, 0),
    'Q':(Pieces.queen, 4, 0),
    'K':(Pieces.king, 5, 0),
    'p':(Pieces.pawn, 0, 1),
    'r':(Pieces.rook, 1, 1),
    'n':(Pieces.knight, 2, 1),
    'b':(Pieces.bishop, 3, 1),
    'q':(Pieces.queen, 4, 1),
    'k':(Pieces.king, 5, 1)
}

def set_board(board_file, boxes):
    with open(board_file, 'r') as f:
        board = list(f.read())

    for x in board:
        if x == "\n":
            board.remove(x)
            
    for x, y in enumerate(board):
        if y in pieces:
            Piece, pic_id, color = pieces[y]
            if x < 40: #top half of board
                side = 1 #1 means moving down
            else: #bottom half of board
                side = 0 #0 means moving up
            boxes[x].occupied_by = Piece(pictures[color][pic_id], x, side)
            boxes[x].occupied = True

def draw_board(DISPLAYSURF, game_screen, boxes):
    DISPLAYSURF.fill(GREY)
    game_screen.display(DISPLAYSURF)
    for x in range(len(boxes)):
        DISPLAYSURF.fill(boxes[x].color, boxes[x].rect)
        if boxes[x].occupied:
            boxes[x].occupied_by.display(boxes, DISPLAYSURF)

def resize(event, scr_height, scr_width, DISPLAYSURF,):
    scr_height = event.h
    sc_width = event.w
    DISPLAYSURF = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    game_screen.resize(event.w, event.h)
    counter = 0
    for x in list(game_screen % (GRID_FACTOR,WHITE,BLUE)):
        boxes[counter].resize(x)
        if boxes[counter].occupied:
            boxes[counter].occupied_by.resize(boxes)
        counter += 1


