def crear_tablero():
    """Crea un tablero de 3x3 vacío."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    """Imprime el tablero en la consola."""
    for fila in tablero:
        print(' '.join(fila))

def marcar_casilla(tablero, fila, columna, simbolo):
    """Marca una casilla del tablero con el símbolo del jugador."""
    tablero[fila][columna] = simbolo

def verificar_victoria(tablero, simbolo):
    """Verifica si un jugador ha ganado."""
    # Verificar filas
    for fila in tablero:
        if all(casilla == simbolo for casilla in fila):
            return True
    
    # Verificar columnas
    for columna in range(3):
        if all(tablero[fila][columna] == simbolo for fila in range(3)):
            return True
    
    # Verificar diagonales
    if all(tablero[i][i] == simbolo for i in range(3)) or \
       all(tablero[i][2-i] == simbolo for i in range(3)):
        return True
    
    return False

def jugar():
    """Función principal del juego."""
    tablero = crear_tablero()
    jugador_actual = 'X'

    while True:
        imprimir_tablero(tablero)
        
        fila = int(input(f"Jugador {jugador_actual}, ingresa el número de fila (1-3): ")) - 1
        columna = int(input(f"Jugador {jugador_actual}, ingresa el número de columna (1-3): ")) - 1

        if tablero[fila][columna] != ' ':
            print("Casilla ocupada. Intenta otra vez.")
            continue

        marcar_casilla(tablero, fila, columna, jugador_actual)

        if verificar_victoria(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        if all(casilla != ' ' for fila in tablero for casilla in fila):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

jugar()