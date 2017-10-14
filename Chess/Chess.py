####################################
##
##Jerry Aska
##
##Chess
##
####################################

###########################################################################################################################
##                                                  Constants Declaration
###########################################################################################################################

import pygame, pygame.gfxdraw, sys, random, math
from pygame.locals import *

pygame.init()

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


list_of_colors         = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, BLACK, WHITE]
list_of_colors_names   = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PURPLE", "BLACK", "WHITE"]

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


pictures = [[white_pawn, white_rook, white_knight, white_bishop, white_king, white_queen], [black_pawn, black_rook, black_knight, black_bishop, black_king, black_queen]]
pictures = [pictures[1],pictures[0]]
###########################################################################################################################
##                                                  Classes Definition
###########################################################################################################################

class piece:
    def __init__(self, img, pos, side):
        self.img        = img
        self.pos        = pos
        self.is_alive   = True
        self.side       = side
        self.moves      = []
        self.first_move = True

    def display(self, boxes):
        DISPLAYSURF.blit(self.img, boxes[self.pos])

    def move(self, new_pos, boxes, king_pos):
        if boxes[new_pos] in self.moves:
            boxes[self.pos].occupied = False
            self.pos = new_pos
            if boxes[self.pos].occupied:
                boxes[self.pos].occupied_by.is_alive = False
            boxes[self.pos].occupied = True
            boxes[self.pos].occupied_by = self
            self.first_move = False
            self.post_move(boxes, king_pos)
            return True
        else:
            return False

    def resize(self, boxes):
        x        = boxes[0]
        self.img = pygame.transform.scale(self.img, (x.width, x.height))

    def post_move(self, boxes, king_pos):
        self.moves = []
        print("Piece post move not active")


