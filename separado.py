import time
import random
import os

# Emojis del juego
EMOJIS = {
    "jugador": "🧍",
    "npc_pendiente": "❗",
    "npc_resuelto": "✅",
    "puente": "🛤️",
    "agua": "🌊",
    "pasto": "🌿",
    "casa": "🏠",
}

# Clase Jugador
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.acertijos_resueltos = 0

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

# Clase principal del juego
class JuegoAcertijosConsola:
    def __init__(self):
        self.mapa = [["🌿" for _ in range(20)] for _ in range(10)]
        self.jugador = Jugador(0, 0)
        
        # Crear NPCs usando las clases específicas
        self.npcs = [
            NPCFacil(2, 2, "Guardián del Bosque", "¿Cuántas patas tiene un gato?", "4"),
            NPCMedio(5, 5, "Sabio del Puente", "Si tienes 10 manzanas y das 3, ¿cuántas te quedan?", "7"),
            NPCDificil(8, 15, "Oráculo de la Casa", "Soy alto cuando soy joven y bajo cuando soy viejo. ¿Qué soy?", "vela"),
        ]
        
        self.puente = [(4, i) for i in range(8, 12)]
        self.agua = [(4, i) for i in range(20) if (4, i) not in self.puente]
        self.casa = [(8, 14), (8, 15), (8, 16)]

    def dibujar_mapa(self):
        os.system("cls" if os.name == "nt" else "clear")
        for y in range(len(self.mapa)):
            fila = ""
            for x in range(len(self.mapa[0])):
                if self.jugador.x == y and self.jugador.y == x:
                    fila += EMOJIS["jugador"]
                elif any(npc.x == y and npc.y == x for npc in self.npcs):
                    npc = next(n for n in self.npcs if n.x == y and n.y == x)
                    fila += EMOJIS["npc_resuelto"] if npc.resuelto else EMOJIS["npc_pendiente"]
                elif (y, x) in self.casa:
                    fila += EMOJIS["casa"]
                elif (y, x) in self.puente:
                    fila += EMOJIS["puente"]
                elif (y, x) in self.agua:
                    fila += EMOJIS["agua"]
                else:
                    fila += EMOJIS["pasto"]
            print(fila)
        print(f"\nResueltos: {self.jugador.acertijos_resueltos}/{len(self.npcs)}")

    def mover_jugador(self, direccion):
        dx, dy = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}.get(direccion, (0, 0))
        nuevo_x = self.jugador.x + dx
        nuevo_y = self.jugador.y + dy
        if 0 <= nuevo_x < len(self.mapa) and 0 <= nuevo_y < len(self.mapa[0]):
            if (nuevo_x, nuevo_y) in self.agua:
                print("🌊 No puedes cruzar el río sin usar el puente.")
                time.sleep(1)
                return
            self.jugador.x = nuevo_x
            self.jugador.y = nuevo_y

    def interactuar(self):
        for npc in self.npcs:
            if abs(npc.x - self.jugador.x) <= 1 and abs(npc.y - self.jugador.y) <= 1 and not npc.resuelto:
                print(f"\n🧙 {npc.nombre} ({npc.dificultad}) te dice: {npc.acertijo}")
                
                # Mostrar información específica según el tipo de NPC
                if isinstance(npc, NPCDificil):
                    print(npc.mostrar_advertencia())
                elif isinstance(npc, NPCFacil):
                    print("💚 NIVEL FÁCIL - Tienes tiempo suficiente para pensar")
                elif isinstance(npc, NPCMedio):
                    print("💛 NIVEL MEDIO - No te tomes demasiado tiempo")
                    
                print(f"⏳ Tienes {npc.tiempo_limite} segundos para responder.")
                
                # Ofrecer pista para NPCs fáciles
                if isinstance(npc, NPCFacil):
                    pista = input("¿Quieres una pista? (s/n): ").lower()
                    if pista == 's':
                        print(npc.mostrar_pista())
                
                inicio = time.time()
                respuesta = input("💬 Tu respuesta: ")
                tiempo_transcurrido = time.time() - inicio
                
                # Verificar tiempo límite
                if tiempo_transcurrido > npc.tiempo_limite:
                    print("⏱️ ¡Se acabó el tiempo!")
                else:
                    # Penalización para NPCs medios
                    if isinstance(npc, NPCMedio):
                        npc.penalizacion_tiempo(tiempo_transcurrido)
                    
                    # Verificar respuesta usando el método específico de cada clase
                    if npc.verificar_respuesta(respuesta):
                        print("✅ ¡Correcto!")
                        npc.resuelto = True
                        self.jugador.acertijos_resueltos += 1
                        
                        # Mensaje especial para NPCs difíciles
                        if isinstance(npc, NPCDificil):
                            print("🎯 ¡Excelente! Has superado el desafío más difícil.")
                    else:
                        print("❌ Incorrecto.")
                        
                        # Mostrar información adicional según el tipo
                        if isinstance(npc, NPCDificil) and npc.intentos_fallidos >= 2:
                            print("💀 Este NPC será más difícil la próxima vez...")
                        elif isinstance(npc, NPCFacil):
                            print("💚 No te preocupes, puedes intentarlo de nuevo.")
                
                time.sleep(2)
                return
                
        print("🤔 No hay nadie con quien interactuar.")
        time.sleep(1)

    def mostrar_estadisticas(self):
        """Muestra estadísticas detalladas del progreso"""
        print("\n📊 ESTADÍSTICAS:")
        for npc in self.npcs:
            estado = "✅ Resuelto" if npc.resuelto else "❌ Pendiente"
            print(f"  {npc.dificultad}: {npc.nombre} - {estado}")

    def jugar(self):
        print("🎮 ¡Bienvenido al Juego de Acertijos!")
        print("Los NPCs tienen diferentes niveles de dificultad:")
        print("💚 Fácil: Más tiempo, pistas disponibles")
        print("💛 Medio: Tiempo moderado, penalización por tardanza")
        print("🔴 Difícil: Poco tiempo, muy estricto")
        input("\nPresiona ENTER para comenzar...")
        
        while self.jugador.acertijos_resueltos < len(self.npcs):
            self.dibujar_mapa()
            comando = input("🎮 Mueve (WASD), interactúa (E) o estadísticas (T): ").lower()
            
            if comando in ["w", "a", "s", "d"]:
                self.mover_jugador(comando)
            elif comando == "e":
                self.interactuar()
            elif comando == "t":
                self.mostrar_estadisticas()
                input("Presiona ENTER para continuar...")
                
        self.dibujar_mapa()
        print("\n🎉 ¡Has resuelto todos los acertijos y restaurado el universo!")
        self.mostrar_estadisticas()
        input("Presiona ENTER para salir.")

# Ejecutar el juego
if __name__ == "__main__":
    juego = JuegoAcertijosConsola()
    juego.jugar()
    