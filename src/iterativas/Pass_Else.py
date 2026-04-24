# Este programa demuestra el uso de pass y else en bucles

# Ejemplo 1: Uso de pass
for numero in range(1, 10):
    if numero % 2 == 0:
        pass
    else:
        print(f"Procesando número impar: {numero}")

# EXPLICACIÓN:
# Recorre números del 1 al 9.
# Si el número es par → no hace nada (pass).
# Si es impar → lo imprime.
# pass sirve como placeholder cuando no quieres ejecutar código.


# Ejemplo 2: Función sin implementar
def procesar_datos():
    pass

procesar_datos()

# EXPLICACIÓN:
# Se define una función vacía.
# pass evita errores mientras no se implementa.
# Es útil en desarrollo progresivo.


# Ejemplo 3: Control con pass
modo_debug = False

for i in range(100):
    if not modo_debug:
        pass
    else:
        print(f"Procesando iteración {i}")

# EXPLICACIÓN:
# Si modo_debug es False → no imprime nada.
# Si fuera True → mostraría cada iteración.
# pass deja claro que no hacer nada es intencional.


# Ejemplo 4: else en for (no encuentra elemento)
numeros = [4, 6, 8, 9, 10, 12]

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")

# EXPLICACIÓN:
# Recorre la lista buscando un número primo.
# No encuentra ninguno → no se ejecuta break.
# Entonces se ejecuta el else.


# Ejemplo 5: else en for (sí encuentra elemento)
numeros = [4, 6, 7, 8, 10]

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")

# EXPLICACIÓN:
# Encuentra el número 7.
# Se ejecuta break.
# El else NO se ejecuta.


# Ejemplo 6: Validación con else
def validar_edades(lista_edades):
    for edad in lista_edades:
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")
            break
    else:
        print("Todas las edades son válidas")
        return True

    return False

# EXPLICACIÓN:
# Recorre la lista de edades.
# Si encuentra una inválida → break.
# Si todas son válidas → se ejecuta else.


# Ejemplo 7: Búsqueda con else
def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print(f"Usuario encontrado: {usuario}")
            return usuario
    else:
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")
        nuevo_usuario = {"nombre": nombre, "nivel": 1}
        usuarios.append(nuevo_usuario)
        return nuevo_usuario

# EXPLICACIÓN:
# Busca un usuario en la lista.
# Si lo encuentra → retorna.
# Si no → el else crea uno nuevo.


# Ejemplo 8: Combinando pass y else
def analizar_datos(valores, umbral):
    tiene_advertencias = False

    for valor in valores:
        if valor > umbral:
            tiene_advertencias = True
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")
        else:
            pass
    else:
        if not tiene_advertencias:
            print("Análisis completo: todos los valores están dentro del rango normal")
            return "OK"

    return "ADVERTENCIA"

# EXPLICACIÓN:
# Analiza cada valor.
# pass ignora valores normales.
# Si no hubo advertencias → else confirma que todo está bien.


# Ejemplo 9: while con else
def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2
    iteracion = 0

    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero/aproximacion) / 2
        iteracion += 1
    else:
        if iteracion < max_iteraciones:
            print(f"Convergencia alcanzada en {iteracion} iteraciones")
            return aproximacion

    print("No se alcanzó convergencia en el número máximo de iteraciones")
    return aproximacion

# EXPLICACIÓN:
# Ejecuta iteraciones para aproximar la raíz.
# Si termina normalmente (sin break) → se ejecuta else.
# Indica si logró converger.


# Ejemplo 10: Validación completa
def validar_formulario(datos):
    campos_requeridos = ["nombre", "email", "edad"]
    errores = []

    for campo in campos_requeridos:
        if campo not in datos:
            errores.append(f"Falta el campo requerido: {campo}")
            break
        elif not datos[campo]:
            errores.append(f"El campo {campo} no puede estar vacío")
            break
    else:
        if "@" not in datos["email"]:
            errores.append("Email inválido")

        try:
            edad = int(datos["edad"])
            if edad < 18 or edad > 120:
                errores.append("La edad debe estar entre 18 y 120")
        except ValueError:
            errores.append("La edad debe ser un número")

    if "telefono" in datos:
        if not datos["telefono"].isdigit():
            errores.append("El teléfono debe contener solo dígitos")
    else:
        pass

    if errores:
        return {"valido": False, "errores": errores}
    else:
        return {"valido": True}

# EXPLICACIÓN:
# Primero valida campos obligatorios.
# Si algo falla → break.
# Si todo está correcto → else valida formatos.
# pass se usa para campos opcionales.
# Devuelve si el formulario es válido o no.


# Ejecutar:
# python src/iterativas/Pass_Else.py