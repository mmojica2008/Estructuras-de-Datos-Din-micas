
from estructuras.lista_enlazada import ListaEnlazada


class Medicos:
    def __init__(self):
        self.lista = ListaEnlazada()

    def registrar(self, identificacion, nombre, especialidad, telefono):
        medico = {
            "id": identificacion,
            "nombre": nombre,
            "especialidad": especialidad,
            "telefono": telefono
        }

        self.lista.agregar(medico)
        return medico

    def mostrar(self):
        return self.lista.mostrar()

    def buscar(self, identificacion):
        return self.lista.buscar(identificacion)

    def eliminar(self, identificacion):
        return self.lista.eliminar(identificacion)
