# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:11:28 2021

@author: Kadeem
"""
import LA
import pytest

test_vector_01: list = [1, 2, 4]
test_vector_02: list = [3, 1, 2]
test_vector_03: list= [4, 2, 1]
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

def test_new_matrix():
    assert LA.new_matrix(test_scalar_01, test_scalar_02) == [[0, 0, 0], [0, 0, 0]]
    assert LA.new_matrix(test_scalar_02, test_scalar_01) == [[0, 0], [0, 0], [0, 0]]

def test_vector_addition():
    assert LA.vector_addition(test_vector_01, test_vector_02) == [4, 3, 6]
    assert LA.vector_addition(test_vector_03, test_vector_04) == [9, 5, 3]

def test_scalar_vector_multi():
    assert LA.scalar_vector_multi(test_vector_01, test_scalar_01) == [2, 4, 8]
    assert LA.scalar_vector_multi(test_vector_02, test_scalar_02) == [9, 3, 6]
    
def test_scalar_matrix_multi():
    assert LA.scalar_matrix_multi(test_matrix_01, test_scalar_01) == [[2, 8, 14], [4, 10, 16], [6, 12, 18]]
    assert LA.scalar_matrix_multi(test_matrix_03, test_scalar_02) == [[3, 12], [6, 15], [9, 18]]
    
def test_matrix_addition():
    assert LA.matrix_addition(test_matrix_01,test_matrix_02) == [[2, 7, 9], [5, 10, 11], [5, 13, 13]]
    assert LA.matrix_addition(test_matrix_06,test_matrix_07) == [[3, 9], [9, 16]]
    
def test_matrix_vector_multi():
    assert LA.matrix_vector_multi(test_matrix_01,test_vector_01) == [17, 38, 59]
    assert LA.matrix_vector_multi(test_matrix_02,test_vector_02) == [10, 28, 17]
    
def test_matrix_matrix_multi():
    assert LA.matrix_matrix_multi(test_matrix_03,test_matrix_04) == [[58, 139], [64, 154]]
    assert LA.matrix_matrix_multi(test_matrix_06,test_matrix_07) == [[32, 49], [48, 75]]
    
def test_absolute_value():
    assert LA.absolute_value(test_scalar_01, 0) == 2.0
    assert LA.absolute_value(test_scalar_02, 0) == 3.0
    
def test_p_norm():
    assert LA.p_norm(test_vector_01, test_scalar_01) == 4.58257569495584
    assert LA.p_norm(test_vector_01, test_scalar_02) == 4.179339196381232
    
def test_inf_norm():
    assert LA.inf_norm(test_vector_01) == 4.0
    assert LA.inf_norm(test_vector_02) == 3.0
    
def test_boolean_norm():
    assert LA.boolean_norm(test_vector_01, test_scalar_01, True) == 4.0
    assert LA.boolean_norm(test_vector_02, test_scalar_02, False) == 3.3019272488946263
    
def test_inner_product():
    assert LA.inner_product(test_vector_01,test_vector_02) == 13
    assert LA.inner_product(test_vector_03,test_vector_04) == 28