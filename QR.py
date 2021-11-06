"""
This assignment is due by 11:59pm on 11/05/2021. 

For this assignment you will be updating the python script QR.py from the
previous homework. As usual, all functions must satisfy the same requirements as in HW03. 

You will import the LA.py script from HW03 and HW04. You must make use of those
functions to implement the functions below. Failure to do this will result in an
earned grade of 0.

1) Remove the function which implemented unstable Gram-Schmidt. It is unstable
and we may use the stable version exclusively from this point forward. 

2) Write a function which takes as it's argument a list of vectors and returns
an orthonormal list of vectors which shares the same span. 
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
    Q :list = []
    R :list[list] = LA.new_matrix(len(matrix),len(matrix))
    
    for i in range(len(matrix)):
        R[i][i] = LA.p_norm(V[i], )
        Q.append(LA.scalar_vector_multi(V[i], (1/R[i][i])))
        for j in range(i, len(matrix)):
            R[j][i] = LA.inner_product(Q[i], V[j])
            V[j] = LA.vector_addition(V[j], LA.scalar_vector_multi(Q[i], -R[j][i]))
    return Q,R

def orthonormal_vectors(vectors: list):
    """ 
    Orthonormalize a list of vectors.
    
    Takes a list of vectors then uses the Stable Gram-Schmidt method of QR factorization
    to produce an orthonormal list of vectors Q.
    
    Arguements:
        vectors: list of multiple vectors, or a matrix as list of column vectors.
        
    Returns:
        Orthonormalized list of vectors Q, of our inout list of vectors.
    """
    
    result: list[list] = stable_gram(vectors)[0]
    return result
