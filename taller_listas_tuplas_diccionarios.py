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


valores = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

euro = 2500
dolar= 3000
yen= 3000


print('desea pasar de pesos a?')
print('1. euro')
print('2. dolar')
print('3. yen')
print()

pasar= float(input('ingrese los pesos colobianos que desea pasar: '))
divis= int(input('A que divisa lo desea convertir: '))

if divis == 1:
    res= pasar / euro
    print(valores['Euro'], res)
elif divis == 2:
    res = pasar / dolar
    print(valores['Dollar'], res)
elif divis == 3:
    res = pasar / yen
    print(valores['Yen'], res)


print("-----------------------------------------------")

"""4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados."""

tupla = (123, 3.14, "Hola", [1, 2, 3], {"a": 1, "b": 2})

for a in tupla:
    print(f"El valor {a} es de tipo {type(a).__name__}")