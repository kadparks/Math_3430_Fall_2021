 """
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 

For Problems #0-5 from HW01, Do the following.



1) Write your answer from HW01 in a comment.

2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 

3) Test each of your functions on at least 2 inputs. 

4) Upload your .py file to a github repo named "Math_3430_Fall_2021"

This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions

Q1: What do we have?

A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 

Q2: What do we want?

A2: Their sum stored as a list.

Q3: How will we get there?

A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 

-PsuedoCode

def add_vectors(vector_a,vector_b):

Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.

# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]

Return the desired result.
"""
#Accidently wrote my own code for vector addition, unaware was provided
#Took WAAYY more time than it should have unfortunately
def vector_addition(vector_1, vector_2):
    result = []
    for element in vector_1:
        result.append(0)
        
    for i in range(len(result)):
        result[i] = vector_1[i] + vector_2[i]
    return result

#End Example

#To create a new matrix with zeros
def new_matrix(cols, rows):
    matrix = []
    while len(matrix) < cols:
        matrix.append([])
        while len(matrix[-1]) < rows:
            matrix[-1].append(0)
    return matrix

#Problem 01
"""
Write an algorithm to implement scalar-vector multiplication.
Q1. What do we have?
	We have a scalar and a vector stored as a list in a computer.
Q2. What do we want?
	Our given vector scaled by the scalar value.
Q3. How do we get there?
	We are going to take each element of our vector, scale it by the scalar, 
    then store the new element in it's corresponding place in a new vector.

def scalar_vector_multi(vector, scalar):
#Initialize result as an empty list
result = []

#Then add a 0 for every element in our vector.
for element in vector:
	result.append(0)

#Set each element of result to corresponding scaled element.
for i in range(vector)
	result[index] = vector[index] * scalar
return result
"""

def scalar_vector_multi(vector, scalar):
    result = []
    for element in vector:
        result.append(0)
        
    for i in range(len(vector)):
        result[i] = vector[i] * scalar
    return result

#Problem 02
"""
Write an algorithm to implement scalar-matrix multiplication.
Q1. What do we have?
	A scalar and a matrix stored as a list of columns in a computer.
Q2. What do we want?
	Our matrix scaled by the scalar.
Q3. How do we get there?
	We will create a new matrix with proper dimensions then add 0 for each in element of our given mattrix. 
    Then we will scale each element of our matrix and plug
	each scaled element in to the corresponding place in our new matrix.

def scalar_matrix_multi(matrix, scalar):

#initialze result as empty list and 0 for every column of matrix
result = []
for i in matrix:
	result.append(0)

#Scale each element of matrix by scalar, then plug into new result matrix.
for element in range(columns)
	for element in range(rows)
		result[index] = matrix[index]*scalar
return result
"""

def scalar_matrix_multi(matrix, scalar):
    cols = len(matrix)
    rows = len(matrix[-1])
    result = new_matrix(cols, rows)
    
    for i in range(cols):
        for j in range(rows):
            result[i][j] = matrix[i][j]*scalar
    return result

#Problem 03
"""
Write an algorithm to implement matrix addition.
Q1. What do we have?
	Two matrices with same dimensions, both stored as a list of columns, in a computer
Q2. What do we want?
	The sum of both matrices
Q3. How do we get there?
	We will create a new list with 0's for each element of one of our matrices. Then we will add the element from our first matrix with the element from our second
	matrix with the corresponding index. Then we will take that new element and store it our new matrix in the corresponding index.

def matrix_addition(matrix_1, matrix_2):

#initialze result as empty list and 0 for every column of matrix
result = []
for i in matrix:
	result.append(0)

#Add each element of matrix 1 with corresponding element in matrix 2, then store in corresponding index in new matrix.
for element in range(columns)
	for element in range(rows)
		result[index] = matrix_1[index] + matrix_2[index]
return result
"""

def matrix_addition(matrix_1, matrix_2):
    cols_m1 = len(matrix_1)
    rows_m1 = len(matrix_1[-1])
    cols_m2 = len(matrix_2)
    rows_m2 = len(matrix_2[-1])
    result = new_matrix(cols_m1, rows_m2)
    
    for i in range(cols_m1):
        for j in range(rows_m2):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]
    return result

#Problem 04
"""
Write an algorithm to implement matrix-vector multiplication using the linear
combination of columns method. You must use the algorithms from Problem #0 and
Problem #1.  

Q1. What do we have?
	A matrix stored as a list of columns and a vector in a computer.
Q2. What do we want?
	The product of our matrix and vector, which will return a new vector.
Q3. How do we get there?
	We will create a new list with 0's for every element of our vector. The we will multiply the nth column in our matrix by the nth element in our vector, then
	add each of those new vectors to get our result.

def matrix_vector_multi(matrix, vector):
#initialze result as empty list and 0 for every column of matrix
result = []
for i in matrix:
	result.append(0)

#Multiply each nth column in matrix by each nth element in vector, then add those new vectors.
for element in range(cols):
	matrix[index] = scalar_vector_multi(matrix[index], vector[index])
for element in range(cols)
	result = vector_addition(result, matrix[index])
return result
"""

