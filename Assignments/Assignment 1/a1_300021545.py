#ITI 1120
#Asssignment 1
#Trivedi, Haard
#300021545

import math
import turtle

#Question 1
def mh2kh(s):
    '''(number) -> number
    Preconditions: "s" is a non-negative number
    Converts speed per hour in miles to speed in kilometres per hour'''
    return s*1.60934
#Question 2
def pythagorean_pair(a,b):
    '''(number, number) -> boolean
    Preconditions: length "a" and length "b" are positive
    Returns whether length "a" and "b" are a pythagorean pair such that they form a 90 degree angle'''
    c2 = (a**2) + (b**2)
    c = math.sqrt(c2)
    mod = c2 % c
    return mod==0
#Question 3    
def in_out(xs,ys,side):
    '''(number, number, number) -> boolean
    Preconditions: "side" is a non-negative number
    Returns whether the coordinates that will be input are part of the square formed from the bottom-left corner using the input location and dimensions'''
    x = float(input("Enter a number for the x coordinate of a query point: "))
    y = float(input("Enter a number for the y coordinate of a query point: "))
    a = (x<=xs+side)
    b = (y<=ys+side)
    return (a==True and b==True)
#Question 4
def safe(n):
    '''(number) -> boolean
    Preconditions: "n" is a non-negative integer with a maximum of two digits
    Returns whether "n" is a safe number'''
    num1 = n%10
    num2 = n%9
    return (num1 != 9 and num2 != 0)
#Question 5
def quote_maker(quote, name, year):
    '''(word, word, number) -> words
    Preconditions: "year" is a non-negative integer and the "quote" and "name" are strings
    Returns a sentence explaning the input information'''
    return "In "+str(year)+", a person named "+name+" said: "+quote
#Question 6
def quote_displayer():
    '''() -> words
    Preconditions: no input in function call
    Returns a sentence explaning the input information'''
    quote = input("Give me a quote: ")
    name = input("Who said that?: ")
    year = int(input("What year did (s)he say that?: "))    
    return quote_maker(quote, name, year)
#Question 7
def rps_winner():
    '''() -> words
    Preconditions: no input in function call
    Returns a sentence verifing whether Player 1 was the winner and whther a tie occurred'''
    p1 = input("What choice did Player 1 make?\nType one of the following options: rock, paper, scissors. ")
    p2 = input("What choice did Player 2 make?\nType one of the following options: rock, paper, scissors. ")
    len1 = len(p1)
    len2 = len(p2)
    win = len1 - len2
    print("Player 1 wins. That is", win==-4 or win==3 or win==1 , "\nIt is a tie. That is" , win==0)
#Question 8    
def fun(x):
    '''(number) -> number
    Preconditions: "x" is a positive number
    Returns y in the equation 10^(4y)=x+3'''
    y = (math.log10(x+3))/4
    return y
#Question 9
def ascii_name_plaque(name):
    '''(words) -> drawing
    Preconditions: "name" is a string
    Prints a name plate with entered string'''
    a = len(name)
    print((8+a)*("*"),"\n*", (a+4)*(" "), "*", "\n*", ("__" + name + "__"), "*", "\n*", (a+4)*(" "), ("*\n" + (8+a)*("*")))
