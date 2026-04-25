# Este programa demuestra el uso de return en funciones

# Ejemplo 1: Retorno básico
def calcular_cuadrado(numero):
    resultado = numero * numero
    return resultado

area = calcular_cuadrado(4)
print(area)

# EXPLICACIÓN:
# Recibe un número.
# Calcula su cuadrado.
# return devuelve el resultado y termina la función.


# Ejemplo 2: Función sin return
def saludar(nombre):
    print(f"Hola, {nombre}")

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")

# EXPLICACIÓN:
# La función imprime pero no retorna nada.
# Python devuelve None automáticamente.
# Diferencia entre mostrar y devolver.


# Ejemplo 3: Múltiples valores
def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)

print(suma, media, menor, mayor)

# EXPLICACIÓN:
# Retorna varios valores.
# Python los empaqueta en una tupla.
# Se pueden desempaquetar en variables.


# Ejemplo 4: Retorno como tupla
resultado = estadisticas(datos)
print(resultado)
print(resultado[1])

# EXPLICACIÓN:
# Se guarda todo en una sola variable.
# Se accede por índices.
# Es una tupla.


# Ejemplo 5: Return anticipado
def dividir_seguro(a, b):
    if b == 0:
        print("Error: División por cero")
        return None

    return a / b

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))

# EXPLICACIÓN:
# Si b es 0 → retorna antes.
# Evita errores.
# El código después no se ejecuta.


# Ejemplo 6: Función booleana
def es_mayor_de_edad(edad):
    return edad >= 18

print(es_mayor_de_edad(16))

# EXPLICACIÓN:
# Devuelve True o False.
# Se usa en condicionales.
# Hace el código más claro.


# Ejemplo 7: Validación simple
def es_correo_valido(email):
    return "@" in email and "." in email

print(es_correo_valido("test@mail.com"))

# EXPLICACIÓN:
# Verifica condiciones.
# Retorna booleano.
# Muy común en validaciones.


# Ejemplo 8: Transformación de datos
def formato_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"

print(formato_nombre("ana", "garcia"))

# EXPLICACIÓN:
# Modifica el formato del texto.
# Retorna el resultado.
# No imprime dentro de la función.


# Ejemplo 9: Cálculo con return
def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    return precio_base * (1 + tasa_iva)

print(calcular_precio_con_iva(100))

# EXPLICACIÓN:
# Aplica un cálculo.
# Retorna el resultado.
# Usa parámetro por defecto.


# Ejemplo 10: Retorno de lista
def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

print(crear_lista_pares(10))

# EXPLICACIÓN:
# Genera lista con comprensión.
# Retorna todos los pares.
# No usa variables externas.


# Ejemplo 11: Retorno de diccionario
def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

print(crear_diccionario_cuadrados([1, 2, 3, 4]))

# EXPLICACIÓN:
# Crea estructura tipo dict.
# Clave = número, valor = cuadrado.
# Retorna estructura completa.


# Ejemplo 12: Coherencia en retorno
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []

    return [num for num in numeros if num > 0]

print(filtrar_positivos([1, -2, 3]))

# EXPLICACIÓN:
# Siempre devuelve lista.
# Evita errores de tipo.
# Buena práctica.


# Ejemplo 13: Return temprano en lógica
def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Inválido"
    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"
    return "Insuficiente"

print(obtener_calificacion(85))

# EXPLICACIÓN:
# Evalúa condiciones en orden.
# Cada return corta la ejecución.
# Evita if anidados.


# Ejemplo 14: Conversión completa
def convertir_temperatura(valor, origen, destino):
    unidades_validas = {'C', 'F', 'K'}
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    if origen == destino:
        return valor

    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:
        celsius = valor

    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:
        return celsius

print(convertir_temperatura(25, 'C', 'F'))

# EXPLICACIÓN:
# Valida datos.
# Usa retorno anticipado.
# Convierte entre unidades.
# Siempre devuelve valor o None.


# Ejecutar:
# python src/funciones/Return.py