import random

def crear_tablero():
    return [["-" for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

def verificar_ganador(tablero, jugador):
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

def juego():
    tablero = crear_tablero()
    jugador_actual = "X"
    while True:
        imprimir_tablero(tablero)

        # Jugador hace su movimiento
        fila, col = map(int, input("Ingrese fila (1-3) y columna (1-3): ").split())
        while tablero[fila-1][col-1] != "-":
            print("Casilla ocupada. Intente nuevamente.")
            fila, col = map(int, input("Ingrese fila (1-3) y columna (1-3): ").split())
        tablero[fila-1][col-1] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡{jugador_actual} ha ganado!")
            break

        # Verificar empate
        if all(celda != "-" for fila in tablero for celda in fila):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        # Turno de la computadora (implementación simple)
        jugador_actual = "O"
        while True:
            fila, col = random.randint(0, 2), random.randint(0, 2)
            if tablero[fila][col] == "-":
                tablero[fila][col] = jugador_actual
                break

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡{jugador_actual} ha ganado!")
            break

        jugador_actual = "X"

if __name__ == "__main__":
    juego()