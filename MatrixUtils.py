import random
import sys
import numpy as np
import csv

"""
Created on Wed Sep  6 14:11:42 2023

@author: Antonio J. Nebro
"""

def write_matrix_to_file(number_of_rows: int , number_of_columns: int, file_name:str, seed:int = 4):
    """ Function that generates a matrix of random numbers and writes it into a CSV file
    """
    random.seed(seed)
    file = open(file_name, "w") 
    
    for row_index in range(number_of_rows):
        row = random.sample(range(1000), number_of_columns)
        for number in row[:-1]:
            file.write(str(number) + ".0,")
        file.write(str(row[-1]) + "1.0")
        file.write("\n")
        
    file.close()
    
def read_matrix_from_csv_to_list(file_name:str):
    """ Function that reads a matrix of numbers stored in a CSV file into a list
    """
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def read_matrix_from_csv_to_numpy_matrix(file_name:str):
    """ Function that reads a matrix of numbers stored in a CSV file into a numpy matrix
    """
    data = np.genfromtxt(file_name, delimiter=',')

    return data


