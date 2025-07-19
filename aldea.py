#Crear una aldea que tenga casas y lagos y que el mapa sea de 50 x 50
class Aldea:
    def __init__(self, filas_tablero, columnas_tablero):
        self.filas_tablero = filas_tablero
        self.columnas_tablera = columnas_tablero
        self.mapa = [['⬜' for _ in range(columnas_tablero)] for _ in range (filas_tablero)]
        
    def imprimir_mapa(self):
        for fila in self.mapa:
            print(' '.join(fila))
            
    def agregar_casa(self,fila_tablero,columna_tablero):
        if 0 <= fila_tablero < self.filas_tablero and 0 <= columna_tablero < self.columnas_tablera:
            self.mapa[fila_tablero][columna_tablero] = '🏘️'
    
    def agregar_lago(self,fila_tablero,columna_tablero):
        if 0 <= fila_tablero < self.filas_tablero and 0 <= columna_tablero < self.columnas_tablera:
            self.mapa[fila_tablero][columna_tablero] = '🌊'
    
    def agregar_calle(self, fila_tablero,columna_tablero):
         if 0 <= fila_tablero < self.filas_tablero and 0 <= columna_tablero < self.columnas_tablera:
            self.mapa[fila_tablero][columna_tablero] = '🛣️'
    

Aldea1 = Aldea(20,20)

for fila in range(20):
    for columna in range(20):
        if fila % 2:
            if columna % 5 == 0 or columna % 5 ==3:
                Aldea1.agregar_calle(fila,columna)
            else:
                Aldea1.agregar_casa(fila,columna)
        else:
            Aldea1.agregar_calle(fila,columna)
                
Aldea1.imprimir_mapa()