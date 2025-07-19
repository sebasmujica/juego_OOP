class Juego():
    def __init__(self):
        self.fila_jugador = None
        self.columna_jugador = None
        self.fila_evento_facil , self.columna_evento_facil = None
        self.fila_evento_medio , self.columna_evento_medio = None
        self.fila_evento_dificil , self.columna_evento_dificil = None

    def evento(self):
        if (self.fila_jugador, self.columna_jugador) in [(self.fila_evento_facil,self.columna_evento_facil),(self.fila_evento_medio,self.columna_evento_medio),(self.fila_evento_dificil,self.columna_evento_dificil)]:
            #TODO Se incia el evento 
            pass


