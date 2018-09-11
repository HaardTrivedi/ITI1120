#Lab 9
#ITI1120

#Exercise 2
def min_or_max(lst, boolean):
    temp = lst[0]
    index = 0
    if boolean:
        print ("Min:")
        for i in range (len(lst)):
            if (lst[i]<temp):
                temp = lst[i]
                index = i
    else:
        print ("Max:")
        for i in range (len(lst)):
            if (lst[i]>temp):
                temp = lst[i]
                index = i
    print (temp,index)
#Task 5: The above function performs O(n)

#Exercise 3
def first_one(L):
    a = 0
    b = len(L) - 1
 
    while a != b + 1:
        mid = (a + b) // 2
        if L[mid] < 1:
            a=mid+1
        else:
            b=mid-1
          
    if 0 <= a < len(L) and L[a] == 1:
        return a
    else:
        return -1
