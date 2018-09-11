#Haard Trivedi
#300021545
#ITI 1120
#Assignment 5 - Part 3

def digit_sum(n):
    '''(int) -> int
    Returns the sum of all the digits in a non-negative integer
    Preconditions: n is a non-negative integer'''
    if n==0:
        return n
    else:
        return (n%10) + digit_sum(n//10)

def digital_root(n):
    '''(int) -> int
    Returns the sum of all the digits in a non-negative integer until the final number is single-digit number
    Preconditions: n is a non-negative integer'''
    if n>=10:
        return digital_root(digit_sum(n))
    else:
        return n
        