###########################################################################################################################
###########################################################################################################################

        
class pawn(piece):
    def activate(self, boxes, king_pos):
        self.moves = []
        try:
                    
            if not self.pos // GRID_FACTOR == GRID_FACTOR - 2 * self.side * GRID_FACTOR:
                pos = self.pos - GRID_FACTOR + 2 * GRID_FACTOR * self.side
                if not boxes[pos].occupied:
                    self.moves.append(boxes[pos])
                    if self.first_move:
                        pos = self.pos - 2 * GRID_FACTOR + 4 * GRID_FACTOR * self.side
                        if not boxes[pos].occupied:
                            self.moves.append(boxes[pos])

            if not self.pos % GRID_FACTOR == GRID_FACTOR - 1:
                pos = self.pos - GRID_FACTOR + 2* GRID_FACTOR * self.side + 1
                if boxes[pos].occupied and (boxes[pos].occupied_by.side != self.side):
                    self.moves.append(boxes[pos])

            if not self.pos % GRID_FACTOR == 0:
                pos = self.pos - GRID_FACTOR + 2 * GRID_FACTOR * self.side - 1
                if boxes[pos].occupied and (boxes[pos].occupied_by.side != self.side):
                    self.moves.append(boxes[pos])
        except IndexError:
            pass
        for x in self.moves:
            pygame.draw.circle(DISPLAYSURF, GREEN, (x.pos_x + x.width // 2, x.pos_y + x.height // 2), x.width // 10)
        pygame.display.update()


###########################################################################################################################
###########################################################################################################################

        
class rook(piece):
    def activate(self, boxes, king_pos):
        self.moves = []

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x += 1
            check = check_y * GRID_FACTOR + check_x
            if check_x >= GRID_FACTOR:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x -= 1
            check = check_y * GRID_FACTOR + check_x
            if check_x < 0:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_y += 1
            check = check_y * GRID_FACTOR + check_x
            if check_y >= GRID_FACTOR:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_y -= 1
            check = check_y * GRID_FACTOR + check_x
            if check_y < 0:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        for x in self.moves:
            pygame.draw.circle(DISPLAYSURF, GREEN, (x.pos_x + x.width // 2, x.pos_y + x.height // 2), x.width // 10)
        pygame.display.update()


###########################################################################################################################
###########################################################################################################################

        
class bishop(piece):
    def activate(self, boxes, king_pos):
        self.moves = []

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x += 1
            check_y += 1
            check = check_y * GRID_FACTOR + check_x
            if check_x >= GRID_FACTOR or check_y >= GRID_FACTOR:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x -= 1
            check_y -= 1
            check = check_y * GRID_FACTOR + check_x
            if check_x < 0 or check_y < 0:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x -= 1
            check_y += 1
            check = check_y * GRID_FACTOR + check_x
            if check_x < 0 or check_y >= GRID_FACTOR:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x += 1
            check_y -= 1
            check = check_y * GRID_FACTOR + check_x
            if check_x >= GRID_FACTOR or check_y < 0:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        for x in self.moves:
            pygame.draw.circle(DISPLAYSURF, GREEN, (x.pos_x + x.width // 2, x.pos_y + x.height // 2), x.width // 10)
        pygame.display.update()


###########################################################################################################################
###########################################################################################################################


class knight(piece):
    def activate(self, boxes, king_pos):
        self.moves = []

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x -= 1
        check_y -= 2
        check = check_y * GRID_FACTOR + check_x
        if not (check_x < 0 or check_y < 0):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x += 1
        check_y -= 2
        check = check_y * GRID_FACTOR + check_x
        if not (check_x >= GRID_FACTOR or check_y < 0):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x -= 1
        check_y += 2
        check = check_y * GRID_FACTOR + check_x
        if not (check_x < 0 or check_y >= GRID_FACTOR):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x += 1
        check_y += 2
        check = check_y * GRID_FACTOR + check_x
        if not (check_x >= GRID_FACTOR or check_y >= GRID_FACTOR):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])


        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x -= 2
        check_y -= 1
        check = check_y * GRID_FACTOR + check_x
        if not (check_x < 0 or check_y < 0):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x += 2
        check_y -= 1
        check = check_y * GRID_FACTOR + check_x
        if not (check_x >= GRID_FACTOR or check_y < 0):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x -= 2
        check_y += 1
        check = check_y * GRID_FACTOR + check_x
        if not (check_x < 0 or check_y >= GRID_FACTOR):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x += 2
        check_y += 1
        check = check_y * GRID_FACTOR + check_x
        if not (check_x >= GRID_FACTOR or check_y >= GRID_FACTOR):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        for x in self.moves:
            pygame.draw.circle(DISPLAYSURF, GREEN, (x.pos_x + x.width // 2, x.pos_y + x.height // 2), x.width // 10)
        pygame.display.update()


###########################################################################################################################
###########################################################################################################################

        
class queen(piece):
    def activate(self, boxes, king_pos):
        self.moves = []

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x += 1
            check = check_y * GRID_FACTOR + check_x
            if check_x >= GRID_FACTOR:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x -= 1
            check = check_y * GRID_FACTOR + check_x
            if check_x < 0:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_y += 1
            check = check_y * GRID_FACTOR + check_x
            if check_y >= GRID_FACTOR:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_y -= 1
            check = check_y * GRID_FACTOR + check_x
            if check_y < 0:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x += 1
            check_y += 1
            check = check_y * GRID_FACTOR + check_x
            if check_x >= GRID_FACTOR or check_y >= GRID_FACTOR:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x -= 1
            check_y -= 1
            check = check_y * GRID_FACTOR + check_x
            if check_x < 0 or check_y < 0:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x -= 1
            check_y += 1
            check = check_y * GRID_FACTOR + check_x
            if check_x < 0 or check_y >= GRID_FACTOR:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        while True:
            check_x += 1
            check_y -= 1
            check = check_y * GRID_FACTOR + check_x
            if check_x >= GRID_FACTOR or check_y < 0:
                break
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    break
            self.moves.append(boxes[check])
            if boxes[check].occupied:
                break

        for x in self.moves:
            pygame.draw.circle(DISPLAYSURF, GREEN, (x.pos_x + x.width // 2, x.pos_y + x.height // 2), x.width // 10)
        pygame.display.update()


###########################################################################################################################
###########################################################################################################################


class king(piece):
    def activate(self, boxes, king_pos):
        self.moves = []
        add = True

##        if self.first_move:          
##            check_x = self.pos % GRID_FACTOR
##            check_y = self.pos // GRID_FACTOR
##            check_x += 1
        
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x += 1
        check = check_y * GRID_FACTOR + check_x
        if not check_x >= GRID_FACTOR:
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x -= 1
        check = check_y * GRID_FACTOR + check_x
        if not check_x < 0:
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_y += 1
        check = check_y * GRID_FACTOR + check_x
        if not check_y >= GRID_FACTOR:
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_y -= 1
        check = check_y * GRID_FACTOR + check_x
        if not check_y < 0:
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x += 1
        check_y += 1
        check = check_y * GRID_FACTOR + check_x
        if not (check_x >= GRID_FACTOR or check_y >= GRID_FACTOR):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x -= 1
        check_y -= 1
        check = check_y * GRID_FACTOR + check_x
        if not (check_x < 0 or check_y < 0):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x -= 1
        check_y += 1
        check = check_y * GRID_FACTOR + check_x
        if not (check_x < 0 or check_y >= GRID_FACTOR):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        add = True
        check_x = self.pos % GRID_FACTOR
        check_y = self.pos // GRID_FACTOR
        check_x += 1
        check_y -= 1
        check = check_y * GRID_FACTOR + check_x
        if not (check_x >= GRID_FACTOR or check_y < 0):
            if boxes[check].occupied:
                if boxes[check].occupied_by.side == self.side:
                    add = False
            if add:
                self.moves.append(boxes[check])

        for x in self.moves:
            pygame.draw.circle(DISPLAYSURF, GREEN, (x.pos_x + x.width // 2, x.pos_y + x.height // 2), x.width // 10)
        pygame.display.update()

##    def move(self, new_pos, boxes, king_pos):
##        if boxes[new_pos] in self.moves:
##            boxes[self.pos].occupied = False
##            self.pos = new_pos
##            if boxes[self.pos].occupied:
##                boxes[self.pos].occupied_by.is_alive = False
##            boxes[self.pos].occupied = True
##            boxes[self.pos].occupied_by = self
##            self.first_move = False
##            self.post_move(boxes, king_pos)
##            return [True, self.pos]
##        else:
##            return [False, self.pos]


###########################################################################################################################
###########################################################################################################################


class box:
    def __init__(self, pos_x = 0, pos_y = 0, width = 0, height = 0, color = BLACK, occupied = False, occupied_by = None):
        self.pos_x          = pos_x
        self.pos_y          = pos_y
        self.height         = height
        self.width          = width
        self.rect           = (self.pos_x, self.pos_y, self.width, self.height)
        self.color          = color
        self.occupied       = False
        self.occupied_by    = occupied_by

    def resize(self, box):
        self.pos_x          = box.pos_x
        self.pos_y          = box.pos_y
        self.height         = box.height
        self.width          = box.width
        self.rect           = (self.pos_x, self.pos_y, self.width, self.height)

    def is_clicked(self, mouse_pos_x, mouse_pos_y):
        if mouse_pos_x > self.pos_x and mouse_pos_x < self.pos_x + self.width:
            if mouse_pos_y > self.pos_y and mouse_pos_y < self.pos_y + self.height:
                return True
        return False

    def __mul__(self,value):
        try:
            if value > 0:
                return box(self.pos_x, self.pos_y, self.width, int(self.height * value))
            elif value < 0:
                return box(self.pos_x, self.pos_y, int(self.width * -value), self.height)
            elif value == 0:
                return box()
        except TypeError:
            print("Inappropriate argument type")
            return box()

    def __pow__(self,value):
        try:
            if value > 0:
                return box(self.pos_x, self.pos_y, int(self.width * value), int(self.height * value))
            if value < 0:
                print("Expected positive integer; got negative")
            elif value == 0:
                pass
            return box()
        except TypeError:
            print("Inappropriate argument type")
            return box()

    def __mod__(self,val):
        value = val[0]
        count = 0
        for x in range(value**2):
            item = self // value
            item.pos_x += item.width * (x % value)
            item.pos_y += item.height * (x // value)
            item.rect = (item.pos_x, item.pos_y, item.width, item.height)
            if (count%value + count//value)%2 == 0:
                item.color = val[1]
            else:
                item.color = val[2]
            count+=1
            yield item

    def __floordiv__(self, value):
        try:
            if value > 0:
                return box(self.pos_x, self.pos_y, int(self.width / value), int(self.height / value))
            if value < 0:
                print("Expected positive integer; got negative")
            elif value == 0:
                print("Cannot divide by 0")
            return box()
        except TypeError:
            print("Inappropriate argument type:",value)
            return box()

    def __truediv__(self, value):
        try:
            if value > 0:
                return box(self.pos_x, self.pos_y, self.width, int(self.height / value))
            elif value < 0:
                return box(self.pos_x, self.pos_y, int(self.width / -value), self.height)
            elif value == 0:
                print("Cannot divide by 0")
            return box()
        except TypeError:
            print("Inappropriate argument type")
            return box()

    def __iter__(self):
        return self.pos_x, self.pos_y, self.width, self.height


###########################################################################################################################
###########################################################################################################################

        
class screen(box):
    def __init__(self, pos_x = 0, pos_y = 0, width = scr_width, height = scr_height, color = SCREEN_COLOR, ratio = SCREEN_RATIO, grid_factor = GRID_FACTOR):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.rect = (pos_x, pos_y, width, height)
        self.color = color
        self.ratio = ratio
        self.grid_factor = grid_factor
        self.factor = 1
        self.resize(width, height)

    def display(self):
        DISPLAYSURF.fill(self.color, self.rect)

    def resize(self, new_width, new_height, displace_x = 0, displace_y = 0):
        new_width = new_width - displace_x - new_width % self.grid_factor
        new_height = new_height - displace_y - new_height % self.grid_factor
        ratio = new_width / new_height
        if ratio >= self.ratio:
            self.width   = int(new_height * self.ratio)
            self.height  = new_height
            self.pos_x   = displace_x + (new_width - self.width) // 2
            self.pos_y   = displace_y
        if ratio < self.ratio:
            self.width   = new_width
            self.height  = int(new_width / self.ratio)
            self.pos_x   = displace_x
            self.pos_y   = displace_y + (new_height - self.height) // 2
        self.rect = (self.pos_x, self.pos_y, self.width, self.height)


###########################################################################################################################
###########################################################################################################################

        

DISPLAYSURF     = pygame.display.set_mode((scr_width, scr_height),pygame.RESIZABLE)
game_screen     = screen(width = scr_width, height = scr_height, grid_factor = GRID_FACTOR)
boxes           = list(game_screen % (GRID_FACTOR,WHITE,BLUE))


side = 1
positions = [[0, 7, 1, 6, 2, 5, 3, 4],[56, 63, 57, 62, 58, 61, 59, 60]]

king_pos = [0, 0]

pawn_rows = [8,48]
royal_rows = [0,56]
for pos in [1, 0]:
    side = (side + 1) % 2
    for x in list(map(lambda y: y + pawn_rows[pos], range(8))):
        boxes[x].occupied_by = pawn(pictures[pos][0], x, side)
        boxes[x].occupied = True
    for y in [0, 7]:
        x = y + royal_rows[pos]
        boxes[x].occupied_by = rook(pictures[pos][1], x, side)
        boxes[x].occupied = True
    for y in [1, 6]:
        x = y + royal_rows[pos]
        boxes[x].occupied_by = knight(pictures[pos][2], x, side)
        boxes[x].occupied = True
    for y in [2, 5]:
        x = y + royal_rows[pos]
        boxes[x].occupied_by = bishop(pictures[pos][3], x, side)
        boxes[x].occupied = True
    for y in [4]:
        x = y + royal_rows[pos]
        boxes[x].occupied_by = king(pictures[pos][4], x, side)
        boxes[x].occupied = True
        king_pos[pos] = x
    for y in [3]:
        x = y + royal_rows[pos]
        boxes[x].occupied_by = queen(pictures[pos][5], x, side)
        boxes[x].occupied = True


def draw_board():
    DISPLAYSURF.fill(GREY)
    game_screen.display()
    for x in range(len(boxes)):
        DISPLAYSURF.fill(boxes[x].color, boxes[x].rect)
        if boxes[x].occupied:
            DISPLAYSURF.blit(boxes[x].occupied_by.img,boxes[x].rect)
draw_board()
active = False

side = 0

while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            draw_board()
            x, y = pygame.mouse.get_pos()
            for z in boxes:
                if z.is_clicked(x, y):
                    if active:
                        if z is store:
                            active = False
##                        elif type(store) is king:
##                            data = store.occupied_by.move(boxes.index(z), boxes, king_pos[(side + 1) % 2])
##                            if data[0]:
##                                active = False
##                                draw_board()
##                                king_pos[side] = data[1]
##                                side = (side + 1) % 2
##                            else:
##                                print(side)
                        elif store.occupied_by.move(boxes.index(z), boxes, king_pos[(side + 1) % 2]):
                            if type(store) is king:
                                king_pos[side] = store.occupied_by.pos
                            active = False
                            draw_board()
                            side = (side + 1) % 2
                        else:
                            if z.occupied:
                                if z.occupied_by.side == side:
                                    z.occupied_by.activate(boxes, king_pos[side])
                                    active = True
                                    store = z
                    elif not active:
                        if z.occupied:
                            if z.occupied_by.side == side:
                                z.occupied_by.activate(boxes, king_pos[(side + 1) % 2])
                                active = True
                                store = z
        if event.type == VIDEORESIZE:
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
            draw_board()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


