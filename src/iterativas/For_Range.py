# Este programa demuestra el uso de bucles for y range en Python

# Ejemplo 1: Recorrer una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# EXPLICACIÓN:
# Se define una lista llamada "frutas" con tres elementos.
# El bucle for recorre la lista automáticamente elemento por elemento.
# En cada iteración, la variable "fruta" toma el valor de un elemento distinto.
# Primero "manzana", luego "banana" y finalmente "cereza".
# En cada vuelta se imprime el valor actual.


# Ejemplo 2: Uso básico de range()
for i in range(5):
    print(i)

# EXPLICACIÓN:
# range(5) genera una secuencia de números desde 0 hasta 4.
# El 5 no se incluye.
# El bucle for recorre esos valores y los imprime uno por uno.


# Ejemplo 3: range con inicio y fin
for i in range(3, 8):
    print(i, end=" ")

# EXPLICACIÓN:
# range(3, 8) genera números desde 3 hasta 7.
# El segundo valor (8) no se incluye.
# Se usa end=" " para imprimir los valores en la misma línea separados por espacio.


# Ejemplo 4: range con paso
for i in range(2, 11, 2):
    print(i, end=" ")

# EXPLICACIÓN:
# range(2, 11, 2) inicia en 2, termina antes de 11 y avanza de 2 en 2.
# Esto genera números pares: 2, 4, 6, 8, 10.


# Ejemplo 5: Cuenta regresiva
for i in range(10, 0, -1):
    print(i, end=" ")

# EXPLICACIÓN:
# range(10, 0, -1) comienza en 10 y disminuye de 1 en 1.
# Llega hasta 1 (sin incluir el 0).
# El paso negativo indica que el conteo es descendente.


# Ejemplo 6: Iterar usando índices
nombres = ["Ana", "Carlos", "Elena"]
for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

# EXPLICACIÓN:
# len(nombres) devuelve la cantidad de elementos de la lista.
# range(len(nombres)) genera índices válidos (0, 1, 2).
# Se accede a cada elemento usando nombres[i].
# Permite trabajar con posición y valor al mismo tiempo.


# Ejemplo 7: Uso de enumerate()
nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

# EXPLICACIÓN:
# enumerate() devuelve pares (índice, valor).
# Evita usar range y hace el código más claro.
# "indice" es la posición y "nombre" el valor del elemento.


# Ejemplo 8: Iterar sobre una cadena
mensaje = "Python"
for letra in mensaje:
    print(letra)

# EXPLICACIÓN:
# Las cadenas también son secuencias.
# El bucle recorre cada carácter individualmente.
# En cada iteración, "letra" contiene un carácter distinto.


# Ejemplo 9: Iterar sobre diccionario (claves)
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

# EXPLICACIÓN:
# Al recorrer un diccionario con for, se obtienen las claves.
# Para acceder al valor correspondiente se usa usuario[clave].


# Ejemplo 10: items() y values()
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

for valor in usuario.values():
    print(valor)

# EXPLICACIÓN:
# items() devuelve pares (clave, valor).
# values() devuelve solo los valores del diccionario.
# Permite recorrer estructuras de forma más directa.


# Ejemplo 11: Comprensiones de listas
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)

pares = [x for x in range(10) if x % 2 == 0]
print(pares)

# EXPLICACIÓN:
# Es una forma compacta de crear listas.
# En el primer caso se calculan cuadrados de 1 a 5.
# En el segundo se filtran solo números pares.
# Combina bucle y condición en una sola línea.


# Ejemplo 12: Bucles anidados
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()

# EXPLICACIÓN:
# Hay un bucle dentro de otro.
# El bucle interno se ejecuta completamente por cada iteración del externo.
# Se usa para trabajar con matrices o combinaciones.


# Ejemplo 13: Suma de números
n = 10
suma = 0
for i in range(1, n+1):
    suma += i
print(f"La suma es: {suma}")

# EXPLICACIÓN:
# Se inicializa la variable suma en 0.
# El bucle recorre del 1 al 10.
# En cada iteración se acumula el valor en "suma".
# Resultado final: suma total de los números.


# Ejemplo 14: Números primos
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []
for num in range(2, 20):
    if es_primo(num):
        primos.append(num)

print(primos)

# EXPLICACIÓN:
# Se define una función que verifica si un número es primo.
# Se prueba dividiendo hasta la raíz cuadrada del número.
# Si es divisible, no es primo.
# Luego se recorren números del 2 al 19 y se almacenan los primos en una lista.


# Ejemplo 15: Procesamiento de datos
temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

max_temp = max(temperaturas)
indice_max = temperaturas.index(max_temp)
print(f"Día más caluroso: {dias[indice_max]}")

promedio = sum(temperaturas) / len(temperaturas)
print(f"Promedio: {promedio:.1f}")

for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}")

# EXPLICACIÓN:
# max() obtiene la temperatura más alta.
# index() devuelve la posición de ese valor.
# Se usa esa posición para obtener el día correspondiente.
# sum() y len() calculan el promedio.
# Luego se recorre la lista para mostrar los días con temperatura mayor al promedio.


# Ejecutar:
# python src/iterativas/For_Range.py