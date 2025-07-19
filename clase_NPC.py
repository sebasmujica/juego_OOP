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
    
    
# Clase NPC Nivel Difícil
class NPCDificil(NPC):
    def __init__(self, x, y, nombre, acertijo, respuesta):
        # NPCs difíciles tienen solo 10 segundos para responder
        super().__init__(x, y, nombre, acertijo, respuesta, 10, "Difícil")
        self.intentos_fallidos = 0
        
    def verificar_respuesta(self, respuesta_jugador):
        """Los NPCs difíciles son más estrictos con las respuestas"""
        respuesta_limpia = respuesta_jugador.strip().lower()
        es_correcta = respuesta_limpia == self.respuesta
        
        if not es_correcta:
            self.intentos_fallidos += 1
            if self.intentos_fallidos >= 2:
                print("💀 Demasiados intentos fallidos. ¡Tendrás que ser más cuidadoso!")
        
        return es_correcta
    
    def mostrar_advertencia(self):
        """Los NPCs difíciles muestran advertencias especiales"""
        return f"🔥 NIVEL DIFÍCIL - Solo tienes {self.tiempo_limite} segundos. ¡Piensa rápido!"