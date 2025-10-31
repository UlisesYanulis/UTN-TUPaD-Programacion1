#Práctico 6: Funciones

# %% Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# %% Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre))


# %% Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("Ingresá tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


# %% Ejercicio 4
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresá el radio del círculo: "))
print("Área:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))


# %% Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresá la cantidad de segundos: "))
print("Horas:", segundos_a_horas(segundos))


# %% Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresá un número: "))
tabla_multiplicar(numero)


# %% Ejercicio 7
def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b)

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))

suma, resta, producto, division = operaciones_basicas(a, b)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", producto)
print("División:", division)


# %% Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"IMC: {imc:.2f}")


# %% Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingresá la temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print("Fahrenheit:", fahrenheit)


# %% Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))

print("Promedio:", calcular_promedio(a, b, c))
# %%