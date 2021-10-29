"""
This homework is due on 10/15/2021 by 11:59pm. 


For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

Once you have finished writing LA.py you will upload it to the same github repo
you used for HW02. The functions you need to write are 

#0 A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.


#1 A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.


#2 A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.

#3 A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.

#4 A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.

#5 A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""
#To create a new matrix with zeros
def new_matrix(cols, rows):
    matrix: list[float] = []
    while len(matrix) < cols:
        matrix.append([])
        while len(matrix[-1]) < rows:
            matrix[-1].append(0)
    return matrix

"""
# Begin Example
# Problem #0

def add_vectors(vector_a: list[float],
                vector_b: list[float]) -> list[float]:
    Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
     
    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result

# End Example
# Note that you must add unit tests for problem 0!!!!!
"""

#Own add function
def vector_addition(vector_1, vector_2):
    result: list[float] = []
    for element in vector_1:
        result.append(0)
        
    for i in range(len(result)):
        result[i] = vector_1[i] + vector_2[i]
    return result

#Problem #1

def scalar_vector_multi(vector, scalar):
    """
    Produces the product of a scalar and a vector.
    
    Creates a result vector stored as a list of zeros the same length as the input
    then overwrites each element of the result vector with the corresponding element
    of the product of our input vector and the scalar. Does this process using a 
    for loop over the indices of result.
    
    Args:
        vector: A vector stored as a list
        scalar: A number belonging to the set of natural #'s N
        
    Returns:
        The input vector scaled appropriately by the scalar, stored as a list.
    """
        
    result: list[float] = []
    for element in vector:
        result.append(0)
        
    for i in range(len(vector)):
        result[i] = vector[i] * scalar
    return result

#Problem #2

def scalar_matrix_multi(matrix , scalar):
    """
    Produces the product of a matrix and a scalar.
    
    Creates a new matrix of same dimensions of our input matrix, stored as a 
    list of columns with zeros added for each element then overwrites each element 
    with the corresponding element of the product of our input matrix and scalar.
    Does this using a for loop over the indices of result, utilizing our previous
    function scalar_vector_multi(vector, scalar).
    
    Args:
        matrix: A matrix stored as a list of columns
        scalar: A number belonging to the set of natural #'s N
        
    Returns:
        The input matrix scaled appropriately by the scalar, stored as a list of columns.
    """
    cols = len(matrix)
    rows = len(matrix[-1])
    result = new_matrix(cols, rows)
    """
    for i in range(cols):
        for j in range(rows):
            result[i][j] = matrix[i][j]*scalar
    return result
    """
    for i in range(cols):
        result[i] = scalar_vector_multi(matrix[i], scalar)
    return result

#Problem #3

def matrix_addition(matrix_1, matrix_2):
    """
    Produces the sum of two matrices.
    
     Creates a new matrix of same dimensions of our input matrix, stored as a 
    list of columns with zeros added for each element then overwrites each element 
    with the corresponding element of the sum of our input matrices. Does this process 
    using a for loop over the indices of result, utilizing our previous function
    vector_addition(vector_1, vector_2).
    
    Args:
        matrix_1: A n x m matrix, stored as a list of column vectors.
        matrix_2: A n x m matrix, where matrix_2(n,m) = matrix_1(n,m), also stored
        as a list of columns.
        
    Returns:
        The sum of our input matrices, stored as a list of column vectors.
    """
    cols_m1 = len(matrix_1)
    rows_m1 = len(matrix_1[-1])
    cols_m2 = len(matrix_2)
    rows_m2 = len(matrix_2[-1])
    result = new_matrix(cols_m1, rows_m2)
    """
    for i in range(cols_m1):
        for j in range(rows_m2):
            result[i][j] = matrix_1[i][j] + matrix_2[i][j]
    return result
    """
    for i in range(cols_m1):
        result[i] = vector_addition(matrix_1[i], matrix_2[i])
    return result

#Problem #4

def matrix_vector_multi(matrix,vector):
    """
    Produces the product of a matrix and a vector.
    
    Creates a new column vector of length n x 1, where n is the # of rows of our input
    matrix, with zeros added for each element n then takes the linear combination product
    of our input matrix and vector then overwrites each corresponding element into 
    the result. Achieves this by using a for loop over the indices of result, utilizing 
    two previous functions vector_addition(vector_1, vector_2) and scalar_vector_multi(
    vector, scalar).
    
    Args:
        matrix: A n x m matrix, stored as a list of columns.
        vector: A vector stored as a list, with length n.
        
    Returns:
        The linear combination of our input matrix and vector, 
        stored as a list
    """
    cols = len(matrix)
    rows = len(matrix[-1])
    vec_sca = len(vector)
    result: list[float] = []
    for element in range(rows):
        result.append(0)
    
    for i in range(cols):
        result = vector_addition(result, scalar_vector_multi(matrix[i], vector[i]))
    return result

#Problem 5
    
def matrix_matrix_multi(matrix_1, matrix_2):
    """
    Produces the product of two matrices.
    
    *This function operates under the assumption that matrix_1 and matrix_2 are
    compatible for matrix multiplication. That is, the # of columns in the left most
    matrix is equal to the # of rows in the right most matrix.*
    
    Creates a new matrix of size n x m, where n is the # of rows of the left most
    matrix and m is the # of columns in the right most matrix, stored as a 
    list of columns with zeros added for each element then overwrites each element 
    with the corresponding element of the product of our input matrices. Achieves this by
    by using a for loop over the indices of result, and calling our previous function
    matrix_vector_multi(matrix,vector).
    
    Args:
        matrix_1: The left most matrix, stored as a list of columns, of size n x m
        matrix_2: The right most matrix, stored as a  list of columns, of size m x h
        
    Returns:
        The product of our matrices, stored as a list of columns.
    """
    
    cols_m1 = len(matrix_1)
    rows_m1 = len(matrix_1[-1])
    cols_m2 = len(matrix_2)
    rows_m2 = len(matrix_2[-1])
    result = new_matrix(cols_m2, rows_m1)
    
    for i in range(cols_m2):
        result[i] = matrix_vector_multi(matrix_1, matrix_2[i])
    return result

