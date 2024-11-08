import os
import random

def bienvenida():
    print("BIENVENIDO AL JUEGO DE SUDOKU ! \n\n")
    print("Instrucciones: \n")
    print("1. El tablero de sudoku es una cuadrícula de 9x9. \n")
    print("2. El tablero se divide en 9 subcuadrículas de 3x3 llamadas regiones. \n")
    print("3. El objetivo del juego es rellenar todas las celdas vacías con números del 1 al 9. \n")
    print("4. Cada número no debe repetirse en ninguna fila, columna o región. \n")
    print("5. Si se cumplen todas las condiciones, ¡ganarás! \n")
    print("6. ¡Buena suerte! \n\n")
    input("Presiona Enter para comenzar...")
    print("\n\n")
    os.system('cls')
    
    return None

def impresion(matriz):
    for i in range(9):
        
        if i % 3 == 0 and i != 0:
            print("-" * 25)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("||", end=" ")
            print(matriz[i][j], end=" ")
        print()
    return matriz


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
                            return True
                        matriz[i][j] = 0  # Retroceso (Backtracking)
                return False
    return True

def llenar(matriz):
    numeros = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if matriz[i][j] == 0:
                random.shuffle(numeros)
                for num in numeros:
                    if es_seguro(matriz, i, j, num):
                        matriz[i][j] = num
                        if llenar(matriz):
                            return True
                        matriz[i][j] = 0
                return False
    return True
    #return matriz

def borrar(matriz1, matriz2, dificultad):
    cantidad = 0
    # Copiar los contenidos de matriz_original a matriz_copiada
    for i in range(len(matriz1)): 
        for j in range(len(matriz1[0])): 
            matriz2[i][j] = matriz1[i][j]
            
    if dificultad == 1:
        cantidad = random.randint(36, 49)
    elif dificultad == 2:
        cantidad = random.randint(32, 35)
    elif dificultad == 3:
        cantidad = random.randint(17, 32)
        
    print("Cantidad de números que el usuario tendra como pistas:", cantidad)
    diferencia = 81 - cantidad
    #print("Diferencia (números a borrar):", diferencia)
    
    volados = 0  # Inicializar fuera del bucle for
    while volados < diferencia:
        
        posicion_fila = random.randint(0, 8)
        posicion_columna = random.randint(0, 8)
        
        # Solo incrementar volados si realmente hacemos un cambio en la matriz
        if matriz2[posicion_fila][posicion_columna] != 0:
            matriz2[posicion_fila][posicion_columna] = 0
            volados += 1

    return matriz2

