# ITI1120
# Exercise Target
# Trivedi, Haard
# 30021545
# 06/15/09/17

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

alex.circle(10)
#Small circle
alex.left(90)
alex.penup()
alex.forward(10)
alex.left(90)
alex.forward(20)
alex.pendown()
alex.left(90)
alex.circle(20)
#Middle circle
alex.left(90)
alex.penup()
alex.forward(20)
alex.left(90)
alex.forward(40)
alex.pendown()
alex.left(90)
#Big circle
alex.circle(40)
#Top-Bottom
alex.left(90)
alex.backward(60)
alex.forward(200)
alex.backward(100)
#Left-Right
alex.left(90)
alex.forward(100)
alex.backward(200)
alex.forward(100)
#Diagonal 1
alex.left(45)
alex.forward(100)
alex.backward(200)
alex.forward(100)
#Diagonal 2
alex.right(90)
alex.backward(100)
alex.forward(200)

wn.exitonclick()

