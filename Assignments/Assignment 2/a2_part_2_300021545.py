import math

def min_enclosing_rectangle(radius, x, y):
    '''(integer,integer,integer) -> None
    Preconditions: The variable 'radius' must be a positive integer
    The functino takes the parameters and returns the smallest axis-aligned rectangle enclosing the circle'''
    if radius>=0:
        return (x-radius),(y-radius)
    else:
        return None

def series_sum():
    '''(none) -> integer
    Preconditions: The parameter input when prompted has to be a non-negative integer
    The function adds the all the squared reciprocals until the squared reciprocal of the number that was input'''
    n = int(input("Please enter a non-negative integer: "))
    if n>0:
        x = 1000
        for i in range(n):
            x = x + 1/((i+1)**2)
        return x
    elif n==0:
        return 1000
    else:
        return None

def pell(n):
    '''(integer) -> integer
    Preconditions: To obtain an integer response, the parameter should be a non-negative integer
    The function returns 2 times the previous number added to second last number before 'n' in a sequence that starts from 0 and 1'''
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return round(((1+math.sqrt(2))**n - (1-math.sqrt(2))**n)/(2*math.sqrt(2)))
    else:
        return None

def countMembers(s):
    '''(string) -> integer
    Preconditions: Enter string in quatations marks
    The function returns the number of extraordinary characters from string entered'''
    l = list(s)
    x = 0
    for i in range(len(l)):
        if l[i] >= 'e' and l[i] <= 'j':
            x+=1
        elif l[i] >= 'F' and l[i] <= 'X':
            x+=1
        elif l[i] >= str(2) and l[i] <= str(6):
            x+=1
        elif l[i] == '!' or l[i] == ',' or l[i] == '\\':
            x+=1
    return x

def casual_number(s):
    '''(string) -> integer
    Preconditions: To obtain an integer, enter an integer in quatations 
    The function returns the integer entered without the commmas'''
    l = list(s)
    i=0
    negative = 0
    while i < len(l):
        if l[i] == ',':
            l.remove(',')
            i=i
        elif l[i] == '-':
            negative = negative + 1
            if negative > 1:
                return None
            i+=1
        elif int(l[i]) >= 0 and int(l[i]) <= 9:
            i+=1
        else:
            return None
    if (''.join(l).isdigit()) == True:
        return int(''.join(l))
    elif (l[0] in ('-')) and ''.join(l[1:]).isdigit() == True:
        return int(''.join(l))
    else:
        return None

def alienNumbers(s):
    '''(string) -> integer
    Preconditions: Enter string with T, y, e, a, N, U 
    The function returns the total according to the values given'''
    l = list(s)
    T=0
    y=0
    e=0
    a=0
    N=0
    U=0
    for i in range(len(s)):
        if l[i] == 'T':
            T+=1
        elif l[i] == 'y':
            y+=1
        elif l[i] == '!':
            e+=1
        elif l[i] == 'a':
            a+=1
        elif l[i] == 'N':
            N+=1
        elif l[i] == 'U':
            U+=1
    return (1024*T)+(598*y)+(121*e)+(42*a)+(6*N)+U

def alienNumbersAgain(s):
    '''(string) -> integer
    Preconditions: Enter string with T, y, e, a, N or U 
    The function returns the total according to the values given'''
    l = list(s)
    T=0
    y=0
    e=0
    a=0
    N=0
    U=0
    for i in range(len(s)):
        if l[i] == 'T':
            T+=1
        elif l[i] == 'y':
            y+=1
        elif l[i] == '!':
            e+=1
        elif l[i] == 'a':
            a+=1
        elif l[i] == 'N':
            N+=1
        elif l[i] == 'U':
            U+=1
    return (1024*T)+(598*y)+(121*e)+(42*a)+(6*N)+U

def encrypt(s):
    '''(string) -> string
    Preconditions: Enter string  
    The function returns a jumbled version of the string entered with the order reversed and the first and last objects placed after one another'''
    l = list(reversed(list(s)))
    m = []
    a = 0
    b = -1
    c = 1
    for i in range(0,len(l)//2,1):
        m.append(l[i])
        m.append(l[b])
        b=b-1
    return ''.join(m)

def oPify(s):
    '''(string) -> string
    Preconditions: Enter a string with quatations
    The function returns a string with 'o' and 'p' included between two letters with them being capital if the letters are capital'''
    l = list(s)
    for i in range(len(l)-1):
        if len(l)==1:
            return l
        elif len(l)>1:
            if i<len(l)-1:
                if l[i] >= 'a' and l[i] <= 'z':
                    l[i] = str(l[i])+'o'
                    if l[i+1] >= 'a' and l[i+1] <= 'z':
                        l[i+1] = 'p'+str(l[i+1])
                    elif l[i+1] >= 'A' and l[i+1] <= 'Z':
                        l[i+1] = 'P'+str(l[i+1])
                elif l[i] >= 'A' and l[i] <= 'Z':
                    l[i] = str(l[i])+'O'
                    if l[i+1] >= 'a' and l[i+1] <= 'z':
                        l[i+1] = 'p'+str(l[i+1])
                    elif l[i+1] >= 'A' and l[i+1] <= 'Z':
                        l[i+1] = 'P'+str(l[i+1])
    return ''.join(l)

def nonrepetitive(s):
    '''(string) -> string
    Preconditions: 's' has to be a string
    The function returns whether it has repetitive substrings'''
    l = list(s)
    if len(l)==0 or len(l)==1:
        return True
    else:
        for i in range(len(l)-1):
            for j in range(len(l)//2):
                for k in range(len(l)//2):
                    if l[i:i+j+1]==l[i+j:i+j+k+1]:
                        return False
        l = list(reversed(l))
        for i in range(len(l)-1):
            for j in range(len(l)//2):
                for k in range(len(l)//2):
                    if l[i:i+j+1]==l[i+j:i+j+k+1]:
                        return False
    return True
