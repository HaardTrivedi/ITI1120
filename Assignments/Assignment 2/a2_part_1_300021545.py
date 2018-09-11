import math
import random
import cmath


def primary_school_quiz(flag, n):
    '''(integer, integer) -> questions
    Preconditions: The variable 'flag' must be either 0 or 1 and 'n' can be any integer aobve 1
    The function takes the 'flag' parameter and provides 'n' number of subtraction questions for option 0 and exponentiation question for option 1'''
    answers=[]
    response=[]
    correct=0
    #Subtraction
    if flag==0:
        print("Subtraction")
        for i in range (n):
            a=random.randint(0,9)
            b=random.randint(0,9)
            xa = a-b
            statement = "What is the result of "+str(a)+"-"+str(b)+"? "
            xr = int(input(statement))
            answers.insert(i,xa)
            response.insert(i,xr)
        for i in range (n):
            if answers[i]==response[i]:
                correct=correct+1
        percent=int((correct/n)*100)
        #End
        if percent>90:
            print("Congratulations"+name+"! You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep.")
        elif percent>70 and percent<90:
            print("You did well"+name+", but I know you can do better.")
        else:
            print("I think you need some more practice "+name+".")
    #Exponentiation    
    elif flag==1:
        print("Exponentiation")
        for i in range (n):
            a=random.randint(0,9)
            b=random.randint(0,9)
            xa = a**b
            statement = "What is the result of "+str(a)+"^"+str(b)+"? "
            xr = int(input(statement))
            answers.insert(i,xa)
            response.insert(i,xr)
        for i in range (n):
            if answers[i]==response[i]:
                correct=correct+1
        percent=int((correct/n)*100)
        #End
        if percent>90:
            print("Congratulations "+name+"! You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep.")
        elif percent>70 and percent<90:
            print("You did well"+name+", but I know you can do better.")
        else:
            print("I think you need some more practice "+name+".")
        pass
    else:
        print("That is an invalid argument")


def high_school_eqsolver(a,b,c):
    '''(integer, integer) -> questions
    Preconditions: The variable 'flag' must be either 0 or 1 and 'n' can be any integer aobve 1
    The function takes the 'flag' parameter and provides 'n' number of subtraction questions for option 0 and exponentiation question for option 1'''
    a = float(a)
    b = float(b)
    c = float(c)
    d = (b**2)-(4*a*c)
    if a!=0 and b!=0 and c!=0:
        if d==0:
            x = ((0-b) + math.sqrt(d))/(2*a)
            print("The quadratic equation "+str(a)+"x^2 "+str(b)+"x "+str(c)+" = 0 has only one solution, a real root:")
            print(x)
        if d>0:
            x1 = ((0-b) + math.sqrt(d))/(2*a)
            x2 = ((0-b) - math.sqrt(d))/(2*a)
            if a>0:
                a = "+ "+str(a)
            if b>0:
                b = "+ "+str(b)
            if c>0:
                c = "+ "+str(c)
            print("The quadratic equation "+str(a)+"x^2 "+str(b)+"x "+str(c)+" = 0 has the following real roots:")
            print(x1,"and",x2)
        elif d<0:
            d = abs(d)
            x1 = math.sqrt(d)/(2*a)
            e = -b/(2*a)
            if a>0:
                a = "+ "+str(a)
            if b>0:
                b = "+ "+str(b)
            if c>0:
                c = "+ "+str(c)
            print("The quadratic equation "+str(a)+"x^2 "+str(b)+"x "+str(c)+" = 0 has the following complex roots:")
            print(e,"+ i",x1,"\nand","\n"+str(e),"- i",x1)
    elif a==0 and b!=0 and c!=0:
        x = (0-c)/b
        if b>0:
            b = "+ "+str(b)
        if c>0:
            c = "+ "+str(c)
        print("The linear equation "+str(b)+"x "+str(c)+" = 0 has the following root/solution: "+x)
    elif a==0 and b==0 and c!=0:
        if b>0:
            b = "+ "+str(b)
        if c>0:
            c = "+ "+str(c)
        print("The linear equation "+str(b)+"x "+str(c)+" = 0 is satisfied for no number x")
    elif a==0 and b==0 and c==0:
        if b>0:
            b = "+ "+str(b)
        if c>0:
            c = "+ "+str(c)
        print("The linear equation "+str(b)+"x "+str(c)+" = 0 is satisfied for all numbers x")
    
def ascii_name_plaque(name):
    a = len(name)
    print((8+a)*("*"),"\n*", (a+4)*(" "), "*", "\n*", ("__" + name + "__"), "*", "\n*", (a+4)*(" "), ("*\n" + (8+a)*("*")))


# main
ascii_name_plaque('Welcome to my math quiz-generator / equation-solver')
name=input("What is your name? ")
status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    ascii_name_plaque(name+', welcome to my quiz-generator for primary school students.')
    flag = input("Press:\n0 for subtraction\n1 for exponentiation\n")
    n = input("How many questions would to like to practice with? ")
    flag = int(flag.strip())
    n = int(n.strip())
    primary_school_quiz(flag, n)

elif status=='2':
    ascii_name_plaque('quadratic equation, ax^2 + bx + c= 0, solver for '+name)
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        question = (question.strip()).lower()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a = int(input("Enter a number the coefficient a: "))
            b = int(input("Enter a number the coefficient b: "))
            c = int(input("Enter a number the coefficient c: "))
            high_school_eqsolver(a,b,c)
 
else:
    print(name+" you are not a target audience for this software.")

print("Good bye "+name+"!")
