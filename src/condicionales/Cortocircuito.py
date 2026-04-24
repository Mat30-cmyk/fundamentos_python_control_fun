# Este programa demuestra la evaluación de cortocircuito

# Ejemplo 1: Evitar error con lista vacía
lista = []

if lista and lista[0] == 'Python':
    print("El primer elemento es 'Python'.")

# EXPLICACIÓN:
# "lista" vacío = False
# Entonces NO evalúa lista[0]
# Evita error (IndexError) 🔥


# Ejemplo 2: Evitar división por cero
dividendo = 10
divisor = 0

if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")

# EXPLICACIÓN:
# Primero evalúa divisor != 0 → False
# Entonces NO ejecuta la división
# Evita crash 😵


# Ejemplo 3: Operador OR (cortocircuito)
acceso_registrado = True
acceso_permitido = False

if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")

# EXPLICACIÓN:
# "or" se cumple si una es True
# No necesita evaluar todo siempre
# Más rápido ⚡


# Ejemplo alternativo sin cortocircuito (más largo)
# if acceso_permitido:
#     print("Acceso concedido.")
# else:
#     if acceso_registrado:
#         print("Acceso concedido.")


# Ejemplo 4: any() con cortocircuito
numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es no cero.")

# EXPLICACIÓN:
# any() para cuando encuentra un True
# Aquí se detiene en el 1
# No revisa toda la lista 😎


# Ejemplo 5: all() con cortocircuito
condiciones = [True, True, False, True]

if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")

# EXPLICACIÓN:
# all() se detiene cuando encuentra False
# Aquí para en el tercero
# Más eficiente 🚀

# Ejecutar:
# python src/condicionales/Cortocircuito.py