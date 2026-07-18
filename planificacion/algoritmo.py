class Algoritmo:
    def __init__(self, idle, Tiempo_de_espera_promedio, Tiempo_de_respuesta_promedio):
        self.idle = idle
        self.Tiempo_de_espera_promedio = Tiempo_de_espera_promedio
        self.Tiempo_de_respuesta_promedio = Tiempo_de_respuesta_promedio
        self.tipo_de_algoritmo = None