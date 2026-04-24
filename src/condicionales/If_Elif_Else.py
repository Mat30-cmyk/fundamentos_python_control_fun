# Este programa evalúa múltiples condiciones usando if-elif-else

numero = 0

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# EXPLICACIÓN:
# Se evalúan varias condiciones en orden.
# Si es mayor que 0 → positivo.
# Si es menor que 0 → negativo.
# Si no cumple ninguna → es cero (else).

nota = 87

if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 80:
    print("Calificación: Notable")
elif nota >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Suspenso")

# EXPLICACIÓN:
# Se evalúan rangos de nota.
# Python ejecuta SOLO la primera condición verdadera.
# 87 cumple >=80, por eso imprime "Notable".

edad = 45

if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")

# EXPLICACIÓN:
# Se usan comparaciones encadenadas.
# 45 está entre 18 y 65 → adulto.
# Es más limpio que usar varios and.

color = "azul"

if color == "rojo":
    print("El color es rojo.")
elif color == "verde":
    print("El color es verde.")
elif color == "azul":
    print("El color es azul.")

# EXPLICACIÓN:
# Se comparan valores específicos.
# Cuando encuentra coincidencia, se detiene.
# "azul" coincide en el último elif.

# Ejecutar: python src/condicionales/If_Elif_Else.py