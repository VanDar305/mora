def crear_tablero():
  """Crea un tablero de 3x3 vacío."""
  tablero = []
  for _ in range(3):
    fila = [' '] * 3
    tablero.append(fila)
  return tablero

def imprimir_tablero(tablero):
  """Imprime el tablero en la consola."""
  for fila in tablero:
    print('|', end='')
    for celda in fila:
      print(f' {celda} |', end='')
    print()

def hacer_jugada(tablero, jugador, fila, columna):
  """Hace una jugada en el tablero."""
  if tablero[fila][columna] == ' ':
    tablero[fila][columna] = jugador
    return True
  else:
    print("Casilla ocupada. Intenta otra vez.")
    return False

def verificar_ganador(tablero, jugador):
  """Verifica si un jugador ha ganado."""
  # Comprobar filas
  for fila in tablero:
    if all(celda == jugador for celda in fila):
      return True

  # Comprobar columnas
  for col in range(3):
    if all(tablero[fila][col] == jugador for fila in range(3)):
      return True

  # Comprobar diagonales
  if all(tablero[i][i] == jugador for i in range(3)) or \
     all(tablero[i][2-i] == jugador for i in range(3)):
    return True

  return False

def main():
  tablero = crear_tablero()
  jugador_actual = 'X'

  while True:
    imprimir_tablero(tablero)

    fila = int(input("Ingrese el número de fila (0-2): "))
    columna = int(input("Ingrese el número de columna (0-2): "))

    if hacer_jugada(tablero, jugador_actual, fila, columna):
      if verificar_ganador(tablero, jugador_actual):
        print(f"¡El jugador {jugador_actual} ha ganado!")
        break

      jugador_actual = 'O' if jugador_actual == 'X' else 'X'
    else:
      continue

if __name__ == "__main__":
  main()