def matrix_vector_multi(matrix,vector):
    cols = len(matrix)
    rows = len(matrix[-1])
    vec_sca = len(vector)
    result = []
    for element in range(rows):
        result.append(0)
    
    for i in range(cols):
        matrix[i] = scalar_vector_multi(matrix[i], vector[i])
    for j in range(cols):
        result = vector_addition(result, matrix[j])
    return result

#Problem 05
"""
Write an algorithm to implement matrix-matrix multiplication using your
algorithm from Problem #4.  

Q1. What do we have?
	Two matrices both stored as a list of columns in a computer, where the # of columns of our left most matrix is equivalent to the # of rows of our right most matrix.
Q2. What do we want?
	The product of our two matrices, with dimensions x # of rows from our left most matrix by y # of columns from our right most matrix.
Q3. How do we get there?
	We will create a new matrix with proper dimensions for our product, then add a zero for each element. Then we will take the matrix_vector_multi of our left most matrix
	multiplied by the first column of our right most matrix, then take that new vector and copy it into its correspong column in our new matrix. We will repeat this process
	for every column in our right most matrix.

def matrix_matrix_multi(matrix_1, matrix_2):
#initialze result as empty list and 0 for every column of matrix
result = []
for i in matrix:
	result.append(0)

#Multipy our left most matrix by the nth column of our second matrix, then copying into our new matrix.
	for element in range(cols_matrix_2)
		result[index] = matrix_vector_multi(matrix_1, matrix_2[index])
	return result
"""

def matrix_matrix_multi(matrix_1, matrix_2):
    cols_m1 = len(matrix_1)
    rows_m1 = len(matrix_1[-1])
    cols_m2 = len(matrix_2)
    rows_m2 = len(matrix_2[-1])
    result = new_matrix(cols_m2, rows_m1)
    
    for i in range(cols_m2):
        result[i] = matrix_vector_multi(matrix_1, matrix_2[i])
        print(result)
    return result


#Test Inputs

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]
test_vector_03 = [4, 2, 1]
test_vector_04 = [5, 3, 2]

test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]]
test_matrix_02 = [[1,3,2],[3,5,3],[2,7,4]]
test_matrix_03 = [[1,4],[2,5],[3,6]]
test_matrix_04 = [[7,9,11],[8,10,12]]
test_matrix_05 = [[2,3],[1,2],[7,4]]

test_scalar_01 = 2
test_scalar_02 = 3

# vector_addition(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output for vector_addition: ' + str(vector_addition(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')
print('')
print('')
#scalar_vector_multi(test_vector_01, test_scalar_01) should output [2,4,8]
print('Test Output for scalar_vector_multi: ' + str(scalar_vector_multi(test_vector_01, test_scalar_01)))
print('Should have been [2,4,8]')
#scalar_vector_multi(test_vector_02, test_scalar_02) should output [9,3,6]
print('Test Output for scalar_vector_multi: ' + str(scalar_vector_multi(test_vector_02, test_scalar_02)))
print('Should have been [9,3,6]')
print('')
print('')
#scalar_matrix_multi(test_matrix_01, test_scalar_01) should output [[2,8,14],[4,10,16],[6,12,18]]
print('Test Output for scalar_matrix_multi: ' + str(scalar_matrix_multi(test_matrix_01, test_scalar_01)))
print('Should have been [[2,8,14],[4,10,16],[6,12,18]]')
#scalar_matrix_multi(test_matrix_03, test_scalar_02) should outout [[3,12],[6,15],[9,18]]
print('Test Output for scalar_matrix_multi: ' + str(scalar_matrix_multi(test_matrix_03, test_scalar_02)))
print('Should have been [[3,12],[6,15],[9,18]]')
print('')
print('')
#matrix_addition(test_matrix_01, test_matrix_02) should output [[2,7,9],[5,10,11],[5,13,13]]
print('Test Output for matrix_addition: ' + str(matrix_addition(test_matrix_01, test_matrix_02)))
print('Should have been [[2,7,9],[5,10,11],[5,13,13]]')
#matrix_addition(test_matrix_03, test_matrix_05) should output [[3,7],[3,7],[10,10]]
print('Test Output for matrix_addition: ' + str(matrix_addition(test_matrix_03, test_matrix_05)))
print('Should have been [[3,7],[3,7],[10,10]]')
print('')
print('')
#matrix_vector_multi(test_matrix_01,test_vector_01) should output [17, 38, 59]
print('Test Output for matrix_vector_multi: ' + str(matrix_vector_multi(test_matrix_01,test_vector_01)))
print('Should have been [17, 38, 59]')
#matrix_vector_multi(test_matrix_03,test_vector_02) should output [11, 29]
print('Test Output for matrix_vector_multi: ' + str(matrix_vector_multi(test_matrix_03,test_vector_02)))
print('Should have been [11, 29]')
print('')
print('')
#matrix_matrix_multi(test_matrix_01, test_matrix_02) should output [[13,31,49],[22,55,88],[28,67,106]]
print('Test Output for matrix_matrix_multi: ' + str(matrix_matrix_multi(test_matrix_01, test_matrix_02)))
print('Should have been [[13,31,49],[22,55,88],[28,67,106]]')
#matrix_matrix_multi(test_matrix_03, test_matrix_04) should output [[58, 139],[64, 154]]
print('Test Output for matrix_matrix_multi: ' + str(matrix_matrix_multi(test_matrix_03, test_matrix_04)))
print('Should have been [[58, 139],[64, 154]]')