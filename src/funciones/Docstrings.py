# Este programa demuestra el uso de docstrings en funciones

# Ejemplo 1: Docstring básico
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

print(sumar(2, 3))

# EXPLICACIÓN:
# El docstring define el propósito de la función.
# Se coloca inmediatamente después de la definición.
# Permite entender rápidamente qué hace sin leer la implementación.


# Ejemplo 2: Docstring completo
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        numeros: lista de valores numéricos

    Returns:
        promedio como float
    """
    return sum(numeros) / len(numeros)

print(calcular_promedio([1, 2, 3, 4]))

# EXPLICACIÓN:
# Incluye descripción, parámetros (Args) y valor de retorno (Returns).
# Facilita el uso correcto de la función.
# Es el formato recomendado en proyectos reales.


# Ejemplo 3: Acceder al docstring
print(calcular_promedio.__doc__)

# EXPLICACIÓN:
# __doc__ permite acceder al contenido del docstring en tiempo de ejecución.
# Es útil para inspección y herramientas automáticas.


# Ejemplo 4: Uso de help()
help(calcular_promedio)

# EXPLICACIÓN:
# help() muestra la documentación formateada de la función.
# Utiliza el docstring como fuente principal.


# Ejemplo 5: Validación con docstring estilo Google
def validar_email(email):
    """
    Verifica si un correo es válido.

    Args:
        email (str): correo a validar

    Returns:
        bool: True si es válido
    """
    return "@" in email and "." in email

print(validar_email("test@mail.com"))

# EXPLICACIÓN:
# Usa el estilo Google.
# Define tipo de dato y valor de retorno.
# Mejora la legibilidad y estandarización del código.


# Ejemplo 6: Docstring estilo reST
def convertir_a_celsius(fahrenheit):
    """
    Convierte Fahrenheit a Celsius.

    :param fahrenheit: temperatura en F
    :type fahrenheit: float
    :return: temperatura en C
    :rtype: float
    """
    return (fahrenheit - 32) * 5/9

print(convertir_a_celsius(68))

# EXPLICACIÓN:
# Usa formato reStructuredText.
# Es compatible con herramientas de documentación automática.
# Permite especificar tipos de forma explícita.


# Ejemplo 7: Docstring estilo NumPy
def filtrar_pares(lista):
    """
    Filtra números pares.

    Parameters
    ----------
    lista : list

    Returns
    -------
    list
    """
    return [n for n in lista if n % 2 == 0]

print(filtrar_pares([1,2,3,4,5,6]))

# EXPLICACIÓN:
# Usa el estilo NumPy.
# Muy utilizado en proyectos científicos.
# Presenta la información de forma estructurada.


# Ejemplo 8: Función simple documentada
def es_mayor_de_edad(edad):
    """Retorna True si es mayor de edad."""
    return edad >= 18

print(es_mayor_de_edad(20))

# EXPLICACIÓN:
# Docstring de una sola línea.
# Adecuado para funciones simples.
# Describe la funcionalidad de forma directa.


# Ejemplo 9: Función con comportamiento especial
def dividir_seguro(a, b):
    """
    Divide dos números.

    Returns:
        resultado o None si b es 0
    """
    if b == 0:
        return None
    return a / b

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))

# EXPLICACIÓN:
# Documenta comportamiento especial (división por cero).
# Indica claramente qué devuelve en casos límite.
# Evita mal uso de la función.


# Ejemplo 10: Docstring con ejemplos
def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Ejemplo:
        >>> area_triangulo(4,3)
        6.0
    """
    return (base * altura) / 2

print(area_triangulo(4,3))

# EXPLICACIÓN:
# Incluye ejemplos de uso dentro del docstring.
# Sirven como guía práctica y pruebas automatizadas.


# Ejemplo 11: Uso de doctest
import doctest
doctest.testmod()

# EXPLICACIÓN:
# doctest ejecuta los ejemplos del docstring.
# Permite validar automáticamente el comportamiento.


# Ejemplo 12: Buenas prácticas
def contar_palabras(texto):
    """
    Cuenta palabras en un texto.

    Args:
        texto (str)

    Returns:
        int
    """
    return len(texto.split())

print(contar_palabras("hola mundo python"))

# EXPLICACIÓN:
# Especifica tipo de entrada y salida.
# Mejora comprensión y mantenimiento del código.


# Ejemplo 13: Función completa bien documentada
def calcular_precio_final(precio_base, descuento=0, impuesto=0.21):
    """
    Calcula precio final con descuento e impuesto.

    Args:
        precio_base (float)
        descuento (float)
        impuesto (float)

    Returns:
        float

    Raises:
        ValueError
    """
    if precio_base < 0:
        raise ValueError("Valor inválido")

    precio = precio_base * (1 - descuento/100)
    return precio * (1 + impuesto)

print(calcular_precio_final(100, 10))

# EXPLICACIÓN:
# Docstring completo con parámetros, retorno y excepciones.
# Incluye validación de datos.
# Representa una implementación profesional.

# Ejecutar:
# python src/funciones/Docstrings.py