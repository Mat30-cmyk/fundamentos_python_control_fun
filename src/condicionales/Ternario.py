# Este programa usa condicionales ternarios (if en una sola línea)

# Ejemplo 1: Mayor o menor de edad
edad = 17
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)

# EXPLICACIÓN:
# Si la condición es verdadera → primer valor
# Si es falsa → segundo valor
# Es un if-else en una sola línea.


# Ejemplo 2: Número máximo
a = 1
b = 2

print("El máximo es:", a if a > b else b)

# EXPLICACIÓN:
# Compara a y b.
# Devuelve el mayor sin usar if tradicional.


# Ejemplo 3: Ternario anidado
edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)

# EXPLICACIÓN:
# Hay un ternario dentro de otro.
# Evalúa múltiples condiciones, pero se vuelve medio enredado 🤯


# Ejemplo 4: (repetido, mismo caso)
edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)

# EXPLICACIÓN:
# Es el mismo ejemplo anterior.
# Sirve para reforzar cómo funcionan los ternarios anidados.


# Ejemplo 5: Uso en listas (list comprehension)
numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)

# EXPLICACIÓN:
# Recorre la lista y evalúa cada número.
# Si es par → "par"
# Si no → "impar"
# Resultado: ['impar', 'par', 'impar', 'par', 'impar']


# Ejemplo 6: Evitar error (división por cero)
dividendo = 10
divisor = 0
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"
print(resultado)

# EXPLICACIÓN:
# Solo divide si divisor ≠ 0.
# Si no, evita el error y muestra mensaje.
# Esto es usar ternario de forma inteligente 🧠


# Ejecutar:
# python src/condicionales/Ternario.py