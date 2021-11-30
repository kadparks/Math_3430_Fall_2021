"""
This assignment is due by 11:59pm on 11/19/2021. 

For this assignment you will be writing a python script named LS.py which will
contain several functions. All functions must satisfy the same requirements as in HW03. 

You will import the LA.py and QR.py scripts from the previous homeworks. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.

The functions you will need to write are

1) Write a function which takes as it's argument a vector stored as a list, and
a matrix, and returns the least squares solution, calculated by using QR
factorization.
"""
import LA
import QR

def backsub(matrix: list, vector: list):
    """
    Produces the back substitution of our input matrix and vector.
    
    First we will initialze result as our first solution in backsubstitution. Then we will 
    use an outer for loop to iterate from the second to last column to the first column. In this for
    loop we will aslo set a variable named temp to be the current indexed element in our input vector.
    Then in an inner for loop, we will subtract all previous solutions scaled by their coefficients in the 
    corresponding equation from temp. Then back in the outer for loop, we will divide temp by the coefficient
    of the variable we are solving for from the corresponding equation, then append the new temp to result.
    Finally we reverse the order of solutions to obtain the desired solution.
     
    Arguements:
        matrix: A matrix stored as a list of columns.
        vector: A vector stored as a list.
            
    Returns:
        The backsubstitution of our input matrix and vector.
    """
    
    result: list = [vector[-1] * (1/(matrix[-1][-1]))]
    for current in range(len(matrix) - 2, -1, -1):
        temp: float = vector[current]
        for index in range(len(result)):
            temp -= matrix[len(matrix) - 1 - index][current]*result[index]
        temp *= 1/(matrix[current][current])
        result.append(temp)
    result = result[::-1]
    return result

#Problem 1
def least_squares(matrix: list, vector: list):
    """
    Finds the Least Squares of our input matrix and vector
    
    First we initialize QandR to the Stable Gram-Schmidt decomposition of our input matrix. Then we set Q equal to
    the first index of QandR, and set R equal to the last index of QandR. Then we create a variable
    Q_1 that is equal to the conjugate transpose of Q. Then we will create another variable Q_2 that will be the 
    product of matrix vector multiplaction using the matrix Q_1 and our input vector. Then we will set result 
    equal to the backsubstitution of the matrix R and the vector Q_2.
    
    Arguements:
        matrix: A matrix stored as a list of columns.
        vector: A vector stored as a list.
    
    Returns:
        The least squares solution of our input matrix and vector.
    """
    
    QandR = QR.stable_gram(matrix)
    Q = QandR[0]
    R = QandR[-1]
    Q_1 = QR.conjugate_transpose(Q)
    Q_2 = LA.matrix_vector_multi(Q_1, vector)
    result = backsub(R, Q_2)
    return result

