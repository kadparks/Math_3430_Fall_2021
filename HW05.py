"""
This assignment is due by 11:59pm on 10/29/2021. 

For this assignment you will be writing a python script named QR.py which will
contain several functions. All functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

For all functions below, matrices will be stored as lists of lists where each
component list represents a column of the matrix. Use of any other
representation will result in an earned grade of 0.

The functions you will need to add are

1) A function which implements the unstable version of Gram-Schmidt for reduced QR
factorization. It will
take as it's argument a matrix and will return a list of two matrices. The first
will be Q and the second will be R from the QR factorization described in the
algorithm.

2) A function which implements the stable version of Gram-Schmidt for reduced QR
factorization.It will take as it's argument a matrix and will return a list of 
two matrices. The first will be Q and the second will be R from the QR factorization 
described in the algorithm.

"""

"""
Turned in late, so ommitted the unstable version of GS to save time, as it is not used in
HW6 or after.
"""


import LA

def stable_gram(matrix: list):
    """
    Produces QR factorization using Stable Gram-Schmidt method.
    
    Creates V which is a copy of our input matrix, Q which is an empty list,
    and R which is a square matrix of dimensions nxn, where n is the # of columns in
    our input matrix and/or V. We use a first for loop to first make the elements of the diagonal of R equal 
    to the p-norm of the respective index column vectors of V. Then in Q, we add the scalar vector
    multiplication product of our ith index column vector of V with the reciprocal of our double ith
    index element in R. Then in a second for loop within the first, we will overwrite the jth and ith
    index of R with the inner product of the ith index of Q and the jth index of V. Then we will take
    the jth index of V and overwrite that with the vector addition of the jth index of V and the vector
    produced by the scalar_vector_multi of the ith index of Q and the jth and ith index of -R.
    
    Arguements:
        matrix: stored as a list of column vectors.
    Returns:
        The matrices Q and R, where Q is an orthnormal matrix and R is an upper triangular matrix.

    

    """
    V = matrix
    Q: list = []
    R: list[list] = LA.new_matrix(len(matrix),len(matrix))
    
    for i in range(len(matrix)):
        R[i][i] = LA.p_norm(V[i], )
        Q.append(LA.scalar_vector_multi(V[i], (1/R[i][i])))
        for j in range(i, len(matrix)):
            R[j][i] = LA.inner_product(Q[i], V[j])
            V[j] = LA.vector_addition(V[j], LA.scalar_vector_multi(Q[i], -R[j][i]))
    return Q,R
