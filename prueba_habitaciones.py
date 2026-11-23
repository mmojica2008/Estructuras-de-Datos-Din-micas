
from modulos.habitaciones import Habitaciones

sistema = Habitaciones()

sistema.registrar(101, "Individual")
sistema.registrar(102, "Compartida")
sistema.registrar(103, "UCI")

print("HABITACIONES REGISTRADAS:")
print(sistema.mostrar())

sistema.cambiar_estado(101)

print("\nDESPUÉS DE CAMBIAR EL ESTADO:")
print(sistema.mostrar())
