import os
os.system ("cls")
'''
edad = 18
if (edad >=18):
    print ("es mayor de 18")
else:
    print("es menor de edad")

#---------------------------------------

edad = 20
if edad < 18 and edad >0:
    print ("niños")
elif edad >= 18 and edad <=35:
    print ("pos adolencentes")
elif edad >= 18 and edad <=35:
    print ("pos adolencentes")
elif edad > 35 and edad <=60:
    print ("adultos")
else:
    print ("adultos mayores")
'''
#----------------------------------

A = float(input("ingrese el valor de A: "))
B= float(input("ingrese el valor de B: "))
operador= (input("ingrese el operador "))


if operador == "+":
    print (A, "+", B, "es igual a: ", A+B)
elif operador == "-":
    print (A, "-", B, "es igual a: ", A-B)
elif operador == "*":
    print (A, "*", B, "es igual a: ", A*B)
elif operador == "/":
    if B > 0:
        print (A, "/", B, "es igual a: ", A/B)
    else:
        print ("no se puede dividir por 0")
else:
    print ("error de operacion")