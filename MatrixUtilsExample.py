from MatrixUtils import write_matrix_to_file, read_matrix_from_csv_to_list, read_matrix_from_csv_to_numpy_matrix

"""
Created on Wed Sep  6 14:11:42 2023

@author: Antonio J. Nebro
"""


if __name__ == "__main__":
    """ Example of program that writes and read matrices
    """
    write_matrix_to_file(100, 100, "matrix1000.1.csv")
    write_matrix_to_file(100, 100, "matrix1000.2.csv")

    
    """list_matrix = read_matrix_from_csv_to_list("30x30.csv")
    print(list_matrix)

    numpy_matrix = read_matrix_from_csv_to_numpy_matrix("30x30.csv")
    print(type(numpy_matrix))
    print(numpy_matrix.shape)
    print(numpy_matrix)
    """

