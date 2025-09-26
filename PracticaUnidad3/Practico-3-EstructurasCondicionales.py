#Practico 3 Estructuras Condicionales

# %% Ejercicio 1
edad = int(input("Ingresá tu edad: "))

if edad > 18:
    print("Es mayor de edad")


# %% Ejercicio 2
nota = float(input("Ingresá tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# %% Ejercicio 3
n = int(input("Ingresá un número: "))

if n % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# %% Ejercicio 4
edad = int(input("Ingresá tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:  # 12 a 17
    print("Adolescente")
elif edad < 30:  # 18 a 29
    print("Adulto/a joven")
else:            # 30 o más
    print("Adulto/a")


# %% Ejercicio 5
contrasena = input("Ingresá una contraseña: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# %% Ejercicio 6
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")


# %% Ejercicio 7
texto = input("Ingresá una frase o palabra: ")
vocales = "aeiouAEIOU"

if len(texto) > 0 and texto[-1] in vocales:
    texto = texto + "!"
print(texto)


# %% Ejercicio 8
nombre = input("Ingresá tu nombre: ")
opcion = input("Elegí 1 (MAYÚSCULAS), 2 (minúsculas) o 3 (Primera letra mayúscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())


# %% Ejercicio 9
magnitud = float(input("Ingresá la magnitud del terremoto (escala Richter): "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


# %% Ejercicio 10 (alternativa repetitiva, validación previa)
hemisferio = input("Hemisferio (N/S): ").upper()

if hemisferio == "N" or hemisferio == "S":
    mes = int(input("Mes (1-12): "))
    dia = int(input("Día (1-31): "))

    mmdd = mes * 100 + dia  # formateo MMDD para comparar rangos

    if hemisferio == "N":
        if (1221 <= mmdd <= 1231) or (101 <= mmdd <= 320):
            print("Invierno")
        elif 321 <= mmdd <= 620:
            print("Primavera")
        elif 621 <= mmdd <= 920:
            print("Verano")
        else:  # 21/09–20/12
            print("Otoño")

    elif hemisferio == "S":
        if (1221 <= mmdd <= 1231) or (101 <= mmdd <= 320):
            print("Verano")
        elif 321 <= mmdd <= 620:
            print("Otoño")
        elif 621 <= mmdd <= 920:
            print("Invierno")
        else:  # 21/09–20/12
            print("Primavera")
else:
    print("Entrada inválida: escribí 'N' o 'S'.")