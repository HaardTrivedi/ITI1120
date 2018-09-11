def sum_odd_while_v2(n):
    '''(int)->int
    Returns the sum of all odd integers between 5 and n
    '''
    total = 0
    i = 5

    while i<=n:
        total += i
        i += 2
    return total

def first_neg(l):
    i = 0
    while (i<len(l) and l[i]>=0):
        i+=1
    if (i<len(l) and l[i]<0):
        return i
    else:
        return None

def sum_5_consecutive_for(n):
    if len(n)<4:
        return False
    else:
        for i in range (len(n)-4):
            if (len(n)-1)<5:
                return False
            elif sum(n[i:i+5])==0:
                return True
    return False

def sum_5_consecutive_while(n):
    i = 0
    while (len(n)-i)>=5:
        if sum(n[i:i+5])==0:
            return True
        i+=1
    return False

def fib(n):
    a = [0]*n
    a[0] = 1
    a[1] = 1
    for i in range(2,len(a)):
        a[i] = a[i-1] + a[i-2]
    print (a)

def inner_product(x,y):
    n = len(x)
    suma = 0
    for i in range(n):
        suma+=(x[i]*y[i])
    return suma
            
