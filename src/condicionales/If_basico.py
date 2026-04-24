# Este programa evalúa diferentes condiciones usando if

edad = 20
if edad >= 18:
    print("Eres mayor de edad.")

# EXPLICACIÓN:
# Se evalúa si la variable edad es mayor o igual a 18.
# Como 20 cumple la condición, se imprime el mensaje.
# Si no se cumpliera, no pasaría nada (no hay else).

temperatura = 30
if temperatura > 25:
    print("Hace calor hoy.")

# EXPLICACIÓN:
# Se verifica si la temperatura es mayor a 25.
# Como 30 es mayor, se ejecuta el print.
# Sirve para tomar decisiones basadas en valores.

hora = 10
if hora >= 6 and hora < 12:
    print("Buenos días.")

# EXPLICACIÓN:
# Aquí se usan dos condiciones con "and".
# Se valida que la hora esté entre 6 y 12.
# Ambas deben cumplirse para que se ejecute el mensaje.

# Ejecutar: python src/condicionales/If_basico.py