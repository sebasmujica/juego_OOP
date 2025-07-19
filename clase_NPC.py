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
    
    # Clase NPC Nivel Medio  
class NPCMedio(NPC):
    def __init__(self, x, y, nombre, acertijo, respuesta):
        # NPCs medios tienen 15 segundos para responder
        super().__init__(x, y, nombre, acertijo, respuesta, 15, "Medio")
        
    def penalizacion_tiempo(self, tiempo_transcurrido):
        """Los NPCs medios tienen penalización si tardas mucho"""
        if tiempo_transcurrido > self.tiempo_limite * 0.7:
            print("⚠️ Tardaste demasiado, pero aún puedes responder...")
            return True
        return False