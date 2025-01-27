def crear_tablero():
    """Crea un tablero inicial de 3x3"""
    tablero = [["-" for _ in range(3)] for _ in range(3)]
    return tablero

def imprimir_tablero(tablero):
    """Imprime el tablero en la consola"""
    for fila in tablero:
        print(" ".join(fila))

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador ha ganado"""
    # Verificar filas
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
    # Verificar columnas
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def jugar():
    """Función principal del juego"""
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, ingresa la fila (1-3): ")) - 1
        col = int(input(f"Jugador {jugador_actual}, ingresa la columna (1-3): ")) - 1

        if tablero[fila][col] != "-":
            print("Casilla ocupada. Intenta otra vez.")
            continue

        tablero[fila][col] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if all(celda != "-" for fila in tablero for celda in fila):
            print("¡Empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

jugar()