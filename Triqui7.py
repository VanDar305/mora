def crear_tablero():
    return [[' ' for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print('|', end=' ')
        for celda in fila:
            print(celda, end=' | ')
        print()

def ingresar_movimiento(tablero, jugador):
    while True:
        try:
            fila = int(input(f"Jugador {jugador}, ingresa la fila (1-3): ")) - 1
            columna = int(input(f"Jugador {jugador}, ingresa la columna (1-3): ")) - 1
            if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == ' ':
                return fila, columna
            else:
                print("Movimiento inválido. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or \
           all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2-i] == jugador for i in range(3)):
        return True

    return False

def jugar():
    tablero = crear_tablero()
    jugador = 'X'
    while True:
        mostrar_tablero(tablero)
        fila, columna = ingresar_movimiento(tablero, jugador)
        tablero[fila][columna] = jugador

        if verificar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print(f"¡El jugador {jugador} ha ganado!")
            break

        if all(all(celda != ' ' for celda in fila) for fila in tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

        jugador = 'O' if jugador == 'X' else 'X'

if __name__ == "__main__":
    jugar()