#Lab 4
#ITI1120
#Friday October 6, 2017

#1
##
##def is_eligible(age, citizenship, record):
##     age.strip()
##     citizenship.strip()
##     record.strip()
##     if int(age) >=18:
##          if (citizenship == "Canadian") or (citizenship == "Canada") or (citizenship == 'canadian') or (citizenship == 'canada'):
##               if (record == 'yes') or (record == 'Yes') or (record == 'YES'):               
##                    print(name, ", you are ineligible to vote") 
##               else:
##                    print(name, ", you are eligible to vote") 
##     else:
##          print(name, ", you are ineligible to vote")
##
##name=input("What is your name?: ")
##age= input("How old are you?: ")
##citizenship=input("What is your citizenship?: ")
##record=input('Are you in prison for a criminal offence?: ')
##
##is_eligible(age, citizenship, record)

#2
def mess(phrase):
     s = ''
     for x in phrase:
          if x in 'rstvwxyz':
               s = s + x.upper()
          else:
               s = s + x
     s = s.replace(' ', '-')
     return s

#4
#Question
def half_pyramid():
     num = int(input('Enter a number: '))
     symbol = input('Enter a symbol: ')
     for i in range(num):
          print((i+1) * symbol)
#Bonus
def full_pyramid():
     lines = int(input('Enter the number of lines: '))
     symbol = input('Enter a symbol: ')
     for i in range (1,(lines*2),2):
          spc = (lines*2)-i
          print(((spc*' ') + ((i) * (symbol+' '))))
          
#5
def divisors(n):
     print("Divisors")
     s = ''
     for i in range(n):
          if n%(i+1) == 0:
               if i==0:
                  s = s + str(i+1)
               else:
                  s = s + ", " + str(i+1)  
     print(s)

def prime(x):
     print("Prime")
     p=None
     if x > 1:
        for i in range(2, x):
          if (x % i) == 0:
               p = False
     if p==False:
          print(x, "is not a prime number")
     else:
          print(x, "is a prime number")

def all_primes(x):
     print("All primes before", x,":")
     for num in range(1,x):
          if all(num%i!=0 for i in range(2,num)):
               print(num)

     
x = int(input('Enter a number: '))
divisors(x)
prime(x)
all_primes(x)
