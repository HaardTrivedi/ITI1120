#ITI1120
#Lab 7
#Friday November 3, 2017

#5.22
def pairsum(lst,n):
    for i in range((len(lst))//2):
        for j in range(len(lst)):
            if lst[i]+lst[j]==n:
                print(i,j)

#5.29
def lastfirst(lst):
    first = []
    last = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == ",":
                last.append(lst[i][:j])
                first.append(lst[i][j+2:])
    print(first, last)

#5.31
def subsetSum(lst, n):
    length = len(lst)
    first = 0
    second = 0
    third = 0
    for i in range(length-2):
        first=lst[i]
        for j in range(i+1, length-1):
            second=lst[j]
            for k in range(j+1, length):
                third=lst[k]
                if (first + second + third) == n:
                    return True
    return False

#5.48
def sublist(l1, l2):
    len1 = len(l1)
    len2 = len(l2)
    if len1==0:
        return True
    for k in range(len2):
        if l1[0] == l2[k]:
            return sublist(l1[1:], l2[k+1:])
    return False

#5.37
def mssl(l):
    a = 0
    for i in range(len(l)):
        for j in range(1, len(l)+1):
            b = sum(l[i:j]) 
            if b > a: 
                a = b
    return a

#main
print("5.22 Pair Sum")
pairsum([7,8,5,3,4,6],11)

print("\n5.29 Last First")
lastfirst(["Gerber, Len", "Fox, Kate", "Dunn, Bob"])

#5.31 subsetSum
subsetSum([5,4,10,20,15,19], 38)
subsetSum([5,4,10,20,15,19], 10)

#5.48 Sublist
sublist([15,1,100],[20,15,30,50,1,100])
sublist([15,50,20],[20,15,30,50,1,100])

#5.37 Max Sum Sublist
mssl([4,-2,-8,5,-2,7,7,2,-6,5])
