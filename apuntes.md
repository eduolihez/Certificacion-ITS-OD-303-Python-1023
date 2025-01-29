## **Tema 1: Operaciones con Tipos de Datos y Operadores**

### **1. Tipos de Datos Básicos**
- **`str` (string):**
  - Secuencia inmutable de caracteres. Ejemplo: `"Hola"`, `'Python'`.
  - Operaciones comunes: concatenación (`+`), repetición (`*`), longitud (`len()`).
- **`int` (entero):**
  - Números sin decimales. Ejemplo: `42`, `-7`.
  - Límites: dependen de la memoria.
- **`float` (flotante):**
  - Números con decimales. Ejemplo: `3.14`, `-0.001`.
  - Precisión: puede haber errores de redondeo (ej: `0.1 + 0.2 = 0.30000000000000004`).
- **`bool` (booleano):**
  - Valores `True` o `False`.
  - Se usan en condiciones y operaciones lógicas.

### **2. Conversión de Tipos**
- **Funciones clave:**
  - `int()`: Convierte a entero. Ejemplo: `int("123") → 123`.
  - `float()`: Convierte a flotante. Ejemplo: `float(5) → 5.0`.
  - `str()`: Convierte a string. Ejemplo: `str(3.14) → "3.14"`.
  - `bool()`: Evalúa si un valor es verdadero o falso (0, `""`, `None` son `False`).

### **3. Operaciones con Secuencias**
- **Indexación:**
  - Acceso a elementos: `cadena[0]` (primer carácter).
  - Índices negativos: `cadena[-1]` (último carácter).
- **Slicing:**
  - Sintaxis: `[inicio:fin:paso]`.
  - Ejemplo: `"Python"[2:4] → "th"`.

### **4. Operadores**
- **Aritméticos:**
  - `//`: División entera (`7 // 2 → 3`).
  - `%`: Módulo (resto de división: `7 % 2 → 1`).
  - `**`: Potencia (`2 ** 3 → 8`).
- **Comparación:**
  - `==`, `!=`, `>`, `<`, `>=`, `<=`.
  - Se pueden encadenar: `1 < x <= 5`.
- **Lógicos:**
  - `and`: `True` si ambos operandos son `True`.
  - `or`: `True` si al menos uno es `True`.
  - `not`: Invierte el valor (`not True → False`).
- **Asignación:**
  - `=`, `+=`, `-=`, `*=`, etc. Ejemplo: `x += 5` equivale a `x = x + 5`.

### **5. Precedencia de Operadores**
1. Paréntesis `()`.
2. Potencia `**`.
3. Multiplicación `*`, División `/`, Módulo `%`.
4. Suma `+`, Resta `-`.
5. Comparación (`<`, `>`, etc.).
6. Operadores lógicos: `not`, `and`, `or`.

---

## **Tema 2: Control de Flujo con Decisiones y Bucles**

### **1. Condicionales**
```python
# Ejecuta el bloque si la condición es verdadera.
if condicion1: 
# Evalúa una nueva condición si las anteriores son falsas.
elif condicion2:
# Se ejecuta si ninguna de las condiciones anteriores es verdadera.
else:
```

### **2. Bucles**
- **`for`:** Itera sobre elementos de una secuencia.
  ```python
  for i in range(5):  # 0, 1, 2, 3, 4
      print(i)
  ```
- **`while`:** Ejecuta mientras una condición sea `True`.
  ```python
  n = 0
  while n < 5:
      print(n)
      n += 1
  ```

### **3. Control de Bucles**
- **`break`:** Termina el bucle.
  ```python
  for i in range(10):
      if i == 5:
          break  # Sale del bucle
  ```
- **`continue`:** Salta a la siguiente iteración.
  ```python
  for i in range(5):
      if i == 2:
          continue  # Salta la iteración actual
      print(i)
  ```
- **`pass`:** Marca una posición sin código (útil para estructuras vacías).

---

## **Tema 3: Operaciones de Entrada y Salida**

### **1. Archivos**
- **Abrir y cerrar:**
  ```python
  archivo = open("archivo.txt", "r")  # Modos: 'r' (lectura), 'w' (escritura), 'a' (añadir)
  contenido = archivo.read()  # Lee todo el contenido
  archivo.close()
  ```
- **Manejo seguro con `with`:**
  ```python
  with open("archivo.txt", "r") as archivo:
      lineas = archivo.readlines()  # Lista de líneas
  ```

### **2. Consola**
- **Entrada:**
  ```python
  nombre = input("Ingresa tu nombre: ")  # Devuelve un string
  ```
- **Salida formateada:**
  - **`f-strings` (recomendado):**
    ```python
    edad = 25
    print(f"Tienes {edad} años.")
    ```
  - **`.format()`:**
    ```python
    print("Tienes {} años.".format(edad))
    ```

---

## **Tema 4: Documentación y Estructura del Código**

### **1. Comentarios y Docstrings**
- **Comentarios de una línea:**
  ```python
  # Esto es un comentario
  ```
- **Docstrings (documentación):**
  ```python
  def suma(a, b):
      """Suma dos números y devuelve el resultado."""
      return a + b
  ```

### **2. Funciones**
- **Parámetros por defecto:**
  ```python
  def saludar(nombre="Usuario"):
      print(f"Hola, {nombre}!")
  ```
- **Retorno múltiple:**
  ```python
  def operaciones(a, b):
      return a + b, a - b  # Devuelve una tupla
  ```

---

## **Tema 5: Depuración y Manejo de Errores**

### **1. Tipos de Errores**
- **Sintaxis:** `SyntaxError` (ej: `print("Hola"` sin cerrar paréntesis).
- **Ejecución:** `ZeroDivisionError`, `TypeError`, `FileNotFoundError`.

### **2. Manejo de Excepciones**
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
else:
    print("Todo funcionó bien.")
finally:
    print("Este bloque siempre se ejecuta.")
```

---

## **Tema 6: Módulos y Herramientas**

### **1. Módulos Comunes**
- **`math`:**
  ```python
  import math
  print(math.sqrt(25))  # 5.0
  ```
- **`datetime`:**
  ```python
  from datetime import datetime
  fecha = datetime.now()
  print(fecha.strftime("%d/%m/%Y"))  # Formato: 21/10/2023
  ```
- **`random`:**
  ```python
  import random
  print(random.randint(1, 10))  # Número aleatorio entre 1 y 10
  ```

### **2. Argumentos de Línea de Comandos**
```python
import sys
print("Argumentos recibidos:", sys.argv)  # Ejemplo: python script.py arg1 arg2
```

---

## **Consejos para el Examen**
1. **Práctica con Ejercicios:** Resuelve problemas que involucren todos los temas.
2. **Repasa Excepciones Comunes:** Como `IndexError` o `KeyError`.
3. **Usa la Documentación Oficial:** Es clave para entender módulos estándar.
4. **Domina el Manejo de Archivos:** Es un tema frecuente en certificaciones.