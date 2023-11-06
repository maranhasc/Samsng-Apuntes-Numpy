import time
import numpy as np
"En este caso vamos a crear el fichero para multiplicar matrices utilizando numpy"
"primero importamos la funcion read_matrix_from_csv_to_numpy_matrix"
from MatrixUtils import read_matrix_from_csv_to_numpy_matrix

"definimos como funciona la funcion a la que metemos como parametros las dos matrices, matrix1 y matrix2"

def matrix_multiplication_with_numpy(matrix1, matrix2):
    "El metodo np.dot es el que usamos para la multiplicacion de matrices"
    return np.dot(matrix1,matrix2)


if __name__ == "__main__":
    """ Example of program that writes and read matrices
    """

    
    "mediante el read_matrix_from_csv_to_numpy_matrix cogemos los ficheros que hemos generado y los guardamos en sus respectivas variables"
    matrix1 = read_matrix_from_csv_to_numpy_matrix("1000x1000a.csv")
    matrix2 = read_matrix_from_csv_to_numpy_matrix("1000x1000b.csv")

    t0 = time.time()
    "Llamamos a la funcion por ultima vez para guardar el tiempo que tarda desde que se empieza a ejecutar hasta que termina"
    matrix = matrix_multiplication_with_numpy(matrix1, matrix2)
    t1 = time.time()
    computing_time = t1 - t0
    print(computing_time)

    

    

