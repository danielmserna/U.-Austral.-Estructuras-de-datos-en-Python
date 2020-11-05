
matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

matriz[0][0]
matriz[1][2]

#Ejemplo función suma de matrices
def suma_matrices(A,B):

    """
        Suma dos matrices.
        Precondición: A y B son del mismo tamaño y son matrices de números.
    """

    cant_filas = len(A)
    cant_cols = len(A[0])

    C = []

    for fila in range(cant_filas):
        fila_suma = []
        for col in range(cant_cols):
            fila_suma.append(A[fila][col] + B[fila][col])
        C.append(fila_suma)
    return C

suma_matrices(matriz,matriz)
