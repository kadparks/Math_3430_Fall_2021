# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:45:10 2021

@author: Kadeem
"""
import LA
import QR
import LS

test_vector_01: list = [1, 2, 4]
test_vector_02: list = [3, 1, 2]
test_vector_03: list = [4, 2, 1]
test_vector_04: list = [5, 3, 2]
test_matrix_01: list[list] = [[1,4,7],[2,5,8],[3,6,9]]
test_matrix_02: list[list] = [[1,3,2],[3,5,3],[2,7,4]]
test_matrix_03: list[list] = [[1,4],[2,5],[3,6]]
test_matrix_04: list[list] = [[7,9,11],[8,10,12]]
test_matrix_05: list[list] = [[2,3],[1,2],[7,4]]
test_matrix_06: list[list] = [[2,4],[6,9]]
test_matrix_07: list[list] = [[1,5],[3,7]]
test_scalar_01: int = 2
test_scalar_02: int = 3

print('My name is Kadeem and I am a senior at Texas Tech University who is steadily learning how to code. I have created a library consisting of three files, LA.py, QR.py and LS.py. These programs do basic to more complex linear algebra processes')
print('')
print('LA.py contains a large number of functions for performing basic linear algebra tasks.')
print('')
print('The Ith function in LA.py is new_matrix. It will take in two integers n and m as its inputs and return a matrix of zeros with dimensions mxn.')
print('For example, if test_scalar_01 = 2 and test_scalar_02 = 3, then new_matrix(test_scalar_01, test_scalar_02) will return')
print(LA.new_matrix(test_scalar_01, test_scalar_02))
print('')
print('The first function in LA.py is vector_addition. It will take in two vectors as its inputs and return their sum.')
print('For example, if test_vector_01 = [1, 2, 4] and test_vector_02 = [3, 1, 2], then vector_addition(test_vector_01, test_vector_02) will return')
print(LA.vector_addition(test_vector_01, test_vector_02))
print('')
print('The second function in LA.py is scalar_vector_multi. It will take a vector and a scalar as its inputs and return our input vector scaled by our scalar.')
print('For example, if test_vector_01 = [1, 2, 4] and test_scalar_01 = 2, then scalar_vector_multi(test_vector_01, test_scalar_01) will return')
print(LA.scalar_vector_multi(test_vector_01, test_scalar_01))
print('')
print('The third function in LA.py is scalar_matrix_multi. It will take a matrix and a scalar as its inputs and return our input matrix scaled by our scalar.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]] and test_scalar_01 = 2, then scalar_matrix_multi(test_matrix_01, test_scalar_01) will return')
print(LA.scalar_matrix_multi(test_matrix_01, test_scalar_01))
print('')
print('The fourth function in LA.py is matrix_addition. It will take two matrices as its inputs and return their sum.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]] and test_matrix_02 = [[1,3,2],[3,5,3],[2,7,4]], then matrix_addition(test_matrix_01,test_matrix_02) will return')
print(LA.matrix_addition(test_matrix_01,test_matrix_02))
print('')
print('The fifth function in LA.py is matrix_vector_multi. It will take a matrix and a vector as its inputs and return their product matrix.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]] and test_vector_01 = [1, 2, 4], then matrix_vector_multi(test_matrix_01,test_vector_01) will return')
print(LA.matrix_vector_multi(test_matrix_01,test_vector_01))
print('')
print('The sixth function in LA.py is matrix_matrix_multi. It will take two matrices as its inputs and return their product matrix.')
print('For example, if test_matrix_03 = [[1,4],[2,5],[3,6]] and test_matrix_04 = [[7,9,11],[8,10,12]], then matrix_matrix_multi(test_matrix_03,test_matrix_04) will return')
print(LA.matrix_matrix_multi(test_matrix_03,test_matrix_04))
print('')
print('The seventh function in LA.py is absolute_value. It will take an integer as its input and return its absolute value.')
print('For example, if test_scalar_01 = 2, then absolute_value(test_scalar_01, 0) will return')
print(LA.absolute_value(test_scalar_01, 0))
print('')
print('The eighth function in LA.py is p_norm. It will take a vector and a scalar as its inputs and return the p-norm of our input vector, scaled by our scalar.')
print('For example, if test_vector_01 = [1, 2, 4] and test_scalar_01 = 2, p_norm(test_vector_01, test_scalar_01) will return')
print(LA.p_norm(test_vector_01, test_scalar_01))
print('')
print('The ninth function in LA.py is inf_norm. It will take a vector as its input and return the infinity norm of our input vector.')
print('For example, if test_vector_01 = [1, 2, 4], inf_norm(test_vector_01)) will return')
print(LA.inf_norm(test_vector_01))
print('')
print('The tenth function in LA.py is boolean_norm. It will take a vector, scalar, and boolean value as its inputs and return the infinity norm or p-norm of our input vector, contingent on our boolean value.')
print('For example, if test_vector_01 = [1, 2, 4], test_scalar_01 = 2, and boolean = True, boolean_norm(test_vector_01, test_scalar_01, True) will return')
print(LA.boolean_norm(test_vector_01, test_scalar_01, True))
print('')
print('The eleventh function in LA.py is inner_product. It will take a two vectors as its inputs and return their inner product.')
print('For example, if test_vector_01 = [1, 2, 4] and test_vector_02 = [3, 1, 2], inner_product(test_vector_01,test_vector_02) will return')
print(LA.inner_product(test_vector_01,test_vector_02))
print('')
print('')
print('QR.py contains a number of functions for performing Stable Gram-Schmidt QR factorization, orthonormalizing vectors, and Householder QR factorization.')
print('')
print('The first function in QR.py is stable_gram. It will take a matrix as its input and return its QR factorization via Stable Gram-Schmidt.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]], then stable_gram(test_matrix_01) will return')
print(QR.stable_gram(test_matrix_01))
print('')
print('The second function in QR.py is orthonormal_vectors. It will take a list of vectors as its input and return an orthonormalized list of vectors.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]], then orthonormal_vectors(test_matrix_01) will return')
print(QR.orthonormal_vectors(test_matrix_01))
print('')
print('The third function in QR.py is conjugate_transpose. It will take a matrix as its input and return its conjugate transpose.')
print('For example, if test_matrix_03 = [[1,4],[2,5],[3,6]], then conjugate_transpose(test_matrix_03) will return')
print(QR.conjugate_transpose(test_matrix_03))
print('')
print('The fourth function in QR.py is matrix_identity. It will take an integer n as its input and return an nxn identity matrix.')
print('For example, if n = 3, then matrix_identity(3) will return')
print(QR.matrix_identity(3))
print('')
print('The fifth function in QR.py is sign. It will take a number as its input and return a -1 if the number is negative or 1 if the number is positive.')
print('For example, if number = -6.8, then sign(-6.8) will return')
print(QR.sign(-6.8))
print('')
print('The sixth function in QR.py is vector_vector_multi. It will take two vectors as its inputs and return their product.')
print('For example, if test_vector_01 = [1, 2, 4] and test_vector_02 = [3, 1, 2], then vector_vector_multi(test_vector_01, test_vector_02) will return')
print(QR.vector_vector_multi(test_vector_01, test_vector_02))
print('')
print('The seventh function in QR.py is HH_V. It will take a vector as its input and return its reflection.')
print('For example, if test_vector_01 = [1, 2, 4], then HH_V(test_vector_01) will return')
print(QR.HH_V(test_vector_01))
print('')
print('The eighth function in QR.py is HH_F. It will take a vector as its input and return the F_k matrix used in Householder QR factorization.')
print('For example, if test_vector_01 = [1, 2, 4], then HH_F(test_vector_01) will return')
print(QR.HH_F(test_vector_01))
print('')
print('The ninth function in QR.py is HH_Q. It will take a matrix and an integer k as its inputs and return the Q_k matrix used in Householder decomposition.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]] and k = 2, then HH_Q(test_matrix_01, 2) will return')
print(QR.HH_Q(test_matrix_01, 2))
print('')
print('The tenth function in QR.py is HH. It will take a matrix its input and return its Householder QR factorization.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]], then HH(test_matrix_01) will return')
print(QR.HH(test_matrix_01))
print('')
print('')
print('LS.py contains two functions for performing backsubstitution and finding the least squares solution.')
print('')
print('The first function in LS.py is backsub. It will take a matrix and a vector as its inputs and return its backsubstitution.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]] and test_vector_01 = [1, 2, 4], then backsub(test_matrix_01, test_vector_01) will return')
print(LS.backsub(test_matrix_01, test_vector_01))
print('')
print('The second function in LS.py is least_squares. It will take a matrix and a vector as its inputs and return its least squares solution.')
print('For example, if test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]] and test_vector_01 = [1, 2, 4], then least_squares(test_matrix_01, test_vector_01) will return')
print(LS.least_squares(test_matrix_01, test_vector_01))


