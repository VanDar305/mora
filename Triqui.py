def dibujar_tablero(tablero):
    print('-------------')
    for fila in tablero:
        print('|', end='')
        for celda in fila:
            print(f' {celda} |', end='')
        print('\n-------------')

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

def jugar():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador_actual = 'X'

    while True:
        dibujar_tablero(tablero)

        # Pedir al jugador que ingrese su movimiento
        fila = int(input(f"Jugador {jugador_actual}, ingresa la fila (1-3): ")) - 1
        columna = int(input(f"Jugador {jugador_actual}, ingresa la columna (1-3): ")) - 1

        if not (0 <= fila <= 2 and 0 <= columna <= 2):
            print("Movimiento inválido. Intenta de nuevo.")
            continue

        if tablero[fila][columna] != ' ':
            print("Casilla ocupada. Intenta de nuevo.")
            continue

        tablero[fila][columna] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            dibujar_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if all(celda != ' ' for fila in tablero for celda in fila):
            dibujar_tablero(tablero)
            print("¡Empate!")
            break
        jugador_actual = "O" if jugador_actual == "X" else "X"

jugar()  
    