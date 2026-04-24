# Este programa usa match-case para evaluar diferentes tipos de datos

# Ejemplo 1: Clasificación de frutas
fruta = input("Introduzca una fruta: ")

match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")

# EXPLICACIÓN:
# Se usa match para comparar el valor de "fruta".
# Cada case es una opción posible.
# "_" funciona como "else" (caso por defecto).


# Ejemplo 2: Evaluación de coordenadas
punto = (0, 0)

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en coordenadas x={x}, y={y}.")

# EXPLICACIÓN:
# Se compara una tupla (x, y).
# Python desestructura los valores automáticamente.
# Dependiendo de los valores, entra en el case correspondiente.


# Ejemplo 3: Uso de guardas (if dentro de case)
edad = 20

match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")

# EXPLICACIÓN:
# Se usan condiciones adicionales dentro de case con "if".
# Permite evaluar rangos como en if-elif-else.


# Ejemplo 4: Evaluación de diccionarios
usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

for usuario in usuarios:
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.")
        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.")
        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.")
        case _:
            print(f"Rol de {usuario['nombre']} desconocido.")

# EXPLICACIÓN:
# Se comparan diccionarios por su estructura.
# Dependiendo del valor de "rol", se ejecuta un bloque distinto.


# Ejemplo 5: Evaluación de listas
numeros = [1, 2, 3, 4]

match numeros:
    case []:
        print("La lista está vacía.")
    case [uno]:
        print(f"Un solo elemento: {uno}.")
    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.")
    case [uno, *resto]:
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")

# EXPLICACIÓN:
# Se analiza la estructura de la lista.
# "*resto" captura todos los elementos restantes.
# Permite trabajar con listas de tamaño variable.

# Ejecutar: python src/condicionales/Match_Case.py