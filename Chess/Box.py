"""
Box Object
"""
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

