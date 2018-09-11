#Question 3A

##def is_divisible(n,m):
##    mod = n%m
##    if mod == 0:
##        return True
##    elif mod != 0:
##        return False
##
##n = int(input("Enter 1st integer: "))
##m = int(input("Enter 2st integer: "))
##
##is_divisible(n,m)
##if is_divisible(n,m)==True:
##    print(n, "is divisible by", m)
##else:
##    print(n, "is not divisible by", m)

def is_divisible23n8(x):
    if x%8 != 0 and x%2 == 0 or x%3 == 0:
        return "Yes"
    else:
        return "No"
x = int(input("Enter an integer: "))
if is_divisible23n8(x)=="Yes":
    print(x, "is divisible by 2 or 3 but not 8")
else:
    print("It is not true that", x, "is divisible by 2 or 3 but not 8")
