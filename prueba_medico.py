
from modulos.medicos import Medicos

sistema = Medicos()

# Registrar médicos
sistema.registrar(1, "Ana López", "Pediatría", "88881111")
sistema.registrar(2, "Pedro Ruiz", "Cardiología", "88882222")

# Mostrar médicos
print("LISTA DE MÉDICOS:")
print(sistema.mostrar())

# Buscar médico
print("\nBUSCAR MÉDICO:")
print(sistema.buscar(1))

# Eliminar médico
sistema.eliminar(2)

print("\nLISTA ACTUALIZADA:")
print(sistema.mostrar())
