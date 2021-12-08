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
    V :list[list] = matrix
    Q :list = []
    R :list[list] = LA.new_matrix(len(matrix),len(matrix))
    
    for i in range(len(matrix)):
        R[i][i] = LA.p_norm(V[i], )
        Q.append(LA.scalar_vector_multi(V[i], (1/R[i][i])))
        for j in range(i, len(matrix)):
            R[j][i] = LA.inner_product(Q[i], V[j])
            V[j] = LA.vector_addition(V[j], LA.scalar_vector_multi(Q[i], -R[j][i]))
    return Q,R

#HW 6

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

#HW 7
#Problem 1

def conjugate_transpose(matrix: list):
    """
    Produces the conjugate transpose of our input matrix.
    
    First we create a new matrix of 0's with nxm dimensions. Then we use a double for loop to
    call the correct column and row index, then we conjugate the value and overwrite it's proper
    position in the result matrix.
    
    Arguements:
        matrix: A matrix stored as a list of columns.
    
    Returns:
        Conjugate Transpose of our input matrix.
    """
    
    result: list[list[float]] = LA.new_matrix(len(matrix[-1]), len(matrix))
    C: complex = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[-1])):
            C = matrix[i][j]
            C = C.real + (C.imag*-1j)
            result[j][i] = C
    return result




def matrix_identity(n: int):
    """
    Produces an indentity matrix with dimensions nxn.
    
    Arguements: 
        n: An integer n.
    
    Returns:
        An identity matrix with dimensions nxn.
    """
    
    result: list[list[float]] = LA.new_matrix(n, n)
    for i in range((n)):
        result[i][i] = 1
    return result




def sign(number: float):
    """
    Returns the polarity of a number. If number is postive, returns 1. If number is negative,
    returns -1.
    
    Arguements:
        number: Any number.
        
    Returns:
        The polarity of our input number.
    """
    
    if number < 0:
        return -1
    else:
        return 1




def vector_vector_multi(vector_1:list, vector_2:list):
    """
    Produces (vv*/v*v)*2. First we set result equal to an empty list. Then we use a for loop to find 
    the scalar vector multiplication of our second input vector with each element of our first input
    vector, then appends new value into result.
    
    Arguements:
        vector_1: A vector, stored as a list.
        vector_2: A vector, stored as a list.
    
    Returns:
        The product of our input vectors.   
    """
    
    result: list = []
    for i in range(len(vector_1)):
        result.append(LA.scalar_vector_multi(vector_2, vector_1[i]))
    return result




def HH_V(vector:list):
    """
    Produces the reflection of our input vector, which will be used in our process to find Householder
    decompositions.
    
    Arguements:
        vector: A vector, stored as a list.
        
    Returns:
        The reflection of our input vector.
    """
    
    v: list[float] = []
    for i in vector:
      v.append(0)
    v[0] = 1
    result = LA.vector_addition(vector, LA.scalar_vector_multi(v, sign(vector[0])*LA.p_norm(vector)))
    return result




def HH_F(vector: list):
    """
    Calculates the F_k matrix used in Householder.
    
    First we find a scalar a that will be equal to -2 over the p_norm of our input vector squared. Second
    we find a matrix b that is the product of scalar matrix multiplication with the inputs of the product of our
    input vector times itself, and our scalar a. Third we find the sum of our matrix b and an identity matrix with
    dimensions kxk, where k equals the length of our input vector.
    
    Arguements:
        vector: A vector stored as a list.
    
    Returns:
        F_k
    """
    
    a = -2/(LA.p_norm(vector))**2
    b = LA.scalar_matrix_multi(vector_vector_multi(vector, vector), a)
    result: list[list] = LA.matrix_addition(matrix_identity(len(vector)), b)
    return result




def HH_Q(matrix: list, k: int):
    """
    Calcualtes the Q_k matrix used in Householder.
    
    First we create new matrix of 0's, with the dimensions of our input matrix. Second we use for loops
    to overwrite Q with the sum of our input scalar and matrix index in the approriate index, iff the sum is
    less then the length of our matrix index. Third we set a variable v equal to the reflection of the first column
    vector of Q, and a variable f equal to the F_k of our variable v. Fourth we set this function equal to an identity
    matrix with the dimensions of the # of cols of our input matrix. Fifth we use for loops to overwrite our appropriate
    indexes in HH_Q with difference between our indexes and our input scalar.
    
    Arguements:
        matrix: A matrix, stored as a list of columns.
        k:      An integer scalar
    Returns:
        Q_k
    """
    
    Q_k: list[list] = LA.new_matrix(len(matrix), len(matrix[-1]))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if k+i < len(matrix[i]):
                if k+j < len(matrix[i]):
                    Q_k[i][j] = matrix[k+i][k+j]
    v: list = HH_V(Q_k[0])
    f: list[list] = HH_F(v)
    HH_Q: list[list] = matrix_identity(len(matrix))
    for i in range(k, len(HH_Q)):
        for j in range(k, len(HH_Q)):
            HH_Q[i][j] = f[i-k][j-k]
    return HH_Q




def HH(matrix: list):
    """
    Produces Householder QR decomposition
    
    First we set R equal to our input matrix and a variable Q_list equal to an empty list. Second we use a for
    loop in the range of R to set Q_temp equal to the HH_Q of R and our index, set R equal to the matrix matrix 
    multiplication of Q_temp and R, then finally append Q_temp into Q_list. Third we will set Q equal to the last
    index in Q_list, then take the conjugate transpose of the first index of our new Q. Fourth we use another for 
    loop in the range of 1 through the length of our Q_list to overwrite Q with the matrix matrix multiplication
    of Q and the conjugate transpose of our appropriate Q_list index.
   
    Arguements:
       matrix: A matrix, stored as a list of columns.
    
    Returns:
        Two matrices, Q and R, in Householder QR decomposition.
    """
    
    R: list[list] = matrix
    Q_list: list = []
    for i in range(len(R)):
        Q_temp: list[list] = HH_Q(R, i)
        R = LA.matrix_matrix_multi(Q_temp, R)
        Q_list.append(Q_temp)
    Q: list = Q_list[-1]
    Q: list = conjugate_transpose(Q_list[0])
    for i in range(1, len(Q_list)):
        Q = LA.matrix_matrix_multi(Q, conjugate_transpose(Q_list[i]))
    return [Q, R]