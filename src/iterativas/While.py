# Este programa demuestra el uso de bucles while en Python

# Ejemplo 1: while básico
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# EXPLICACIÓN:
# Se inicializa "contador" en 1.
# El bucle se ejecuta mientras contador sea menor o igual a 5.
# En cada iteración se imprime el valor y luego se incrementa.
# Es importante actualizar la variable para evitar bucles infinitos.


# Ejemplo 2: Validación de entrada (while en lugar de for)
entrada = ""
while not entrada.isdigit():
    entrada = input("Introduce un número: ")

print(f"Has introducido el número: {entrada}")

# EXPLICACIÓN:
# El bucle continúa mientras la entrada NO sea un número.
# isdigit() verifica si el texto contiene solo dígitos.
# Se repite hasta que el usuario ingrese un valor válido.


# Ejemplo 3: Bucle controlado por eventos (juego)
import random

objetivo = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado and intentos < 3:
    intentos += 1
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))

    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")

# EXPLICACIÓN:
# El bucle se ejecuta mientras no se adivine el número y queden intentos.
# Se controla con dos condiciones: estado (adivinado) y contador (intentos).
# Se da retroalimentación al usuario en cada intento.


# Ejemplo 4: Condición de salida variable (saldo)
saldo = 1000
while saldo > 0:
    print(f"Saldo actual: {saldo}€")
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))

    if gasto == 0:
        break

    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue

    saldo -= gasto

print(f"Saldo final: {saldo}€")

# EXPLICACIÓN:
# El bucle depende del valor de "saldo".
# break finaliza el bucle inmediatamente.
# continue salta al inicio del bucle sin ejecutar lo restante.
# Permite controlar múltiples condiciones dentro del ciclo.


# Ejemplo 5: Bucle infinito controlado
while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    if respuesta == "n":
        print("Programa finalizado.")
        break

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida.")

# EXPLICACIÓN:
# while True crea un bucle infinito.
# Se usa break para salir cuando se cumple una condición.
# Es útil cuando no se conoce cuántas veces se repetirá.


# Ejemplo 6: Procesamiento de datos (factorial)
def calcular_factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")

# EXPLICACIÓN:
# Se multiplica el número por todos los enteros hasta 1.
# En cada iteración, n disminuye.
# El bucle termina cuando n llega a 0.


# Ejemplo 7: Aproximación (raíz cuadrada)
def calcular_raiz_cuadrada(numero, precision=0.0001):
    aproximacion = numero / 2
    while abs(aproximacion**2 - numero) > precision:
        aproximacion = (aproximacion + numero/aproximacion) / 2
    return aproximacion

print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")

# EXPLICACIÓN:
# Se usa un método iterativo (aproximación sucesiva).
# El bucle se ejecuta hasta alcanzar una precisión deseada.
# abs() mide la diferencia entre el resultado y el valor real.


# Ejemplo 8: Validación de entrada con control de errores
def obtener_numero_en_rango(mensaje, minimo, maximo):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Debes introducir un número entero.")

edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)
print(f"Edad registrada: {edad} años")

# EXPLICACIÓN:
# while True permite repetir hasta obtener un valor válido.
# try/except maneja errores de conversión.
# return finaliza la función cuando la entrada es correcta.


# Ejemplo 9: Generación de patrones
def imprimir_triangulo(altura):
    fila = 1
    while fila <= altura:
        print("*" * fila)
        fila += 1

imprimir_triangulo(5)

# EXPLICACIÓN:
# Se controla el número de filas con "fila".
# En cada iteración se imprime una cantidad creciente de asteriscos.


# Ejemplo 10: Error común (bucle infinito)
# contador = 1
# while contador <= 5:
#     print(contador)
#     # Falta incrementar contador → bucle infinito

# EXPLICACIÓN:
# Si no se actualiza la variable de control, la condición nunca cambia.
# Esto provoca un bucle infinito.


# Ejemplo 11: Versión corregida
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# EXPLICACIÓN:
# Se agrega la actualización del contador.
# Permite que el bucle termine correctamente.


# Ejemplo 12: Comparación while vs for

# Usando while
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma (while): {suma}")

# Usando for
suma = 0
for i in range(1, 11):
    suma += i
print(f"Suma (for): {suma}")

# EXPLICACIÓN:
# Ambos hacen lo mismo.
# while se usa cuando no se conoce el número exacto de iteraciones.
# for es más simple cuando el rango está definido.


# Ejecutar:
# python src/iterativas/While.py