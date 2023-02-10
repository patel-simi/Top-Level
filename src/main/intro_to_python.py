import numpy as np
#this first is needed to create the matrix
from numpy import*
#this is needed to delete a column in the matrix

matrix= np.zeros((3,3))
#1
num_of_points=len(matrix)
for i in range(0,num_of_points):
    for j in range(0,i+1):
        if i==j:
            #the 0s in the range includes the first value
            matrix[i,j]=1 
        #elif i!=j :
            #matrix[j,i]=3
            #matrix[i,j]=3     
print(matrix)

#2
for i in range(0,num_of_points):
    for j in range(0,i+1):
        if i!=j:
            matrix[i,j]= matrix[j,i]=3
print(matrix)

#3 
matrix=np.delete(matrix,2,1)
#this function deletes an array from the matrix
# the 2 represents the 3rd array in the column 
#(the last value determines if youre removing a column or a row)
#^0=for a row and 1= for a column
print(matrix)
