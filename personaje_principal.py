
class personaje_principal:
    def __init__(self,fila_inicio,columna_inicio, fila_tablero , columna_tablero):
        self.fila_inicio , self.columna_inicio = fila_inicio,columna_inicio
        self.fila_tablero , self.columna_tablero = fila_tablero, columna_tablero
        self.tablero = [['⬜️' for f in range(5)] for c in range(5)]
        self.casilla = '⬜️'
        self.jugador = '🟥'
        self.tablero[0][0] = self.jugador
    def moverse(self,entrada_teclado):
        fila_siguiente , columna_siguiente = self.fila_inicio, self.columna_inicio
        #Movimiento hacia arriba
        if entrada_teclado == 'w' and self.fila_inicio > 0:
            fila_siguiente -= 1
        #Movimiento hacia abajo
        elif entrada_teclado == 's' and self.fila_inicio < (self.fila_tablero - 1):
            fila_siguiente += 1
        #Movimiento hacia la derecha
        elif entrada_teclado == 'd' and self.columna_inicio < (self.columna_tablero - 1):
            columna_siguiente+= 1
        #Movimiento hacia la izquierda
        elif entrada_teclado == 'a' and self.columna_inicio > 0:
            columna_siguiente -= 1
        
        if (fila_siguiente,columna_siguiente) != (self.fila_inicio,self.columna_inicio):
            self.tablero[fila_siguiente][columna_siguiente] = self.jugador
            self.tablero[self.fila_inicio][self.columna_inicio] = self.casilla
            self.fila_inicio,self.columna_inicio = fila_siguiente, columna_siguiente
