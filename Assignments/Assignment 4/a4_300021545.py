import random
import timeit

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    # YOUR CODE GOES HERE
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
        network.append(tuple([f1[i],f3[i]]))

    return network

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
    # YOUR CODE GOES HERE
    list1=[]
    list2=[]
    tot=[]
    for x in range(len(network)):
        if network[x][0]==user1:
            list1.append((network[x][1]))
        if network[x][0]==user2:
            list2.append((network[x][1]))
                    
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

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE
    count=[]
    lis=[]
    rec=None

    for j in range(len(network)):
        if user not in network[j][1] and user!=network[j][0]:
            lis.append(network[j][0])

    for i in range(len(lis)):
        a=getCommonFriends(user, lis[i], network)
        if len(count)<len(a):
            count=[]
            for item in a:
                count.append(item)
            rec=lis[i]
            
    return rec

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE
    count=0
    for i in range(len(network)):
        if len(network[i][1])>=k:
            count+=1
    return count

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    # YOUR CODE GOES HERE
    maxf=0
    for i in range(len(network)):
        if len(network[i][1])>maxf:
            maxf=len(network[i][1])
    return maxf 
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE
    maxf = maximum_num_friends(network)
    for i in range(len(network)):
        if len(network[i][1])==maxf:
            max_friends.append(network[i][0])
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE
    average=0
    for i in range(len(network)):
        average+=len(network[i][1])
    average=average/len(network)
    return average
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE
    for i in range(len(network)):
        if len(network[i][1])==len(network)-1:
            return True
    return False
    


####### CHATTING WITH USER CODE:

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
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE
    flag=False

    while flag!=True:
        user = (input("Enter a user ID: "))
        try:
           user = int(user)
        except ValueError:
            print("That was not an integer. Please try again.")
            flag=False
        else:
            for i in range(len(network)):
                if int(user) == network[i][0]:
                    flag=True
            if flag==False:
                print("That user ID does not exist. Try again.")
        
    return user

##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()

start = timeit.default_timer()   
net=create_network(file_name)
stop = timeit.default_timer()
print(stop-start)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")
