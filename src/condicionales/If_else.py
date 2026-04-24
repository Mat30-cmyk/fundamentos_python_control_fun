# Este programa evalúa diferentes casos usando if-else

edad = 17
if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")

# EXPLICACIÓN:
# Se evalúa si la edad es mayor o igual a 18.
# Como 17 no cumple la condición, se ejecuta el else.
# El else se usa cuando la condición es falsa.

contrasena = input("Introduce la contraseña: ")
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")

# EXPLICACIÓN:
# Se compara la contraseña ingresada con la correcta.
# Si coinciden, se permite el acceso.
# Si no, se ejecuta el else y se niega el acceso.

numero = 15
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# EXPLICACIÓN:
# Se usa el operador módulo (%) para saber si es divisible por 2.
# Si el residuo es 0, es par.
# Si no, es impar (entra al else).

saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")

# EXPLICACIÓN:
# Se verifica si hay suficiente saldo para retirar.
# Como 300 < 500, no alcanza.
# Entonces se ejecuta el else mostrando el saldo actual.

# Ejecutar: python src/condicionales/If_else.py