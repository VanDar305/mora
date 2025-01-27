def crear_tablero():
    """Crea un tablero de 3x3 vacío."""
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    """Imprime el tablero en la consola."""
    for fila in tablero:
        print('|', end='')
        for celda in fila:
            print(f' {celda} |', end='')
        print('\n---------')

def mover(tablero, fila, columna, jugador):
    """Realiza un movimiento en el tablero."""
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador
        return True
    else:
        return False

def verificar_ganador(tablero, jugador):
    """Verifica si un jugador ha ganado."""
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
    """Inicia el juego del tres en raya."""
    tablero = crear_tablero()
    jugador_actual = 'X'
    
    while True:
        imprimir_tablero(tablero)
        
        fila = int(input(f"Jugador {jugador_actual}, ingresa el número de fila (1-3): ")) - 1
        columna = int(input(f"Jugador {jugador_actual}, ingresa el número de columna (1-3): ")) - 1
        
        if mover(tablero, fila, columna, jugador_actual):
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡El jugador {jugador_actual} ha ganado!")
                break
            
            jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        else:
            print("Casilla ocupada. Intenta nuevamente.")
        
        # Verificar empate
        if all(celda != ' ' for fila in tablero for celda in fila):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

jugar()