import pygame
"""
Chess Pieces
"""

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
class piece:
    """
    Parent Class for all Piece Objects

    Contains all the attributes and functions shared by all
    piece objects as well as place holder functions for functions
    not yet defined for child objects.
    """
    def __init__(self, img, pos, side):
        self.img        = img
        self.pos        = pos
        self.is_alive   = True
        self.side       = side
        self.moves      = []
        self.first_move = True

    def display(self, boxes, DISPLAYSURF):
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

    def __repr__(self):
        return self.pos


###########################################################################################################################
###########################################################################################################################

        
class pawn(piece):
    """
    Pawn child object of piece

    This object conatins the customized move generatioin function
    for the pawn piece. All other functions are inherited from the
    piece parent class.
    """
    def activate(self, boxes, king_pos, DISPLAYSURF):
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
        
        return self.moves


###########################################################################################################################
###########################################################################################################################

        
class rook(piece):
    """
    Rook child object of piece

    This object conatins the customized move generatioin function
    for the rook piece. All other functions are inherited from the
    piece parent class.
    """
    def activate(self, boxes, king_pos, DISPLAYSURF):
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
        
        return self.moves


###########################################################################################################################
###########################################################################################################################

        
class bishop(piece):
    """
    Bishop child object of piece

    This object conatins the customized move generatioin function
    for the bishop piece. All other functions are inherited from the
    piece parent class.
    """
    def activate(self, boxes, king_pos, DISPLAYSURF):
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
        
        return self.moves


###########################################################################################################################
###########################################################################################################################


class knight(piece):
    """
    Knight child object of piece

    This object conatins the customized move generatioin function
    for the knight piece. All other functions are inherited from the
    piece parent class.
    """
    def activate(self, boxes, king_pos, DISPLAYSURF):
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
        
        return self.moves


###########################################################################################################################
###########################################################################################################################

        
class queen(bishop, rook):
    """
    Queen child object of piece

    This object conatins the customized move generatioin function
    for the queen piece. All other functions are inherited from the
    piece parent class.
    """
    def activate(self, boxes, king_pos, DISPLAYSURF):
        self.moves = [*bishop.activate(self,boxes,king_pos, DISPLAYSURF),
                      *rook.activate(self,boxes,king_pos, DISPLAYSURF)]

        for x in self.moves:
            pygame.draw.circle(DISPLAYSURF, GREEN, (x.pos_x + x.width // 2, x.pos_y + x.height // 2), x.width // 10)
        pygame.display.update()
        
        return self.moves


###########################################################################################################################
###########################################################################################################################


class king(piece):
    """
    King child object of piece

    This object conatins the customized move generatioin function
    for the king piece. All other functions are inherited from the
    piece parent class
    """
    def activate(self, boxes, king_pos, DISPLAYSURF):
        self.moves = []
        add = True
        
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
            
        return self.moves


###########################################################################################################################
###########################################################################################################################


class box:
    """
    Box Object    
    """
    def __init__(self, pos_x = 0, pos_y = 0, width = 0, height = 0,
                 color = (0,0,0), occupied = False, occupied_by = None):
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
        """
        Attribute Magnifier

        Takes a box object, **self**, and a number value, **value**,
        as it's two arguments.

        Returns a box object which is a copy of **self** with
        certain attributes magnified.

        If **value** is positive, the height is magnified by a factor
        of **value**.
        
        If **value** is negative, the width is magnified by a factor
        of **value**.
        
        If **value** is 0, returns an empty box (all attributes are 0).

        If**value** is not of type number, it returns an empty box
        (all attributes are 0) and an error message.

        >>> example = box(0,0,500,500)
        >>> print(example)
        0, 0, 500, 500
        >>> example * 2  #Value > 0
        0, 0, 500, 1000
        >>> example * -2  #Value < 0
        0, 0, 1000, 500
        >>> example * 0  #Value == 0
        0, 0, 0, 0
        >>> example * example  #Value of none number type
        Inappropriate argument type
        0, 0, 0, 0
        """
        try:
            if value > 0:
                return box(self.pos_x, self.pos_y, self.width,
                           int(self.height * value))
            elif value < 0:
                return box(self.pos_x, self.pos_y, int(self.width * -value),
                           self.height)
            elif value == 0:
                return box()
        except TypeError:
            print("Inappropriate argument type")
            return box()

    def __pow__(self,value):
        """
        Attribute Magnifier

        Takes a box object, **self**, and a positive number value, **value**,
        as it's two arguments.

        Returns a box object which is a copy of **self** with
        attributes magnified.

        If **value** is positive, the height and width are both magnified
        by a factor of **value**.
        
        If **value** is negative, it returns an empty box
        (all attributes are 0) and an error message.
        
        If **value** is 0, it returns an empty box (all attributes are 0).
        
         If **value** is not of type number, it returns an empty box
        (all attributes are 0) and an error message.

        >>> example * example
        Inappropriate argument type
        0, 0, 0, 0
        >>> example * "a" #//value of type none number
        Inappropriate argument type
        0, 0, 0, 0
        >>> example = box(0,0,500,500)
        >>> print(example)
        0, 0, 500, 500
        >>> example ** 2  #Value > 0
        0, 0, 1000, 1000
        >>> example ** -2  #Value < 0
        Expected positive integer; got negative
        0, 0, 0, 0
        >>> example ** 0 #Value == 0
        0, 0, 0, 0
        >>> example ** example  #Value of none number type
        Inappropriate argument type
        0, 0, 0, 0
        """
        try:
            if value > 0:
                return box(self.pos_x, self.pos_y, int(self.width * value), int(self.height * value))
            if value < 0:
                print("Expected positive integer; got negative")
            return box()
        except TypeError:
            print("Inappropriate argument type")
            return box()

    def __mod__(self,val):
        """
        Attribute Magnifier

        Takes a box object, **self**, and a tuple as it's two arguments.
        Tuple contains a positive number value, **value**, and two colors,
        **color1**, **color2**.

        Returns a generator of box objects to fill **self** cut into a
        **value** by **value** box.

        Each generated box is of side **self** // **value**. And the colors
        of the box alternate between **color1** and **color2**
        

        >>> example * example
        Inappropriate argument type
        0, 0, 0, 0
        >>> example * "a" #//value of type none number
        Inappropriate argument type
        0, 0, 0, 0
        >>> example = box(0,0,500,500)
        >>> print(example)
        0, 0, 500, 500
        >>> example ** 2  #Value > 0
        0, 0, 1000, 1000
        >>> example ** -2  #Value < 0
        Expected positive integer; got negative
        0, 0, 0, 0
        >>> example ** 0 #Value == 0
        0, 0, 0, 0
        >>> example ** example  #Value of none number type
        Inappropriate argument type
        0, 0, 0, 0
        """
        if not type(val) is int:
            value = val[0]
            color1 = val[1]
            color2 = val[2]
        else:
            value = val
            color1 = (0,0,0)
            color2 = (255,255,255)
        count = 0
        for x in range(value**2):
            item = self // value
            item.pos_x += item.width * (x % value)
            item.pos_y += item.height * (x // value)
            item.rect = (item.pos_x, item.pos_y, item.width, item.height)
            if (count%value + count//value)%2 == 0:
                item.color = color1
            else:
                item.color = color2
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

    def __repr__(self):
        return  ", ".join(map(str,[self.pos_x, self.pos_y, self.width, self.height]))


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

    def display(self, DISPLAYSURF):
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

