# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 00:46:18 2021

@author: Kadeem
"""

import LS
import pytest

test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]


test_matrix_01 = [[1,4,7],[2,5,8],[3,6,9]]
test_matrix_02 = [[1,3,2],[3,5,3],[2,7,4]]


def test_backsub():
    assert LS.backsub(test_matrix_01, test_vector_01) == [-0.06666666666666665, -0.1333333333333333, 0.4444444444444444]
    assert LS.backsub(test_matrix_02, test_vector_02) == [3.5, -0.5, 0.5]
    
def test_least_squares():
    assert LS.least_squares(test_matrix_01, test_vector_01) == [(1.8014398509481976e+16+0j), (-3.6028797018963964e+16+0j), (1.8014398509481984e+16+0j)]
    assert LS.least_squares(test_matrix_02, test_vector_02) == [(4.3333333333333215+0j), (1.3333333333333328+0j), (-2.6666666666666616+0j)]
