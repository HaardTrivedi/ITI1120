# ITI1120
# Exercise Ocean View
# Trivedi, Haard
# 30021545
# 06/15/09/17

import turtle
wn = turtle.Screen()
tim = turtle.Turtle()
#Sun
tim.penup()
tim.setx(-250)
tim.sety(150)
tim.pendown()
#tim.circle(50)
tim.dot(100, 'yellow')
#Water
tim.penup()
tim.setx(-300)
tim.sety(-100)
tim.pendown()
tim.right(90)
x=0
while (x<5):
    tim.circle(60,180)
    tim.right(180)
    x=x+1
wn.bgcolor('blue')
wn.exitonclick()
