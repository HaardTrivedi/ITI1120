#Task 4
def ah(l,x,y):
    lista = l
    i=0
    while i < len(lista):
        if lista[i]>=x and lista[i]<=y:
            e = lista[i]
            i+=1
        else:
            e = lista[i]
            lista.remove(e)
            i=i
    return (len(lista),min(lista))

#Exercise 2   
def is_perfect(n):
    li=[]
    for i in range(1,(n//2)+1):
        if n%i==0:
            li.append(i)
    return sum(li)==n

def perfect(n):
    for i in range(1,n):
        if is_perfect(i)==True:
            print(i)

#Execise 3a           
def arithematic(l):
    diff = l[1] - l[0]
    for i in range(1,len(l)):
        if (l[i]-l[i-1]) != diff:
            return False
        return True

#Exercise 3b
def is_sorted(l):
    for i in range(1,len(l)):
        if (l[i]-l[i-1]) < 0:
            return False
        return True
