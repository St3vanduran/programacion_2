#crear una clase ya sea con una lista/diccionario con 10 personas con nombre apellido edad telefono y crear una funcion random que
#selecione que casa a la de grifindor o slytherin van a ir (todos los datos deben ser ingresados, no puede haber datos guarados)

import os
import random
os.system ("cls")


class estudiante:
    def __init__(self,nombre,apellido,edad,telefono):
        self.nombre = nombre
        self.apellido =apellido
        self.edad = edad
        self.telefono = telefono
        self.casa = self.asignar_casa()

    def asignar_casa(self):
        casas = ["Grifindor", "Slytherin"]
        return random.choice(casas)
    

estudiantes = []

while True:
    print()
    nombre = input("ingrese el nombre del estudiante: ")
    if nombre.lower() == "salir":
        break
    apellido = str(input("ingrese su apellido: "))
    edad = float(input("ingrese su edad:"))
    telefono = float(input("ingrese su telefono: "))
    persona = estudiante(nombre, apellido, edad, telefono)
    estudiantes.append(persona)

for i, persona in enumerate(estudiantes):
    print("\nInformación de la persona: ")
    print("Nombre: ", persona.nombre)
    print("Apellido: ", persona.apellido)
    print("Edad: ", persona.edad)
    print("Teléfono: ", persona.telefono)
    print("Casa asignada: ", persona.casa)
print()