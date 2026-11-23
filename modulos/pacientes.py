
from estructuras.lista_enlazada import ListaEnlazada


class Pacientes:
    def __init__(self):
        self.lista = ListaEnlazada()

    def registrar(self, identificacion, nombre, edad, telefono):
        paciente = {
            "id": identificacion,
            "nombre": nombre,
            "edad": edad,
            "telefono": telefono
        }

        self.lista.agregar(paciente)
        return paciente

    def mostrar(self):
        return self.lista.mostrar()

    def buscar(self, identificacion):
        return self.lista.buscar(identificacion)

    def eliminar(self, identificacion):
        return self.lista.eliminar(identificacion)