
from estructuras.lista_enlazada import ListaEnlazada


class Habitaciones:
    def __init__(self):
        self.lista = ListaEnlazada()

    def registrar(self, numero, tipo):
        habitacion = {
            "id": numero,
            "numero": numero,
            "tipo": tipo,
            "estado": "Disponible"
        }

        self.lista.agregar(habitacion)
        return habitacion

    def mostrar(self):
        return self.lista.mostrar()

    def buscar(self, numero):
        return self.lista.buscar(numero)

    def cambiar_estado(self, numero):
        habitacion = self.buscar(numero)

        if habitacion is not None:
            if habitacion["estado"] == "Disponible":
                habitacion["estado"] = "Ocupada"
            else:
                habitacion["estado"] = "Disponible"

            return True

        return False

    def eliminar(self, numero):
        return self.lista.eliminar(numero)
