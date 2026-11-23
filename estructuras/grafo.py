
class Grafo:

    def __init__(self):
        self.conexiones = {}

    def agregar_area(self, area):
        if area not in self.conexiones:
            self.conexiones[area] = []

    def conectar(self, area1, area2):
        self.agregar_area(area1)
        self.agregar_area(area2)

        if area2 not in self.conexiones[area1]:
            self.conexiones[area1].append(area2)

        if area1 not in self.conexiones[area2]:
            self.conexiones[area2].append(area1)

    def mostrar(self):
        return self.conexiones
