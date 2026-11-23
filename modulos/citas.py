
from estructuras.cola import Cola


class Citas:

    def __init__(self):
        self.cola = Cola()

    def registrar(self, identificacion, paciente, medico, fecha, hora):
        cita = {
            "id": identificacion,
            "paciente": paciente,
            "medico": medico,
            "fecha": fecha,
            "hora": hora,
            "estado": "Pendiente"
        }

        self.cola.encolar(cita)
        return cita

    def mostrar(self):
        return self.cola.mostrar()

    def buscar(self, identificacion):
        for cita in self.cola.mostrar():
            if cita["id"] == identificacion:
                return cita
        return None

    def atender(self):
        cita = self.cola.desencolar()

        if cita is not None:
            cita["estado"] = "Atendida"

        return cita

    def eliminar(self, identificacion):
        citas = self.cola.mostrar()

        self.cola.elementos = [
            cita for cita in citas
            if cita["id"] != identificacion
        ]