#Question 10
def draw_bike():
    '''() -> drawing
    Preconditions: no input in function call
    Starts a turtle program that draws a bike'''
    wn = turtle.Screen()
    bike = turtle.Turtle()
    #left wheel
    bike.penup()
    bike.setx(-125)
    bike.sety(-100)
    bike.pendown()
    bike.dot(150, 'gray')
    bike.dot(130, 'white')
    bike.dot(30, 'black')
    bike.dot(25,'gray')
    #right wheel
    bike.penup()
    bike.setx(125)
    bike.sety(-100)
    bike.pendown()
    bike.dot(150, 'gray')
    bike.dot(130, 'white')
    bike.dot(30, 'black')
    bike.dot(25,'gray')
    #metal
    bike.left(135)
    bike.pensize(8)
    bike.pencolor('blue')
    bike.forward(50)

    bike.right(45)
    bike.forward(100)
    #handle
    bike.left(75)
    bike.pencolor('pink')
    bike.fd(20)
    bike.bk(40)
    bike.fd(20)
    
    bike.penup()
    bike.left(105)
    bike.pencolor('blue')
    bike.fd(7)
    bike.pendown()
    bike.fd(18)
    bike.right(90)
    bike.fd(150)
    #seat
    bike.right(70)
    bike.fd(20)
    bike.left(70)
    bike.pencolor('brown')
    bike.fd(20)
    bike.bk(40)
    bike.fd(20)

    bike.left(110)
    bike.penup()
    bike.fd(7)
    bike.pendown()
    bike.pencolor('blue')
    bike.fd(110)
    #gear
    bike.penup()
    bike.fd(20)
    bike.pendown()
    bike.dot(50,'black')
    bike.dot(45,'gray')
    bike.dot(30,'black')
    bike.dot(25,'white')
    bike.penup()
    bike.lt(110)
    bike.fd(27)
    bike.pendown()
    bike.goto(90,5)
    bike.penup()
    bike.goto(-60,5)
    bike.pendown()
    
    bike.goto(-115,-90)
    
    bike.penup()
    bike.goto(-110,-100)
    bike.pendown()
    bike.seth(90)
    bike.right(90)
    bike.forward(65)

    bike.penup()
    bike.forward(25)
    bike.lt(75)
    bike.fd(25)
    bike.pendown()
    #top pedal
    bike.pencolor("black")
    bike.fd(20)
    bike.rt(90)
    bike.fd(10)
    bike.bk(20)
    bike.fd(10)
    bike.lt(90)
    #bottom pedal
    bike.penup()
    bike.bk(70)
    bike.lt(10)
    bike.pendown()
    bike.bk(20)
    bike.rt(90)
    bike.fd(10)
    bike.bk(20)
#Question 11
def alogical(n):
    '''(number) -> number
    Preconditions: "n" is a number greater than or equal to 1
    Returns the number of times "n" needs to be divided by two to obtain a number less than or equal to 1'''
    return int(math.ceil(math.log(n,2)))
#Question 12
def time_format(h,m):
    '''(number, number) -> string
    Preconditions: "h" is a non-negative integer less than or equal to 23 and "m" is a non-negative integer less than or equal to 59
    Returns a sentence explaning the input information'''
    min = int(5 * round(float(m)/5))              
    if m==0 or min==0:
        print ("It is", h, "o'clock.")
    elif min==30:
        print ("It is half past", h, "o'clock.")
    elif m<30 and m>0:
        print ("It is", min, "minutes past", h, "o'clock.")
    elif m>30 and m<=55:
        if h==23:
            print ("It is", int(60-min), "minutes to 0 o'clock.")
        else:
            print ("It is", int(60-min), "minutes to", (h+1), "o'clock.")
    elif m>55:
        if h==23:
            print ("It is 0 o'clock.")
        else:
            print ("It is", (h+1), "o'clock.")
#Question 13
def cad_cashier(price,payment):
    '''(number, number) -> number
    Preconditions: "price" is a postive float no more than two decimal places and "price" is less than or equal to "payment"
    Returns the change owed to customer'''
    prx = 0.05*round(float(price)/0.05)
    change = round(payment - prx,2)  
    return change
#Question 14
def min_CAD_coins(price,payment):
    '''(number, number) -> number, number, number, number, number
    Preconditions: "price" is a postive float no more than two decimal places and "price" is less than or equal to "payment"
    Returns the coins needed to give customer the change owed'''
    change = cad_cashier(price,payment)
    t = int(change//2)
    l = int(round((change - (t*2)),2)/1)
    q = int((round((change - (t*2) - l),2)/0.25))
    d = int((round((change - (t*2) - l - (q*0.25)),2)/0.1))
    n = int(round(change - (t*2) - l - (q*0.25) - (d*0.1),2)/0.05)
    return (t, l, q, d, n)

    
