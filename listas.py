import os
os.system ("cls")

varlista = ['pablo', True, 5.5, 9]

"""
print(varlista[0])
print(varlista[1])
print(varlista[2])
print(varlista[3])
"""

"""for z in varlista:
    print(z)

q = 0

while q < len (varlista):
    print(varlista[0])
    q = +1   """

"del" #elimina cosas de la lista
"varlista.insert(1, cual )" # agrega elementos a la lista donde hay que darle la posicion y objeto

# del varlista [0]
varlista.insert(1, 'cual?')
varlista.append('USCO')
# varlista.append(input("INSERTE UN NUMERO: "))

# for z in varlista:
#    print(z)

Eliminar = input ("digite el valor a eliminar: ")
contador = 0

for z in varlista:
    if Eliminar == z:
        del varlista[contador]
    else:
        contador +=1

print(varlista)

datos = [['hector', 'sanchez', '36'], ['Marria', 'Lugo', 28], ['juan', 'silva', 17]]

for w in datos:
    print(w)

for z in datos:
    for u in z:
        print(u)
    print("--------------")

# diccionario