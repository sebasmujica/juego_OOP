import time , random , os

# Clase base para NPCs
class NPC:
    def __init__(self, x, y, nombre, acertijo, respuesta, tiempo_limite, dificultad):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.acertijo = acertijo
        self.respuesta = respuesta.lower()
        self.tiempo_limite = tiempo_limite
        self.dificultad = dificultad
        self.resuelto = False
    
    def verificar_respuesta(self, respuesta_jugador):
        return respuesta_jugador.strip().lower() == self.respuesta