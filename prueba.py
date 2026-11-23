
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.pila import Pila
from estructuras.cola import Cola
from estructuras.grafo import Grafo

# Probar lista enlazada
pacientes = ListaEnlazada()

pacientes.agregar({
    "id": 1,
    "nombre": "Carlos"
})

print("PACIENTES:")
print(pacientes.mostrar())

# Probar pila
historial = Pila()
historial.apilar("Paciente registrado")

print("\nHISTORIAL:")
print(historial.cima())

# Probar cola
turnos = Cola()
turnos.encolar("Carlos")
turnos.encolar("Maria")

print("\nSIGUIENTE TURNO:")
print(turnos.desencolar())

# Probar grafo
hospital = Grafo()
hospital.conectar("Emergencias", "Laboratorio")

print("\nAREAS:")
print(hospital.mostrar())
