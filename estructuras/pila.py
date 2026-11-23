
class Pila:

    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def cima(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0
