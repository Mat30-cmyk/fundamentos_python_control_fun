# Este programa usa condicionales anidados para tomar decisiones más complejas

# Ejemplo 1: Edad y estado civil
edad = 30
estado_civil = 'soltero'

if edad >= 18:
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    print('Eres menor de edad.')

# EXPLICACIÓN:
# Primero valida si es mayor de edad.
# Luego, dentro de ese bloque, evalúa el estado civil.
# Es un if dentro de otro if (anidado).


# Ejemplo 2: Licencia con permisos (anidado)
edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
else:
    if edad >= 16:
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        print('Eres demasiado joven para conducir.')

# EXPLICACIÓN:
# Se evalúa primero la edad.
# Si no es mayor de edad, entra a otro if.
# Luego valida si tiene permiso.
# Hay varios niveles de anidación (más profundo = más complejo).


# Ejemplo 3: Versión optimizada (sin anidar tanto)
edad = 16
permiso_padres = True

if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
elif edad >= 16 and permiso_padres:
    print('Puedes obtener la licencia con permiso de tus padres.')
elif edad >= 16 and not permiso_padres:
    print('Necesitas el permiso de tus padres para obtener la licencia.')
else:
    print('Eres demasiado joven para conducir.')

# EXPLICACIÓN:
# Se reemplazan los anidados por elif.
# Es más limpio y fácil de leer.
# Usa operadores lógicos (and, not).


# Ejemplo 4: Validación de usuario y contraseña
usuario = 'admin'
contrasena = '1234'

if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')

# EXPLICACIÓN:
# Primero valida el usuario.
# Solo si es correcto, revisa la contraseña.
# Esto evita validar cosas innecesarias.


# Ejemplo 5: Encontrar el número mayor (anidado)
a = 5
b = 10
c = 15

if a > b:
    if a > c:
        print('a es el mayor.')
    else:
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')

# EXPLICACIÓN:
# Se comparan los números entre sí usando varios if.
# Es funcional, pero difícil de leer.
# Mucha anidación = código más enredado 😵


# Alternativa más sencilla (recomendada):
# mayor = a
#
# if b > mayor:
#     mayor = b
#
# if c > mayor:
#     mayor = c
#
# print(f'El número mayor es {mayor}.')

# EXPLICACIÓN:
# Se usa una variable auxiliar.
# Se compara paso a paso.
# Mucho más limpio y mantenible.


# Ejecutar:
# python src/condicionales/Condicionales_Anidados.py