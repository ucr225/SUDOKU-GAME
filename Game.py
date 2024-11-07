import Functions


tablero_resuelto = [[0 for _ in range(9)] for _ in range(9)]
#tablero_resuelto = Functions.generar(tablero_resuelto)
tablero_jugador = [[0 for _ in range(9)] for _ in range(9)]


    
Functions.bienvenida()
"""
    
    dificultad = int(input("Ingrese la dificultad del juego (facil(1), medio (2), dificil (3) ): "))

while dificultad not in [1, 2, 3]:
    dificultad = int(input("Ingrese la dificultad del juego (facil(1), medio (2), dificil (3) ): "))


"""

dificultad = 2
Functions.llenar(tablero_resuelto)

Functions.impresion(tablero_resuelto)
print("Tablero generado")
print("iiiiiiiiiiiiiii")

print("iiiiiiiiiiiiiii")

Functions.borrar(tablero_resuelto,tablero_jugador,dificultad)
Functions.impresion(tablero_jugador)






    





 
