#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 18:36:59 2023

@author: ajnebro
"""
import time
from MatrixUtils import read_matrix_from_csv_to_list

def matrix_multiplication_with_lists(matrix1, matrix2):
    number_of_rows = len(matrix1)
    number_of_columns = len(matrix1[0])
    print(number_of_rows)
    print(number_of_columns)

    # Result matrix initialized to 0s
    result_matrix = []
    for i in range(number_of_rows):
        row = [0.0 for _ in range(number_of_columns)]
        result_matrix.append(row)

    for i in range(number_of_rows):
        for j in range(number_of_columns):
            for k in range(len(matrix2)):
                result_matrix[i][j] = result_matrix[i][j] + float(matrix1[i][k]) * float(matrix2[k][j])

    return result_matrix


if __name__ == "__main__":
    """ Example of program that writes and read matrices
    """
    
    matrix1 = read_matrix_from_csv_to_list("1000x1000a.csv")
    matrix2 = read_matrix_from_csv_to_list("1000x1000b.csv")

    t0 = time.time()
    matrix = matrix_multiplication_with_lists(matrix1, matrix2)
    t1 = time.time()

    computing_time = t1 - t0
    print(computing_time)

