**Teoría Detallada por Tema**

### Tema 1: Operaciones con tipos de datos y operadores
1. **Tipos de Datos:**
   - `str`: Cadenas de texto, representadas entre comillas simples o dobles. Ejemplo: `'Hola'`, `"Python"`.
   - `int`: Números enteros, como `42` o `-7`.
   - `float`: Números con decimales, como `3.14` o `-0.001`.
   - `bool`: Valores lógicos, `True` o `False`, utilizados para decisiones y condiciones.

2. **Operaciones con Datos:**
   - **Conversión de Tipos:** Cambiar entre tipos de datos usando funciones como `int()`, `float()`, `str()`, etc. Ejemplo: convertir un string a entero con `int("123")`.
   - **Indexación y Slicing:** Acceso a elementos individuales o partes de secuencias (listas, cadenas). Indexación empieza desde 0.

3. **Operadores:**
   - **Aritméticos:** Realizan operaciones matemáticas.
     - `+`: Suma.
     - `-`: Resta.
     - `*`: Multiplicación.
     - `/`: División.
     - `//`: División entera (redondea hacia abajo).
     - `%`: Módulo (resto de una división).
     - `**`: Potenciación.
   - **Comparación:** Devuelven un valor booleano (`True` o `False`).
     - `==`: Igual a.
     - `!=`: Distinto de.
     - `>`: Mayor que.
     - `<`: Menor que.
     - `>=`: Mayor o igual que.
     - `<=`: Menor o igual que.
   - **Lógicos:** Combina o invierte condiciones.
     - `and`: Devuelve `True` si ambas condiciones son verdaderas.
     - `or`: Devuelve `True` si al menos una condición es verdadera.
     - `not`: Invierte el valor de verdad.
   - **De Asignación:** Asignan valores a variables.
     - `=`: Asignación simple.
     - `+=`: Suma y asigna.
     - `-=`: Resta y asigna.

4. **Precedencia de Operadores:**
   - El orden de ejecución está definido por la precedencia. Ejemplo: multiplicación y división tienen mayor precedencia que suma y resta.
   - Paréntesis pueden usarse para alterar la precedencia.

---

### Tema 2: Control de flujo con decisiones y bucles
1. **Sentencias Condicionales:**
   - Permiten ejecutar diferentes bloques de código dependiendo de una condición.
     - `if`: Ejecuta el bloque si la condición es verdadera.
     - `elif`: Evalúa una nueva condición si las anteriores son falsas.
     - `else`: Se ejecuta si ninguna de las condiciones anteriores es verdadera.

2. **Bucles:**
   - **`for`:** Itera sobre una secuencia (listas, cadenas, etc.).
   - **`while`:** Ejecuta un bloque de código mientras una condición sea verdadera.
   - **Control de flujo dentro de bucles:**
     - `break`: Termina el bucle inmediatamente.
     - `continue`: Salta a la siguiente iteración.
     - `pass`: No realiza ninguna acción, sirve como marcador de lugar.

---

### Tema 3: Operaciones de entrada y salida
1. **Archivos:**
   - `open()`: Abre un archivo.
     - Modos: `'r'` (lectura), `'w'` (escritura, sobrescribe), `'a'` (adjuntar).
   - `read()`: Lee el contenido del archivo.
   - `write()`: Escribe datos en el archivo.
   - `close()`: Cierra el archivo.
   - Verificar existencia con `os.path.exists()`.

2. **Consola:**
   - `input()`: Solicita datos al usuario desde el teclado.
   - `print()`: Muestra datos en la consola.
   - Formatos avanzados:
     - `string.format()`: Formatea cadenas.
     - `f-strings`: Usan expresiones directamente dentro de cadenas (Python 3.6+).

---

### Tema 4: Documentación y estructura del código
1. **Comentarios y Docstrings:**
   - **Comentarios:** Usan `#` para explicar partes del código.
   - **Docstrings:** Se utilizan para documentar funciones, clases o módulos. Rodeados de triple comillas (`"""`).

2. **Funciones:**
   - **Definición:** Se crean usando `def` seguido del nombre y paréntesis.
   - **Parámetros por defecto:** Se pueden asignar valores predeterminados a los parámetros.
   - **Retorno de valores:** Usa `return` para devolver resultados.

---

### Tema 5: Depuración y manejo de errores
1. **Tipos de Errores:**
   - **Sintaxis:** Errores de escritura que impiden la ejecución.
   - **Lógica:** El código se ejecuta, pero no produce el resultado esperado.
   - **Ejecución:** Ocurren mientras el programa está corriendo, como dividir entre cero.

2. **Manejo de Excepciones:**
   - Bloques clave:
     - `try`: Contiene el código que puede generar una excepción.
     - `except`: Captura y maneja la excepción.
     - `else`: Opcional, ejecuta si no hay excepción.
     - `finally`: Opcional, siempre se ejecuta.

---

### Tema 6: Uso de módulos y herramientas
1. **Módulos Comunes:**
   - **`os`:** Proporciona funciones para interactuar con el sistema operativo (crear, eliminar directorios, listar archivos, etc.). Ejemplo: `os.listdir()` para listar archivos en un directorio.
   - **`sys`:** Permite acceder a parámetros del sistema y manejar argumentos de la línea de comandos. Ejemplo: `sys.argv` para acceder a argumentos.
   - **`math`:** Incluye funciones matemáticas avanzadas como `sqrt()` (raíz cuadrada), `pow()` (potenciación), `fabs()` (valor absoluto).
   - **`datetime`:** Proporciona herramientas para trabajar con fechas y horas. Ejemplo: `datetime.now()` devuelve la fecha y hora actual.
   - **`random`:** Genera valores aleatorios. Ejemplo: `random.choice()` selecciona un elemento al azar de una lista.

2. **Operaciones Específicas:**
   - **Sistema de Archivos y Línea de Comandos:**
     - `os.path.exists(ruta)`: Verifica si un archivo o directorio existe.
     - `sys.argv`: Obtiene argumentos pasados por línea de comandos.
   - **Cálculos Matemáticos:**
     - `math.ceil(numero)`: Redondea al entero más cercano hacia arriba.
     - `math.floor(numero)`: Redondea hacia abajo.
     - `math.pi`: Proporciona el valor de pi.
   - **Fechas y Horas:**
     - `datetime.strftime(formato)`: Convierte una fecha en un string con el formato deseado.
     - `datetime.weekday()`: Devuelve el día de la semana (0 es lunes).
   - **Generación Aleatoria:**
     - `random.randint(a, b)`: Genera un entero aleatorio entre `a` y `b`.
     - `random.shuffle(lista)`: Mezcla aleatoriamente los elementos de una lista.

---
