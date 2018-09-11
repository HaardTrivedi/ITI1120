class Point:
    'class that represents a point in the plane'

## exectuting Point(2,3)
## 1. creates an object of type point
## 2. calls an objects __init__ method
## 3. produces an object's memory address

## Assigning to a new variable using dot operator
## CREATES THAT VARIABLE INSIDE OF THE OBJECT

## Variables INSIDE of an object are called INSTANCE variables

## __init__ is method that is called to initialize the object (create it and initialize its variables)
## the first parameter of method is usually called self
## self refers to the object that is being initialized


#    constructor
#    notice two underscores

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point, float, float) -> None
        >>> p=Point(2,3)
        >>> p.x
        >>> 2
        >>> p.y
        >>> 3

        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,float)->None
        set x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,float)->None
        set y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'
    
    def distance(self,p):
        dx = self.x-p.x
        dy = self.y-p.y
        d = pow((dx**2+dy**2),0.5)
        return d

    def up(self):
        self.y += 1
        
    def down(self):
        self.y = self.y - 1
        
    def left(self):
        self.x = self.x - 1
        
    def right(self):
        self.y += 1


class Animal:
    'represents an animal'

    def __init__(self, species='animal', language='make sounds', age='years'):
        self.spec = species
        self.lang = language
        self.age = age

    def setSpecies(self, species):
        'sets the animal species'
        self.spec = species

    def setLanguage(self, language):
        'sets the animal language'
        self.lang = language

    def speak(self):
        'prints a sentence by the animal'
        print('I am a', self.spec,'and I', self.lang)

    def getAge(self):
        return (self.age)
    


class Bird(Animal): # class Bird inherits all atributes (data and method) from class Animal 
    'represents a bird'

    def speak(self):
        'prints bird sounds'
        return(self.language*3)



class Card:
    'represents a playing card'

    def __init__(self, rank, suit):
        'initialize rank and suit of card'
        self.rank = rank
        self.suit = suit

    def getRank(self):
        'return rank'
        return self.rank

    def getSuit(self):
        'return suit'
        return self.suit    

    def __repr__(self):
        'return formal representation'
        return 'Card('+self.rank+','+self.suit+')'

    def __eq__(self, other):
        'self == other if rank and suit are the same'
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other):
        return self.rank > other.rank
    
    def __ge__(self, other):
        return self.rank >= other.rank
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __le__(self, other):
        return self.rank <= other.rank



class Deck:
    'represents a deck of 52 cards'

    # ranks and suits are Deck class variables
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    # suits is a set of 4 Unicode symbols representing the 4 suits 
    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self):
        'initialize deck of 52 cards'
        self.deck = []          # deck is initially empty

        for suit in Deck.suits: # suits and ranks are Deck
            for rank in Deck.ranks: # class variables
                # add Card with given rank and suit to deck
                self.deck.append(Card(rank,suit))

    def dealCard(self):
        'deal (pop and return) card from the top of the deck'
        return self.deck.pop()

    def shuffle(self):
        'shuffle the deck'
        random.shuffle(self.deck)


    def __len__(self):
        'returns size of deck'
        return len(self.deck)

    def __repr__(self):
        'returns canonical string representation'
        return 'Deck('+str(self.deck)+')'

    def __eq__(self, other):
        '''returns True if decks have the same cards
           in the same order'''
        return self.deck == other.deck


class BankAccount:
    
    def __init__(self,money=0):
        self.money = money

    def withdraw(self,price):
        self.money = self.money - price

    def deposit(self,price):
        self.money += price

    def balance(self):
        return "{:.2f}".format(self.money)

    def __repr__(self):
        return "BankAccount("+"{:.2f}".format(self.money)+")"

class PingPong:

    def __init__(self,state="PONG"):
        self.state = state

    def next(self):
        if (self.state == "PING"):
            self.state = "PONG"
        elif (self.state == "PONG"):
            self.state = "PING"
        return self.state

class Queue:

    def __init__(self):
        self.lst = []

    def enqueue(self,item):
        self.lst.append(item)

    def dequeue(self):
        if (len(self.lst)==0):
            temp =""
        else:
            temp = self.lst[0]
            self.lst.remove(temp)
        return temp

    def isEmpty(self):
        return (self.lst == [])

    def __eq__(self,other):
        return self.lst==other.lst

    def __repr__(self):
        return "Queue("+str(self.lst)+")"

    def __len__(self):
        return len(self.lst)

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __add__(self,v):
        self.x += v.x
        self.y += v.y
        return self

    def __mul__(self,v):
        return self.x*v.y-self.y*v.x

    def __repr__(self):
        return "Vector("+str(self.x)+","+str(self.y)+")"

class Marsupial:
    def __init__(self,color):
        self.color =  color
        self.lst = []
        
    def put_in_pouch(self,string):
        self.lst.append(string)
        
    def pouch_contents(self):
        return self.lst
    
    def __str__(self):
        return "I am a "+self.color+" Marsupial."

class Kangaroo:
    def __init__(self,color,x=0,y=0):
        super().__init__(color) 
        self.x = x
        self.y = y
        
    def __str__(self):
        return "I am a "+self.color+" Kangaroo located at coordinates.("+str(self.x)+","+str(self.y)+")"

    def put_in_pouch(self,string):
        self.lst.append(string)
        
    def pouch_contents(self):
        return self.lst
    
    def jump(self,x,y):
        self.x += x
        self.y += y

class Points:
    def __init__(self,pointslist):
        self.points = pointslist
        
    def add(self,x,y):
        self.points.append(Point(x,y))
        
    def __len__(self):
        return len(self.points)
    
    def __repr__(self):
        return "Points("+str(self.points)+")"
    
    def left_most_point(self):
        temp = self.points[0].x
        for i in range(len(self.points)):
            if (self.points[i].x<temp):
                temp = self.points[i].x
        return self.points[i]
