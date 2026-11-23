
class Cola:

    def __init__(self):
        self.elementos = []

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def mostrar(self):
        return self.elementos

    def esta_vacia(self):
        return len(self.elementos) == 0
