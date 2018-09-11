####### STUDENT INFO ########
# Course: ITI 1120
# Assignment number: Lab 1
# Name: Lu, Field
# Student number: 123456789
#############################

## This program draws a smile face by using turtle class

# import necessary packages
import turtle 

# Initialize turtle
s=turtle.Screen() # create a canvas 
t=turtle.Turtle(shape='turtle') # create a turtle at (0,0)

#  start painting

# draw a big circle
t.penup()
t.goto(0,-150)
t.pendown()
t.circle(150)


# draw left eye
t.penup()
t.goto(-75,50)
t.pendown()
t.setheading(45)
t.circle(-30,90)

# draw right eye
t.penup()
t.goto(75,50)
t.pendown()
t.setheading(135)
t.circle(30,90)

# draw nose
t.penup()
t.goto(0,0)
t.dot(20,'black')
t.pendown()

# draw mouth
t.penup()
t.goto(-40,-50)
t.pendown()
t.setheading(-90)
t.circle(40,180)


t.penup()
t.goto(200,-200)

