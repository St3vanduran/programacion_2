import os
os.system ("cls")

def Multiplicacion():
    num1 = input('*')
    nume = num1.split("*")  
    a = 1
    for x in nume:
        a *= int(x)
    print(a)

def división():
    num2 = input('/')
    numeros2 = num2.split("/")  
    b = 1
    for x in numeros2:
        b /= int(x)
    print(b)

def suma():
    num3 = input('+')
    numeros3 = num3.split("+")  
    c = 0
    for x in numeros3:
        c += int(x)
    print(c)

def resta():
    num4 = input('-')
    numeros4 = num4.split("-")  
    d = 0
    for x in numeros4:
        d -= int(x)
    print(d)

problema =input ("escriba la operacion: ")
problema = list(problema)

for x in range (len(problema)):
    if "*" in problema:
        Multiplicacion()
    
    elif "/" in problema:
        división()

    elif "+" in problema:
        suma()
    
    elif "-" in problema:
        resta()

print()
print("el resultado de la operacion es: ")
print()
os.system('pause')
os.system('cls')