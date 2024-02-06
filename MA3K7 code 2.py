# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:24:52 2024

@author: corey
"""
import numpy as np 
import math
from numpy import linalg

n = 3
matrix = np.array([[2]*n]*n)
print(matrix)

for i in range(math.ceil((n**2)/2)):
    p1_row = int(input("player 1 row (increment from 0): "))
    p1_column = int(input("player 1 column (increment from 0): "))
    p2_row = int(input("player 2 row (increment from 0): "))
    p2_column = int(input("player 2 column (increment from 0): "))
    matrix[p1_row, p1_column] = 0
    if p2_row != "skip":
        matrix[p2_row, p2_column] = 1
    print(matrix)

det = int(np.linalg.det(matrix))
print(det)
if det == 0:
    print("player one wins.")
else:
    print("player two wins")