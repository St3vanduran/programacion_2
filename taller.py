import os
os.system ("cls")

"""
1 Escriba un programa que almacene la cadena de caracteres contraseña en una 
variable, para luego preguntarle al usuario por la contraseña. 
Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con 
la guardada en variable. """

contraseña = "contraseña"

ingrese_contraseña = input ('ingrese la contraseña: ')

iguales = True

for i in range(len(contraseña)):
    if ingrese_contraseña[i] != contraseña[i]:
        iguales = False

if iguales:
    print("La contraseña es correcta.")

else:
    print("La contraseña es incorrecta.")

print()
print()
print()

#2. Realice un programa que le pida al usuario dos números por teclado y muestre por 
# consola su división. Si el divisor es cero el programa debe mostrar un error y solicitar
#nuevamente el numero.

A = float(input("ingrese el primer numero para la division: "))
B = float(input("ingrese el segundo numero para la division: "))

if B == 0:
    print("el 2do numero no se puede dividir por cero")

else:
    division = A/ B
    print("El resultado de la división es:", {division})

print()
print()
print()


#3. Escriba un programa que le pida al usuario por teclado un numero entero y 
# muestre en consola si es par o impar.

print ("por favor ingrese un numero entero")
entero = int(input("que numero desea ingresar: "))

if entero + 2 == 1:
        print("El número es par.")
else:
        print("El número es impar.")

print()
print()
print()


#4. Escriba que mediante un vector  de 5 item, lea cada item y evalué el ingreso a menores de 
# edad, si la persona tiene menos de 19 años el programa le debe mostrar 
#en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!

edad =[21, 23, 17, 25, 9]

for i in edad:
    if i < 19:
        print('es menor de edad')
    else:
        print('es mayor de edad')