# Este programa demuestra el uso de break y continue en Python


# Ejemplo 1: Uso de break
for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")

print("Bucle terminado")

# EXPLICACIÓN:
# El bucle recorre números del 1 al 10.
# Cuando encuentra el número 5, ejecuta break.
# break detiene completamente el bucle.
# No se ejecutan más iteraciones después de ese punto.


# Ejemplo 2: Búsqueda eficiente
def buscar_elemento(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")

# EXPLICACIÓN:
# Se recorre la lista buscando un valor específico.
# Cuando se encuentra, se retorna la posición inmediatamente.
# Esto evita recorrer toda la lista innecesariamente.


# Ejemplo 3: Salida controlada con break
while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    print(f"Has escrito: {entrada}")

# EXPLICACIÓN:
# while True crea un bucle infinito.
# Se usa break para salir cuando el usuario escribe "salir".
# Permite controlar la ejecución mediante eventos.


# Ejemplo 4: Optimización (número primo)
def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

# EXPLICACIÓN:
# Se verifica si un número es divisible.
# Si se encuentra un divisor, se termina inmediatamente.
# Evita cálculos innecesarios.


# Ejemplo 5: Uso de continue
for numero in range(1, 11):
    if numero % 2 == 0:
        continue

    print(f"Número impar: {numero}")

# EXPLICACIÓN:
# continue omite la iteración actual.
# En este caso, se saltan los números pares.
# Solo se imprimen los números impares.


# Ejemplo 6: Filtrado de datos
temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue

    print(f"{temp}°C")

# EXPLICACIÓN:
# Se recorren las temperaturas.
# Se ignoran valores negativos o cero.
# Solo se procesan los valores positivos.


# Ejemplo 7: Evitar errores (división por cero)
numeros = [1, 2, 0, 4, 0, 6, 7]

for num in numeros:
    if num == 0:
        print("Omitiendo división por cero")
        continue

    resultado = 10 / num
    print(f"10 / {num} = {resultado}")

# EXPLICACIÓN:
# Se evita dividir entre cero.
# continue salta esa iteración.
# Previene errores en ejecución.


# Ejemplo 8: Validación de datos
datos = ["25", "error", "42", "texto", "17"]

suma = 0
for valor in datos:
    if not valor.isdigit():
        print(f"Valor no numérico ignorado: '{valor}'")
        continue

    suma += int(valor)

print(f"La suma de los valores válidos es: {suma}")

# EXPLICACIÓN:
# Se verifica si el dato es numérico.
# Los valores inválidos se ignoran.
# Solo se suman los números válidos.


# Ejemplo 9: Combinación de break y continue
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue

    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    if suma > limite:
        print(f"Límite de {limite} superado")
        break

# EXPLICACIÓN:
# continue omite números múltiplos de 3.
# break detiene el bucle si la suma supera el límite.
# Permite controlar el flujo de forma más precisa.


# Ejemplo 10: Bucles anidados
for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue

        print(f"  Elemento {j}")

    print("Fin del grupo\n")

# EXPLICACIÓN:
# continue solo afecta al bucle interno.
# El bucle externo sigue ejecutándose normalmente.


# Ejemplo 11: Salir de múltiples bucles
encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break

    if encontrado:
        break

# EXPLICACIÓN:
# break solo sale del bucle interno.
# Se usa una variable (bandera) para salir también del externo.


# Ejemplo 12: Mejora de legibilidad
# def procesar_item(item):
#     if condicion1(item):
#         return False
#     if condicion2(item):
#         return None
#     return item

# EXPLICACIÓN:
# En lugar de muchos break y continue,
# se delega la lógica a una función.
# Hace el código más limpio y mantenible.


# Ejemplo 13: Rendimiento con break
# encontrado = False
# for elemento in lista_grande:
#     if elemento == objetivo:
#         encontrado = True
#         break

# EXPLICACIÓN:
# break evita recorrer toda la lista.
# Mejora el rendimiento en listas grandes.


# Ejemplo 14: Validación de contraseña
def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
            continue

        if caracter.islower():
            tiene_minuscula = True
            continue

        if caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero

# EXPLICACIÓN:
# Se recorren los caracteres de la contraseña.
# Se verifican condiciones de seguridad.
# continue evita evaluaciones innecesarias.


# Ejemplo 15: Procesamiento de transacciones
transacciones = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

total_procesado = 0

for t in transacciones:
    if t["estado"] != "completada":
        print(f"Transacción {t['id']}: {t['estado']} - ignorada")
        continue

    if t["monto"] <= 0:
        print(f"Transacción {t['id']}: monto inválido ({t['monto']})")
        continue

    total_procesado += t["monto"]
    print(f"Transacción {t['id']}: {t['monto']}€ procesada")

print(f"Total procesado: {total_procesado}€")

# EXPLICACIÓN:
# Se filtran transacciones inválidas con continue.
# Solo se procesan las válidas.
# Se acumula el total correctamente.


# Ejecutar:
# python src/iterativas/Break_Continue.py