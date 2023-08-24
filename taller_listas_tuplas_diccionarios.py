import os
os.system ("cls")

"""1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas.
Luego muestre la lista por consola mediante un ciclo."""

print("para salir del programa diguite salir")

materias_vistas = []

while True:
    print()
    materias = input("Materias vistas: ")
    print()
    if materias.lower() == "salir":
        break
    notas = float(input("ingrese las notas: "))
    materias_vistas.append((materias,notas))
print()
print("lista de materias y notas: ")
for materias, notas in materias_vistas:
    print(f"{materias}: {notas}")

print("----------------------------------------------------------------")

"""2. Escriba un programa que almacene personas (input), luego que le muestre 
por pantalla el mensaje de Su nombre es nombre"""

print("para salir del programa diguite salir")

nombres = []

while True:
    print()
    nombre_personal = input("ingrese su nombre: ")
    print()
    if nombre_personal.lower() == "salir":
        break
    nombres.append((nombre_personal))
print()
print("los nombres guardados son los siguentes: ")
for nombre_personal in nombres:
    print(f"{nombre_personal}")

print("------------------------------------------------")

"""3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en el diccionario."""

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in divisas:
    print(divisas[moneda.title()])
else:
    print("La divisa no está.")


print("-----------------------------------------------")

"""4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados."""

tupla = (123, 3.14, "Hola", [1, 2, 3], {"a": 1, "b": 2})

for a in tupla:
    print(f"El valor {a} es de tipo {type(a).__name__}")