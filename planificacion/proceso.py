class Proceso:
    def __init__(self, id, llegada, rafaga, prioridad):
        self.id = id
        self.llegada = llegada
        self.rafaga = rafaga
        self.prioridad = prioridad
        self.Trestante = rafaga
        self.inicio = None
        self.fin = None
        self.Tretorno= None
        self.Tespera = None 