"""
Indexación y Slicing
"""
lista = [10,20,30,40,50,60,70,80,90]

"""
Se pueden poner numeros negativos, lo que invertirá la palabra
Ejemplo:
p = Python
print(p[::-1])

OUTPUT: nohtyP
"""

# Muestra el item numero 7 de la lista
print(lista[7])

# Muestran los primeros 3 items de la lista
print(lista[:3])

# Muestra los items del 5 al 10
print(lista[5:10])

# Muestra los items saltando de 1 en 1 (cambiando el numero hace mas saltos)
print(lista[::2]) # Ej: si ponemos 5 y no 2, hará del 10 al 60
