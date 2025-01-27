def crear_tablero():
    """Crea un tablero de 3x3 vacío."""
    return [["-" for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    """Imprime el tablero en la consola."""
    for fila in tablero:
        print(" ".join(fila))

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador ha ganado."""
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
    """Función principal del juego."""
    tablero = crear_tablero()
    jugador_actual = "X"
    
    while True:
        imprimir_tablero(tablero)
        
        fila, col = map(int, input(f"Jugador {jugador_actual}, ingresa fila (1-3) y columna (1-3): ").split())
        
        if not (1 <= fila <= 3 and 1 <= col <= 3):
            print("Posición inválida. Intenta nuevamente.")
            continue
        
        if tablero[fila-1][col-1] != "-":
            print("Casilla ocupada. Intenta nuevamente.")
            continue
        
        tablero[fila-1][col-1] = jugador_actual
        
        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador_actual} ha ganado!")
            break
        
        if all(celda != "-" for fila in tablero for celda in fila):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break
        
        jugador_actual = "O" if jugador_actual == "X" else "X"

jugar()