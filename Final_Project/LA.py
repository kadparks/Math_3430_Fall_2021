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
def new_matrix(cols: list, rows: list):
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
def vector_addition(vector_1: list, vector_2: list):
    result: list[float] = []
    for element in vector_1:
        result.append(0)
        
    for i in range(len(result)):
        result[i] = vector_1[i] + vector_2[i]
    return result

#Problem #1

def scalar_vector_multi(vector: list, scalar: float):
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

def scalar_matrix_multi(matrix: list , scalar: float):
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
    cols: list = len(matrix)
    rows: list = len(matrix[-1])
    result: list[list] = new_matrix(cols, rows)
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

def matrix_addition(matrix_1: list, matrix_2: list):
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
    cols_m1: list = len(matrix_1)
    rows_m2: list = len(matrix_2[-1])
    result: list[list] = new_matrix(cols_m1, rows_m2)
    
    for i in range(cols_m1):
        result[i] = vector_addition(matrix_1[i], matrix_2[i])
    return result

#Problem #4

def matrix_vector_multi(matrix: list,vector: list):
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
    cols: list = len(matrix)
    rows: list = len(matrix[-1])
    result: list[float] = []
    for element in range(rows):
        result.append(0)
    
    for i in range(cols):
        result = vector_addition(result, scalar_vector_multi(matrix[i], vector[i]))
    return result

#Problem 5
    
def matrix_matrix_multi(matrix_1: list, matrix_2: list):
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
    
    rows_m1: list = len(matrix_1[-1])
    cols_m2: list = len(matrix_2)
    result: list[list] = new_matrix(cols_m2, rows_m1)
    
    for i in range(cols_m2):
        result[i] = matrix_vector_multi(matrix_1, matrix_2[i])
    return result

#HW4

#Problem 1

def absolute_value(integer:int, integer_1:complex):
    """
    Produces the absolute value of our input integer.
    
    Multiplies our input integer by it's conjugate then raises the result to 1/2 power,
    or takes the square root.
    
    Arguements:
        integer: a normal or complex input number.
        
    Returns:
        The absolute value of our input integer.
    """
    
    z: int[complex] = integer + integer_1
    result = (z*z.conjugate())
    return result**(1/2)

#Problem 2
def p_norm(vector: list, scalar:float = 2):
    """
    Produces the p-norm of our input vector scaled by our input scalar.
    
    Initializes result as an empty list then adds a 0 for every element in our input vector.
    Takes the absolute value of each element in vector and raises it to the power of our input
    scalar. Then takes the sum of the elements in our new vector then raises this sum to the power of
    1 over our input scalar.
    
    Arguements:
        vector: A vector stored as a list.
        scalar: An integer, set to default to 2 if input left blank.
        
    Returns:
        The p-norm of our inputs.
    """
    
    result: list[float] = []
    for element in vector:
        result.append(0)
    
    for i in range(len(vector)):
        result[i] = absolute_value(vector[i], 0)**(scalar)
    result = sum(result)**(1/scalar)
    return result

#Problem 3
def inf_norm(vector: list):
    """
    Produces the infinity norm of our input vector.
    
    Takes the adsolute value of the largest element in our input vector.
    
    Arguements:
        vector: A vector stored as a list.
        
    Returns:
        The infinity norm of our input vector.
    """

    result: int = absolute_value(max(vector),0)
    return result

#Problem 4
def boolean_norm(vector: list, scalar:float = 2, boolean = False):
    """
    Produces the infinity norm of our input vector if the boolean is True, or produces the p-norm
    of our input vector if the boolean is False.
    
    Arguements:
        vector: A vector stored as a list.
        scalar: A float value, defaulted to value 2 if input is left blank.
        boolean: A boolean value, defaulted to False if input is left blank.
        
    Returns:
        The infinity or p-norm of our input vector and scalar, contingent on a boolean value.
    """
    
    if boolean == True:
        inf_norm(vector)
        return inf_norm(vector)
    else: 
        p_norm(vector, scalar)
        return p_norm(vector, scalar)

#Problem 5
def inner_product(vector_1: list, vector_2: list):
    """
    Produces the inner product of our two input vectors.
    
    Initializes result as an empty list then appends 0 for each element in vector_1. Then we will 
    multiply the elements with corresponding indexes in vectors 1 and 2, then overwrite the new element
    into the corresponding index in our result vector. Then we will take the sum of our result vector.
    
    Arguements:
      vector_1: A vector stored as a list.
      vector_2: A vector stored as a list, the same length as vector_1.
      
     Returns:
         The inner product of our input vectors.
    """
    result: list[float] = []
    for element in vector_1:
        result.append(0)
        
    for i in range(len(vector_1)):
        result[i] = vector_1[i]*vector_2[i]
    result = sum(result)
    return result