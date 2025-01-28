"""
Ejercicio 2: Indexación y Slicing
Dada la cadena de texto:
`frase = "Aprender Python es divertido y útil"`

1. Obtén el carácter en la posición 10.
2. Extrae la palabra "Python" utilizando slicing.
3. Invierte toda la cadena (usa slicing).

"""

frase = "Aprender Python es divertido y útil"

print(frase[9]) # Como empieza por 0 ponemos uno menos

print(frase[9:15]) # Cojemos la palabra "Python"

print(frase[::-1])
