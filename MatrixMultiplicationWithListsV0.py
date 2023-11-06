#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 18:36:59 2023

@author: ajnebro
"""
import time
from MatrixUtils import read_matrix_from_csv_to_list

if __name__ == "__main__":
    """ Example of program that writes and read matrices
    """
    
    matrix1 = read_matrix_from_csv_to_list("matrix50.1.csv")
    matrix2 = read_matrix_from_csv_to_list("matrix50.2.csv")
    
    number_of_rows = len(matrix1)
    number_of_columns = len(matrix1[0])
    print(number_of_rows)
    print(number_of_columns)
    
    t0 = time.time()
    
    # Result matrix initialized to 0s
    result_matrix = []
    for i in range(number_of_rows):
        row = [0.0 for _ in range(number_of_columns)]
        result_matrix.append(row)
    

    print(result_matrix)
    
    for i in range(number_of_rows):
        for j in range(number_of_columns):
            for k in range(len(matrix2)):
                result_matrix[i][j] = result_matrix[i][j] + float(matrix1[i][k]) * float(matrix2[k][j])
                
    t1 = time.time()
    
    computing_time = t1 - t0
    
    print(result_matrix)
            ""
            "Hay que crear la de numpy"