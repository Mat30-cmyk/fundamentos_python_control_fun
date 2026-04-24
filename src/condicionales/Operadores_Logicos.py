# Este programa usa operadores lógicos (and, or, not)

# Ejemplo 1: Operador AND
edad = 25
ingresos = 30000

if edad >= 18 and ingresos >= 20000:
    print("Eres elegible para el crédito.")

# EXPLICACIÓN:
# "and" exige que ambas condiciones sean verdaderas.
# Si una falla, no entra al if.


# Ejemplo 2: Operador OR
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")

# EXPLICACIÓN:
# "or" funciona si al menos una condición es verdadera.
# Aquí basta con que sea sábado o domingo.


# Ejemplo 3: Operador NOT
llueve = False

if not llueve:
    print("Podemos salir al parque.")

# EXPLICACIÓN:
# "not" invierte el valor.
# False → True, por eso entra al if.


# Ejemplo 4: Combinación de operadores
edad = 17
permiso_parental = True

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")

# EXPLICACIÓN:
# Puede conducir si:
# - Es mayor de 18
# - O tiene 16+ y permiso
# Se usan paréntesis para controlar el orden.


# Ejemplo 5: Precedencia de operadores
a = True
b = False
c = not b

# resultado = (a or b) and c
resultado = a or b and c
print(resultado)  # Imprime True

# EXPLICACIÓN:
# Orden: not → and → or
# Se evalúa como: a or (b and c)
# b and c = False, entonces queda: True or False → True


# Ejemplo 6: Uso sin operador lógico (anidado)
usuario = "admin"
contrasena = "1234"

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")

# EXPLICACIÓN:
# Primero valida usuario, luego contraseña.
# Funciona, pero está anidado (más feo 😵).


# Ejemplo 7: Forma optimizada con AND
# if usuario == "admin" and contrasena == "1234":
#     print("Acceso concedido.")

# EXPLICACIÓN:
# Se combinan ambas condiciones en una sola línea.

# Ejecutar:
# python src/condicionales/Operadores_Logicos.py