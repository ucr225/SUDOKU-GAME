matriz = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def es_seguro(matriz, fila, col, num):
    for x in range(9):
        if matriz[fila][x] == num or matriz[x][col] == num:
            return False
    inicio_fila, inicio_col = 3 * (fila // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if matriz[i + inicio_fila][j + inicio_col] == num:
                return False
    return True

def resolver(matriz):
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 0:
                for num in range(1, 10):
                    if es_seguro(matriz, i, j, num):
                        matriz[i][j] = num
                        if resolver(matriz):
                            return matriz
                        matriz[i][j] = 0  # Retroceso (Backtracking)
                return None  # Si no se puede resolver, devuelve None
    return matriz  # Si está resuelto, devuelve la matriz

# Probar la solución
resultado = resolver(matriz)
if resultado:
    for fila in resultado:
        print(fila)
else:
    print("Este Sudoku no tiene solución.")
