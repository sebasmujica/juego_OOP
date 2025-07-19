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
    
# Clase NPC Nivel Fácil
class NPCFacil(NPC):
    def __init__(self, x, y, nombre, acertijo, respuesta):
        # NPCs fáciles tienen 20 segundos para responder
        super().__init__(x, y, nombre, acertijo, respuesta, 20, "Fácil")
        
    def mostrar_pista(self):
        """Los NPCs fáciles pueden dar pistas"""
        pistas = {
            "4": "💡 Pista: Piensa en las extremidades que usan para caminar...",
            "gato": "💡 Pista: Es el animal doméstico que dice 'miau'...",
            "perro": "💡 Pista: Es el mejor amigo del hombre..."
        }
        return pistas.get(self.respuesta, "💡 Piensa bien en la pregunta...")