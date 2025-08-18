#Práctico 1: Estructuras secuenciales  

import math

#1
print("Hola Mundo!")

#2
nombre = str(input("Ingrese su nombre: "))
print(f"Hola {nombre}!")

#3
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))
residencia = str(input("Ingrese su lugar de residencia: "))
print(f"Soy {nombre} {apellido}, tengo {edad} años y resido en {residencia}.")

#4
radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print(f"El area del circulo es {area} y el perimetro es {perimetro}.")

#5
seg = int(input("Ingrese la cantidad de segundos: "))
hora = seg / 3600
print(f"{seg} segundos equivalen a {hora} horas.")

#6
num = int(input("Ingrese un numero para ver su tabla de multiplicar: "))
num1 = num * 1
num2 = num * 2
num3 = num * 3
num4 = num * 4
num5 = num * 5
num6 = num * 6
num7 = num * 7
num8 = num * 8
num9 = num * 9
num10 = num * 10

print(f"""
    {num} x 1 = {num1}.
    {num} x 2 = {num2}.
    {num} x 3 = {num3}.
    {num} x 4 = {num4}.
    {num} x 5 = {num5}.
    {num} x 6 = {num6}.
    {num} x 7 = {num7}.
    {num} x 8 = {num8}.
    {num} x 9 = {num9}.
    {num} x 10 = {num10}.
      """)

#7
num1 = int(input("Ingrese el primer numero distinto a 0: "))
num2 = int(input("Ingrese el segundo numero distinto a 0: "))
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f"""
    Resultado suma: {suma}.
    Resultado resta: {resta}.
    Resultado multiplicacion: {mult}.
    Resultado division: {div}.
      """)

#8
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura ** 2)

print(f"El indice de masa corporal es de {imc}")

#9
celsius = float(input("Ingrese los °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} °C equivalen a {fahrenheit} °F.")

#10
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3

print(f"El promedio es {promedio}.")