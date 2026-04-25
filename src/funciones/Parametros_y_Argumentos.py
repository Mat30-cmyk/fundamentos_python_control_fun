# Este programa demuestra el uso de funciones en Python

# Ejemplo 1: Función básica
def saludar():
    print("¡Hola, mundo!")

saludar()

# EXPLICACIÓN:
# Se define una función sin parámetros.
# Al llamarla, ejecuta el print.
# Sirve para reutilizar código simple.


# Ejemplo 2: Función con retorno
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")

# EXPLICACIÓN:
# Recibe base y altura.
# Calcula el área.
# return devuelve el resultado para usarlo fuera.


# Ejemplo 3: Funciones simples
def es_par(numero):
    return numero % 2 == 0

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(es_par(4))
print(celsius_a_fahrenheit(25))

# EXPLICACIÓN:
# es_par devuelve True si es par.
# celsius_a_fahrenheit convierte temperatura.
# Funciones pequeñas = mejor organización.


# Ejemplo 4: Funciones como variables
convertir = celsius_a_fahrenheit
print(convertir(25))

# EXPLICACIÓN:
# Se guarda la función en una variable.
# Se puede llamar igual.
# Python trata funciones como datos.


# Ejemplo 5: Ámbito (scope)
def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

precio_con_descuento = calcular_descuento(100)
print(f"Precio con descuento: {precio_con_descuento}")

# EXPLICACIÓN:
# descuento solo existe dentro de la función.
# No se puede usar fuera.
# Evita conflictos de variables.


# Ejemplo 6: Parámetros y argumentos
def saludar_persona(nombre):
    print(f"Hola, {nombre}!")

saludar_persona("Ana")

# EXPLICACIÓN:
# nombre = parámetro.
# "Ana" = argumento.
# Permite funciones dinámicas.


# Ejemplo 7: Parámetros posicionales
def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

print(calcular_precio_final(100, 0.21))

# EXPLICACIÓN:
# Los valores se asignan por orden.
# 100 → precio_base
# 0.21 → impuesto


# Ejemplo 8: Parámetros con valor por defecto
def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")
saludar("María", "¿Cómo estás?")

# EXPLICACIÓN:
# mensaje tiene valor por defecto.
# Se usa si no se envía argumento.
# Hace la función flexible.


# Ejemplo 9: Parámetros por nombre
def dividir(dividendo, divisor):
    return dividendo / divisor

print(dividir(divisor=2, dividendo=10))

# EXPLICACIÓN:
# No importa el orden.
# Se especifica cada argumento por nombre.
# Mejora la legibilidad.


# Ejemplo 10: Función con múltiples datos
def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)

print(usuario)

# EXPLICACIÓN:
# Devuelve un diccionario.
# Usa parámetros nombrados.
# Facilita trabajar con datos estructurados.


# Ejemplo 11: Combinación de parámetros
def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"

print(calcular_pago(40))
print(calcular_pago(30, moneda="USD"))

# EXPLICACIÓN:
# Mezcla parámetros normales y por defecto.
# Permite diferentes formas de uso.


# Ejemplo 12: Validación de argumentos
def calcular_descuento_seguro(precio, porcentaje):
    if not isinstance(precio, (int, float)) or precio < 0:
        raise ValueError("Precio inválido")

    if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):
        raise ValueError("Porcentaje inválido")

    return precio - (precio * porcentaje / 100)

try:
    print(calcular_descuento_seguro(100, 15))
except ValueError as e:
    print(e)

# EXPLICACIÓN:
# Valida tipo y rango de datos.
# Evita errores en ejecución.
# Usa excepciones.


# Ejemplo 13: *args (múltiples argumentos)
def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar(1, 2, 3, 4))

# EXPLICACIÓN:
# Recibe cualquier cantidad de números.
# Se almacenan como tupla.
# Se recorren con for.


# Ejemplo 14: **kwargs (argumentos por nombre)
def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Python", año=1991)

# EXPLICACIÓN:
# Recibe argumentos tipo clave=valor.
# Se almacenan como diccionario.
# Muy flexible.


# Ejemplo 15: Función completa
def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):
    if mayusculas:
        texto = texto.upper()

    palabras = texto.split()
    palabras_formateadas = [f"{prefijo}{p}{sufijo}" for p in palabras]
    return separador.join(palabras_formateadas)

print(formatear_texto("python es poderoso"))
print(formatear_texto("python es poderoso", mayusculas=True))
print(formatear_texto("python es poderoso", prefijo="#", sufijo="!"))

# EXPLICACIÓN:
# Aplica múltiples transformaciones.
# Usa parámetros opcionales.
# Demuestra funciones flexibles y reutilizables.


# Ejecutar:
# python src/funciones/Parametros_y_Argumentos.py