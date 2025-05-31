import Functions
import os

tablero_resuelto = [[0 for _ in range(9)] for _ in range(9)]
#tablero_resuelto = Functions.generar(tablero_resuelto)
tablero_jugador = [[0 for _ in range(9)] for _ in range(9)]


    
Functions.bienvenida()

    
dificultad = int(input("Ingrese la dificultad del juego (facil(1), medio (2), dificil (3) ): "))

while dificultad not in [1, 2, 3]:
    dificultad = int(input("Ingrese la dificultad valida  del juego (facil(1), medio (2), dificil (3) ): "))
    os.system('cls')



#esto lo use para testing
#dificultad = 2
Functions.llenar(tablero_resuelto)

#Functions.impresion(tablero_resuelto)
print("Tablero generado")
#print("iiiiiiiiiiiiiii")

#print("iiiiiiiiiiiiiii")
#Functions.impresion(tablero_resuelto)
#print("iiiiiiiiiiiiiii")
Functions.borrar(tablero_resuelto,tablero_jugador,dificultad)
Functions.impresion(tablero_jugador)
print("Tablero jugador generado,a continuacion usted debe proceder a llenar los espacios vacios marcados con 0")


while tablero_resuelto != tablero_jugador  :
    numero=int(input("Ingrese el numero que desea colocar en la CELDA: "))
    os.system('cls')
    while numero not in range(1,9):
        numero=int(input("Ingrese el numero que desea colocar en la CELDA: "))
        #os.system('cls')
    
    fila=int(input("Ingrese la fila en la que desea colocar el numero: "))
    fila=fila-1
    while fila not in range(0,8):
        fila=int(input("Ingrese la fila en la que desea colocar el numero: "))
        fila=fila-1
    columna=int(input("Ingrese la columna en la que desea colocar el numero: "))
    columna=columna-1
    while columna not in range(0,8):
        columna=int(input("Ingrese la columna en la que desea colocar el numero: "))     
        columna=columna-1 
    
    while tablero_jugador[fila][columna] != 0:
        os.system('cls')
        print("Esta casilla ya esta ocupada, por favor seleccione otra")
        fila=int(input("Ingrese la fila en la que desea colocar el numero: "))
        while fila not in range(0,8):
            fila=int(input("Ingrese la fila en la que desea colocar el numero: ")) 
            fila=fila-1
        columna=int(input("Ingrese la columna en la que desea colocar el numero: "))
        while columna not in range(0,8):
            columna=int(input("Ingrese la columna en la que desea colocar el numero: "))
            columna=columna-1
    
    if numero == tablero_resuelto[fila][columna]:
        os.system('cls')
        tablero_jugador[fila][columna] = numero
        print("Numero ingresado correctamente")
        if tablero_resuelto == tablero_jugador:
            print("Felicidades, has ganado!!")
            break
        
    else:
        os.system('cls')
        print("Numero incorrecto")
        
        tablero_jugador[fila][columna] = 0
    Functions.impresion(tablero_jugador)
