"""
This assignment is due by 11:59pm on 10/22/2021. 

For this assignment you will be adding functinos to the LA.py script from HW03.
All functions must satisfy the same requirements as in HW03. The functions you
will need to add are

#1) A function which takes a scalar as it's input and returns it's absolute
value. Note that this function must be able to take both real numbers and
complex numbers as input!!!

#2) A function which takes the as it's arguments

1) A vector stored as a list.

2) A float valued scalar, set to default as 2. 

and returns the p-norm of the input vector. Which p-norm must be determined using
the float valued scalar input. If no argument is given, it should default to
2. 

#3) A function which takes as it's argument a vector stored as a list and
returns the infinity norm of the input vector.

#4) A function which takes as it's arguments

1) A vector stored as a list.

2) An float valued scalar, set to default as 2.

3) A boolean value, set to default as False.

The function will return the p-norm of the input vector. If the boolean value is
given as True, the function will return the infinity norm of the input vector.
Otherwise it will return the p-norm of the vector corresponding to the float 
scalar argument. This function must use the functions from problem #2 and
problem #3 to earn credit. 

#5) A function which takes as it's arguments two vectors, stored as lists. This
function then returns the inner product of these vectors. Your function must be
able to handle complex numbers!
"""

#Problem 1
def absolute_value(integer:int, integer_1:complex):
    z = integer + integer_1
    result = (z*z.conjugate())
    return result**(1/2)

#Problem 2
def p_norm(vector, scalar:float = 2):
    
    result: list[float] = []
    for element in vector:
        result.append(0)
    
    for i in range(len(vector)):
        result[i] = absolute_value(vector[i], 0)**(scalar)
    result = sum(result)**(1/scalar)
    return result

#Problem 3
def inf_norm(vector):
    result = absolute_value(max(vector),0)
    return result

#Problem 4
def boolean_norm(vector, scalar:float = 2, boolean = False):
    if boolean == True:
        inf_norm(vector)
        return inf_norm(vector)
    else: 
        p_norm(vector, scalar)
        return p_norm(vector, scalar)

#Problem 5
def inner_product(vector_1, vector_2):
    result: list[float] = []
    for element in vector_1:
        result.append(0)
        
    for i in range(len(vector_1)):
        result[i] = vector_1[i]*vector_2[i]
    result = sum(result)
    return result