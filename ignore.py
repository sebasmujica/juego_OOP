 def imprimir(self):
        os.system('clear')
        for f in range(5):
            print("".join(self.tablero[f]))



jugador = personaje_principal(0,0,5,5)
contador = 5
while True > 0:
    jugador.imprimir()
    movimiento = input()
    if movimiento == 'e':
        break
    jugador.moverse(movimiento)
    jugador.imprimir()


