#Haard Trivedi
#300021545
#ITI 1120
#Assignment 5 - Part 1

def largest_34(a):
    '''(list of numbers) -> number
    Returns the third and fourth largest values in the list
    Preconditions: the list must contain at least four numbers'''
    a.sort()
    return a[-3] + a[-4]

def largest_third(a):
    '''(list of numbers) -> number
    Returns the sum of the values from the last third of the list
    Preconditions: the list must contain at least three numbers'''
    a.sort()
    return sum(a[-(len(a)//3):len(a)])

def third_at_least(a):
    '''(list of numbers) -> number
    Returns the third and fourth largest values in the list
    Preconditions: the list must contain at least three numbers'''
    a.sort()
    for i in range(len(a)-3):
        if a[i]==a[i+2]:
            return i
    return None

def sum_tri(a,x):
    '''(list of numbers, number) -> boolean
    Returns True if three numbers in the list add up to the number x
    Preconditions: the list must contain at least 3 numbers'''
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i]+a[j]+a[k]==x:
                    return True
    return False
