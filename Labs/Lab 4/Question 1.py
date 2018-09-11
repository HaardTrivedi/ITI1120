def is_eligible(age, citizenship, record):    
    if age >=18:
          if (citizenship.strip() == "Canadian") or (citizenship.strip() == "Canada") or (citizenship.strip() == 'canadian') or (citizenship.strip() == 'canada'):
               if (record.strip() == 'yes') or (record.strip() == 'Yes') or (record.strip() == 'YES'):               
                    print(name, ", you are ineligible to vote") 
               else:
                    print(name, ", you are eligible to vote") 
    else:
        print(name, ", you are ineligible to vote")

name=input("What is your name?: ")
age = int(input("How old are you?: "))
citizenship=input("What is your citizenship?: ")
record=input('Are you in prison for a criminal offence?: ')

is_eligible(age, citizenship, record)
