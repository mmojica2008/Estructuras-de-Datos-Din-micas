
from modulos.pacientes import Pacientes

sistema = Pacientes()

# Registrar pacientes
sistema.registrar(1, "Carlos", 25, "8888-1111")
sistema.registrar(2, "María", 30, "8888-2222")

# Mostrar pacientes
print("LISTA DE PACIENTES:")
print(sistema.mostrar())

# Buscar paciente
print("\nBUSCAR PACIENTE:")
print(sistema.buscar(1))

# Eliminar paciente
sistema.eliminar(2)

print("\nLISTA ACTUALIZADA:")
print(sistema.mostrar())
