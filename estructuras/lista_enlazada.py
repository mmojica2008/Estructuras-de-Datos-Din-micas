
from estructuras.nodo import Nodo


class ListaEnlazada:

    def __init__(self):
        self.inicio = None

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.inicio is None:
            self.inicio = nuevo
        else:
            actual = self.inicio

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

    def mostrar(self):
        datos = []
        actual = self.inicio

        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente

        return datos

    def buscar(self, identificacion):
        actual = self.inicio

        while actual is not None:
            if actual.dato["id"] == identificacion:
                return actual.dato

            actual = actual.siguiente

        return None

    def eliminar(self, identificacion):
        actual = self.inicio
        anterior = None

        while actual is not None:
            if actual.dato["id"] == identificacion:

                if anterior is None:
                    self.inicio = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                return True

            anterior = actual
            actual = actual.siguiente

        return False
