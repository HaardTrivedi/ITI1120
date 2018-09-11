# Course: ITI 1120
# Assignment number:Lab 2
# Name: Trivedi, Haard
# Student number:300021545	


import math

def repeater(s1, s2, n):
    return ("_" + (n*(s1+s2)) + "_")

def roots(a, b, c):
    root1 = ((0-b) + math.sqrt(b**2 - 4*a*c))/(2*a) 
    root2 = ((0-b) - math.sqrt(b**2 - 4*a*c))/(2*a)
    return [root1, root2]
   ## return "The quadratic equaiton with coefficients","a =",a,"b =",b,"c =",c,"\nhas the following solutions (ie. roots):",root1,"and",root2

def real_roots(a, b, c):
    x = b**2 - (4*a*c)
    return x>=0
     
def reverse(x):
    y=x//10
    z=x%10
    return (z*10 + y)




