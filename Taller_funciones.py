import os
os.system ("cls")


# 1. Escriba una función que muestre por consola un saludo personalizado. Por ejemplo ‘¡Hola mundo!’

print("¿como quieres que te llamemos?")

def saludo(hoola):
    resultado = hoola
    return resultado
saludo_per = str(input("ingresa como quieres que te llamemos: "))

print("Hola", saludo(saludo_per))

#2. Escriba una función que reciba un nombre por parámetro y que luego muestre en pantalla ¡Hola <nombre>!

def nombre(Nombre):
    result= Nombre
    return result
saludo_ = str(input("ingresa su nombre: "))

print("Buenos dias", nombre(saludo_))

#3. Cree una función que le pida al usuario su nombre y su edad, luego muestre en pantalla los resultados

def datos(pers):
    result= pers
    return result
Nombre = str(input("ingresa su nombre: "))
edad = int(input("ingresa que edad tienes: "))

print("tu nombre es", datos(Nombre), "y tu edad es", datos(edad))

#4. Definir una función que reciba n cantidad de números por parámetros y que luego los sume, reste, mutiplique y divida.

