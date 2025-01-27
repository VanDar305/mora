def dibujar_tablero(tablero):
  print('-------------')
  for i in range(3):
    print('|', tablero[i][0], '|', tablero[i][1], '|', tablero[i][2], '|')
    print('-------------')

def verificar_ganador(tablero, jugador):
  for i in range(3):
    if all(tablero[i][j] == jugador for j in range(3)):
      return True
  for j in range(3):
    if all(tablero[i][j] == jugador for i in range(3)):
      return True
  if all(tablero[i][i] == jugador for i in range(3)):
    return True
  if all(tablero[i][2-i] == jugador for i in range(3)):
    return True
  return False

def jugar():
  tablero = [[' ' for _ in range(3)] for _ in range(3)]
  jugador_actual = 'X'

  while True:
    dibujar_tablero(tablero)

    fila = int(input("Fila (1-3): ")) - 1
    columna = int(input("Columna (1-3): ")) - 1

    if tablero[fila][columna] != ' ':
      print("Casilla ocupada. Intenta de nuevo.")
      continue

    tablero[fila][columna] = jugador_actual

    if verificar_ganador(tablero, jugador_actual):
      dibujar_tablero(tablero)
      print(f"¡{jugador_actual} ha ganado!")
      break

    if all(all(tablero[i][j] != ' ' for j in range(3)) for i in range(3)):
      dibujar_tablero(tablero)
      print("¡Empate!")
      break

    jugador_actual = 'O' if jugador_actual == 'X' else 'X'

jugar()