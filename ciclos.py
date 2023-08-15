import os
os.system ("cls")

"""
#while

varcontrol = 1

while varcontrol <= 10:
    print(varcontrol)
    varcontrol +=1

listado = ['juan', 'pedro', 'maria', 'sofia']

b = 0 

while b < len(listado): # len tamaño del vector
    print(listado[b]) # b vale 4 por el numero de nombres en el listado
    b +=1
"""

#ciclo for

frutas = ['limon','fresa','pera', 'manzana']

for i in frutas:
    print(i)

print("-----------------------")

for a in range(10): #imprime hasta el rango indicado
    print(a)

print("-----------------------")

for a in range(2, 20, 2): #inicio, la condicion y el salto impriendo un rango con saltos 
    print(a)