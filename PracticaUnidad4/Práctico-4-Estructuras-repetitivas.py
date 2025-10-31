# Práctico	4:	Estructuras	repetitivas

# %% Ejercicio 1
for i in range(0, 101):
    print(i)


# %% Ejercicio 2
n = int(input("Ingrese un número entero: "))
n = abs(n)
if n == 0:
    digitos = 1
else:
    digitos = 0
    while n > 0:
        n //= 10
        digitos += 1
print(digitos)


# %% Ejercicio 3
a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))

inicio = min(a, b) + 1
fin = max(a, b)

suma = 0
for n in range(inicio, fin):
    suma += n

print(suma)


# %% Ejercicio 4
total = 0
while True:
    n = int(input("Ingrese un número entero (0 para terminar): "))
    if n == 0:
        break
    total += n
print(total)


# %% Ejercicio 5
import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Ingrese un número entre 0 y 9: "))
    intentos += 1
    if intento == secreto:
        break

print(intentos)


# %% Ejercicio 6
for i in range(100, -1, -2):
    print(i)


# %% Ejercicio 7
n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(0, n + 1):
    suma += i
print(suma)


# %% Ejercicio 8
N = 100
pares = impares = negativos = positivos = 0

for i in range(N):
    n = int(input("Ingrese un número entero: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Negativos:", negativos)
print("Positivos:", positivos)


# %% Ejercicio 9
N = 3
total = 0
for _ in range(N):
    n = int(input("Ingrese un número entero: "))
    total += n
media = total / N
print(media)


# %% Ejercicio 10
n = int(input("Ingrese un número entero: "))
invertido = 0
while n > 0:
    invertido = invertido * 10 + (n % 10)
    n //= 10
print(invertido)
# %%