
from flask import Flask, render_template, request, redirect

from modulos.pacientes import Pacientes
from modulos.medicos import Medicos
from modulos.habitaciones import Habitaciones
from modulos.citas import Citas


app = Flask(__name__)

sistema_pacientes = Pacientes()
sistema_medicos = Medicos()
sistema_habitaciones = Habitaciones()
sistema_citas = Citas()


# PANEL PRINCIPAL
@app.route("/")
def inicio():
    return render_template(
        "index.html",
        pacientes=sistema_pacientes.mostrar(),
        medicos=sistema_medicos.mostrar(),
        habitaciones=sistema_habitaciones.mostrar(),
        citas=sistema_citas.mostrar()
    )


# PACIENTES
@app.route("/registrar_paciente", methods=["POST"])
def registrar_paciente():
    identificacion = int(request.form["id"])
    nombre = request.form["nombre"]
    edad = int(request.form["edad"])
    telefono = request.form["telefono"]

    sistema_pacientes.registrar(
        identificacion, nombre, edad, telefono
    )

    return redirect("/")


@app.route("/eliminar_paciente/<int:identificacion>", methods=["POST"])
def eliminar_paciente(identificacion):
    sistema_pacientes.eliminar(identificacion)
    return redirect("/")


# MEDICOS
@app.route("/registrar_medico", methods=["POST"])
def registrar_medico():
    identificacion = int(request.form["id"])
    nombre = request.form["nombre"]
    especialidad = request.form["especialidad"]
    telefono = request.form["telefono"]

    sistema_medicos.registrar(
        identificacion, nombre, especialidad, telefono
    )

    return redirect("/")


@app.route("/eliminar_medico/<int:identificacion>", methods=["POST"])
def eliminar_medico(identificacion):
    sistema_medicos.eliminar(identificacion)
    return redirect("/")


# HABITACIONES
@app.route("/registrar_habitacion", methods=["POST"])
def registrar_habitacion():
    numero = int(request.form["numero"])
    tipo = request.form["tipo"]

    sistema_habitaciones.registrar(numero, tipo)

    return redirect("/")


@app.route("/cambiar_estado_habitacion/<int:numero>", methods=["POST"])
def cambiar_estado_habitacion(numero):
    sistema_habitaciones.cambiar_estado(numero)
    return redirect("/")


@app.route("/eliminar_habitacion/<int:numero>", methods=["POST"])
def eliminar_habitacion(numero):
    sistema_habitaciones.eliminar(numero)
    return redirect("/")


# CITAS MEDICAS
@app.route("/registrar_cita", methods=["POST"])
def registrar_cita():
    identificacion = int(request.form["id"])
    paciente = request.form["paciente"]
    medico = request.form["medico"]
    fecha = request.form["fecha"]
    hora = request.form["hora"]

    sistema_citas.registrar(
        identificacion, paciente, medico, fecha, hora
    )

    return redirect("/")


@app.route("/atender_cita", methods=["POST"])
def atender_cita():
    sistema_citas.atender()
    return redirect("/")


@app.route("/eliminar_cita/<int:identificacion>", methods=["POST"])
def eliminar_cita(identificacion):
    sistema_citas.eliminar(identificacion)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
