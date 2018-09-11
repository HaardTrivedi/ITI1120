def is_square(m):
     '''2d-list => bool
     Return True if m is a square matrix, otherwise return False
     Matrix is square if it has the same number of rows and columns'''
     for i in range(len(m)):
          if len(m[i]) != len(m):
               return False
     return True


def magic(m):
     '''2D list->bool
     Returns True if m forms a magic square
     Precondition: m is a matrix with at least 2 rows and 2 columns '''
     if(not(is_square(m))):
          return False      

     # YOUR CODE GOES HERE
     length = len(m)
     test = 0
     
     for i in range (length):
          test = test + m[i][i]
     li = []
     
     # TEST CONDITION 1
     for i in range (length):
          for j in range (length):
               li.append(m[i][j])
     for i in range (len(li)):
          if li.count (li[i]) > 1:
               return False
     
     # TEST CONDITION 2
     for i in range (length):
          Row = 0
          Column = 0
          for j in range (length):
               Row += m[j][i]
               Column += m[i][j]
          if test != Row or test != Column:
               return False
     return True
# main
# TESTING OF magic functions

# True

m0=[[2,7, 6],[9,5,1],[4,3,8]]
print(magic(m0))
    
#True
m1 = [[16,3,2,13], [5,10,11,8],[9,6,7,12], [4,15,14,1]]
print(magic(m1))
    
# this should print False. Why? Which condition imposed on magic squares is not true for m2
#
m2 = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print(magic(m2))
    
#this should print False. Why? Which condition imposed on magic squares is not true for m3
m3 =  [[1,1],[1,1]]
print(magic(m3))

#this should print False. Why? Which condition imposed on magic squares is not
#num of rows != num of columns
m3 =  [[1,1],[1,1],[1,2]]
print(magic(m3))
