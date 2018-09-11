import random

class Person:
    def __init__(self, id, name, friends):
        '''(Person, integer, string, list of integers) -> None
        Initializes the ID, user's name and user's friends
        Preconsitions: ID is a non-negative integer, name is a string and friends is a list of non-negative integers'''
        self.id = id
        self.name = name
        self.friends = friends
        
    def get_friends(self):
        '''(Person) -> list of integers
        Returns the list of the person's friends'''
        return self.friends

    def __max__(self):
        '''(Person) -> integer
        Returns the highest ID from the list of friends'''
        return max in self.friends

    def __repr__(self):
        '''(Person) -> string
        Returns canonical string representation Person(ID, Name, Friends)'''
        return 'Person('+str(self.id)+','+self.name+','+str(self.friends)+')'

    def __str__(self):
        '''(Person) -> string
        Returns canonical string representation Person(ID, Name, Friends)'''
        return 'Person('+str(self.id)+','+self.name+','+str(self.friends)+')'

    def __id__(self):
        '''(Person) -> integer
        Returns the id of the current user'''
        return self.id
    
class Network:
    def __init__(self, file1, file2, users=[]):
        '''(Network, string, string, list) -> None
        Initializes people inside of social network
        Preconditions: file1 is a file with names and file2 is the file with only numbers'''
        names = open(file1).read().splitlines()
        friends = open(file2).read().splitlines()
        network=[]

        friends.pop(0)
        
        temp=[]
        f1=[]
        f2=[]
        f3=[]
        for mutual in friends:
            mutual=mutual.split(" ")
            fa=(int(mutual[0].strip()))
            fb=(int(mutual[1].strip()))
            temp.append([fa,fb])
            temp.append([fb,fa])
            f1.append(fa)
            f1.append(fb)
        temp.sort()
        f1.sort()
        a = 0
        
        while a in range(len(f1)-1):
            if f1[a]==f1[a+1]:
                  f1.pop(a)
                  a=a
            else:
                  a+=1
        b = 0
        while b in range(len(temp)-1):
            if temp[b][0]==temp[b+1][0]:
                if b==len(temp)-2:
                    f2.append(temp[b][1])
                    f2.append(temp[b+1][1])
                    f3.append(f2)
                    temp.pop(b)
                else:
                    f2.append(temp[b][1])
                    temp.pop(b)
                    b=b
            else:
                if b==len(temp)-2:
                    f2.append(temp[b][1])
                    f3.append(f2)
                    f3.append([temp[b+1][1]])
                    b+=1
                else:
                    f2.append(temp[b][1])
                    f3.append(f2)
                    temp.pop(b)
                    f2=[]
                    b=b
        
        for i in range(len(f1)):
            network.append([f1[i],f3[i]])
        
        temp2=[]
        for people in names:
            people=people.split("\t")
            temp2.append([int(people[0]), people[1]])

        users=[]
        for j in range(len(network)):
            users.append(Person(network[j][0], temp2[j][1], network[j][1]))
            
        self.users = users

    def get_uid(self):
        '''(Network)->int
        Keeps on asking for a user ID that exists in the network until it succeeds. Then it returns it
        Preconsitions: User must be in the file'''
        
        flag=False

        while flag!=True:
            user = (input("Enter a user ID: "))
            try:
               user = int(user)
            except ValueError:
                print("That was not an integer. Please try again.")
                flag=False
            else:
                for i in range(len(self)):
                    if int(user) == self.users[i].id:
                        flag=True
                if flag==False:
                    print("That user ID does not exist. Try again.")
            
        return user

    def recommend(self, user):
        '''(Network, integer)->integer or None
        Given a 2D-list for friendship network, returns None if there is no other person
        who has at least one neighbour in common with the given user and who the user does
        not know already. Otherwise it returns the ID of the recommended friend. A recommended friend is a person
        you are not already friends with and with whom you have the most friends in common in the whole network.
        If there is more than one person with whom you have the maximum number of friends in common
        return the one with the smallest ID
        Preconditions: User must be in the file'''
        count=[]
        lis=[]
        rec=None

        for j in range(len(self.users)):
            if user not in self.users[j].friends and user!=self.users[j].id:
                lis.append(self.users[j].id)

        for i in range(len(lis)):
            a=self.getCommonFriends(user, lis[i])
            if len(count)<len(a):
                count=[]
                for item in a:
                    count.append(item)
                rec=lis[i]
                
        return rec

    def getCommonFriends(self, user1, user2):
        '''(Network, integer, integer) ->integer
        Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
        and friends of user 1 and user 2 sorted 
        Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2'''
        common=[]
        list1=[]
        list2=[]
        tot=[]
        for x in range(len(self)):
            if self.users[x].id==user1:
                list1.append((self.users[x].friends))
            if self.users[x].id==user2:
                list2.append((self.users[x].friends))
                        
        for i in range(len(list1[0])):
            tot.append(list1[0][i])
        for j in range(len(list2[0])):
            tot.append(list2[0][j])

        tot.sort()
        a = 0
        while a in range(len(tot)-1):
             if tot[a]==tot[a+1]:
                  common.append(tot[a])
                  a+=2
             else:
                  a+=1
                  
        return common

    def network(self):
        '''(Network) -> list
        Returns the list of members in network'''
        return self.users

    def __len__(self):
        '''(Network) -> integer
        Returns the numbers of users in the network'''
        return len(self.users)

    def __repr__(self):
        '''(Network) -> string
        Returns canonical string representation Network([Person(ID, Name, [Friends])])'''
        return 'Network('+str(self.users)+')'

    def __str__(self):
        '''(Network) -> string
        Returns canonical string representation Network([Person(ID, Name, [Friends])])'''
        return 'Network('+str(self.users)+')'

#------------------------------------------------------------------------------#
def get_int():
    '''None->int or None'''
    num = None
    try:
        num=int(input("Enter an integer for a user ID:").strip())
    except ValueError:
        print("That was not an integer. Please try again.")
    return num           

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name
    
    

##############################
# main
##############################
print("Let's get first file that contains IDs and names:")
file_name1=get_file_name()
print("Let's get the 2nd file that contains pairs of friends as in Assignment 4")
file_name2=get_file_name()


net=Network(file_name1,file_name2)
print("Here are all the people in the network, if the network has at most 20 users:")
if len(net)<=20:
    print(net)


print("\nLet's recommend a friend for a user you specify.")
uid=net.get_uid()
rec=net.recommend(uid)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(net.getCommonFriends(uid,rec)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=net.get_uid()
print("About 2st user ...")
uid2=net.get_uid()
print("Here is the list of common friends of", uid1, "and", uid2)
common=net.getCommonFriends(uid1,uid2)
for item in common:
    print(item, end=" ")



    
