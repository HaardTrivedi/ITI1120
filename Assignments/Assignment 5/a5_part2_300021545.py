#Haard Trivedi
#300021545
#ITI 1120
#Assignment 5 - Part 2

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    '''Class represents a rectangle with two points on a plane'''
    
    def __init__(self, bl, tr, colour):
        '''(Rectangle, point, point, string) -> None
        Initializes the two points and the colour of the rectangle'''
        self.bl = bl
        self.tr = tr
        self.colour = colour

    def get_bottom_left(self):
        '''(Rectangle) -> tuple
        Returns a tuple of first/bottom-left point entered'''
        return self.bl

    def get_top_right(self):
        '''(Rectangle) -> tuple
        Returns tuple of second/top-right point entered'''
        return self.tr

    def get_colour(self):
        '''(Rectangle) -> string
        Returns colour of rectangle'''
        return self.colour

    def reset_colour(self, colour):
        '''(Rectangle, string) -> None
        Modifies colour of rectangle to the entered string'''
        self.colour = colour

    def get_perimeter(self):
        '''(Rectangle) -> number
        Returns the sum of the sides of rectangle'''
        return 2*((self.tr.x-self.bl.x) + (self.tr.y-self.bl.y))

    def get_Area(self):
        '''(Rectangle) -> number
        Returns the area of rectangle'''
        return abs(self.tr.x-self.bl.x)*(abs(self.tr.y-self.bl.y))

    def move(self, dx, dy):
        '''(Rectangle, number, number) -> None
        Modifies x and y coordinates of both point of rectangle by dx and dy'''
        self.bl.move(dx, dy)
        self.tr.move(dx, dy)

    def intersects(self, other):
        '''(Rectangle, Rectangle) -> boolean
        Returns whether the two rectangles intersect'''
        return (self.bl.x <= other.tr.x and self.bl.y <= other.tr.y and self.tr.x >= other.bl.x and self.tr.y >= other.bl.y)

    def contains(self, otherx, othery):
        '''(Rectangle, number, number) -> boolean
        Returns whether the coordinates given create a point within the rectangle'''
        return (self.bl.x <= otherx and self.bl.y <= othery and self.tr.x >= otherx and self.tr.y >= othery)

    def __eq__(self, other):
        '''(Rectangle, number, number) -> boolean
        Returns True if the two rectangles have the same two points and colours'''
        return (self.bl == other.bl and self.tr == other.tr and self.colour == other.colour)

    def __repr__(self):
        '''(Point)->string
        Returns canonical string representation Rectangle(Point(x, y), Point(x, y), colour)'''
        return "Rectangle("+str(self.bl)+","+str(self.tr)+","+"'"+self.colour+"')"

    def __str__(self):
        '''(Point)->string
        Returns a string representation in a full sentence of the rectangle'''
        return "I am a "+self.colour+" rectangle with bottom left corner at ("+str(self.bl.x)+", "+str(self.bl.y)+") and top right corner at ("+str(self.tr.x)+", "+str(self.tr.y)+")."

class Canvas:
    '''Class represents multiple rectangles on a plane'''
    
    def __init__(self, reclist=[]):
        '''(Canvas, list of rectangles) -> None
        Initializes the list of rectangles'''
        self.reclist = reclist

    def add_one_rectangle(self, new):
        '''(Canvas, Rectangle) -> None
        Adds a new rectangle into the list of rectangles'''
        self.reclist.append(new)

    def count_same_colour(self, othercolour):
        '''(Canvas, string) -> number
        Returns the amount of occurrances of the othercolour'''
        count = 0
        for rectangle in self.reclist:
            if othercolour == rectangle.colour:
                count+=1
        return count
    
    def total_perimeter(self):
        '''(Canvas) -> number
        Returns the sum of the sum of the sides of all rectangles'''
        perimeter=0
        for rectangle in self.reclist:
            perimeter += rectangle.get_perimeter()
        return perimeter

    def min_enclosing_rectangle(self):
        '''(Canvas) -> string
        Returns the smallest possible rectangle required to fit all the rectangles of the canvas'''
        for rectangle in self.reclist:
            if rectangle == self.reclist[0]:
                maxx=rectangle.tr.x
                maxy=rectangle.tr.y
            else:
                if rectangle.tr.x > maxx:
                    maxx = rectangle.tr.x
                if rectangle.tr.y > maxy:
                    maxy = rectangle.tr.y
        for rectangle in self.reclist:
            if rectangle == self.reclist[0]:
                minx=rectangle.bl.x
                miny=rectangle.bl.y
            else:
                if rectangle.bl.x < minx:
                    minx = rectangle.bl.x
                if rectangle.bl.y < miny:
                    miny = rectangle.bl.y
        return "Rectangle(Point"+str(minx)+","+str(miny)+"),Point("+str(maxx)+","+str(maxy)+"), 'red')"

    def common_point(self):
        '''(Canvas) -> boolean
        Returns True if all the rectangles have one common point of intersection'''
        for rec1 in reclist:
            for rec2 in reclist:
                if rec1.intersects(rec2)==False:
                    return False
        return True

    def __len__(self):
        '''(Canvas) -> integer
        Returns the number of rectangles in the canvas'''
        return len(self.reclist)

    def __repr__(self):
        '''(Canvas) -> string
        Returns a canonical representation of the list of rectangles in the canvas Canvas([Rectangle(Point(x, y), Point(x, y), colour)])'''
        return "Canvas("+str(self.reclist)+")"
