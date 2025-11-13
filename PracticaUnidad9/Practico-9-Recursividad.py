# Práctico 9: Recursividad

# %% Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un numero entero positivo: "))

for i in range(1, numero + 1):
    print("Factorial de", i, "=", factorial(i))

# %% Ejercicio 2
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

n = int(input("Ingrese la posicion hasta la que quiere ver la serie de Fibonacci: "))

for i in range(0, n + 1):
    print(fibonacci(i), end=" ")

print()


# %% Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print("Resultado:", resultado)


# %% Ejercicio 4
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un numero entero decimal: "))
binario = decimal_a_binario(numero)
print("El numero en binario es:", binario)



# %% Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra: ")

if es_palindromo(texto):
    print("Es palindromo")
else:
    print("No es palindromo")

# %% Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un numero entero positivo: "))
resultado = suma_digitos(numero)
print("La suma de sus digitos es:", resultado)

# %% Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

filas = int(input("Ingrese la cantidad de filas de bloques: "))
total = contar_bloques(filas)
print("La cantidad total de bloques es:", total)


# %% Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0

    ultimo = numero % 10

    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese el digito a contar: "))

cantidad = contar_digito(numero, digito)
print("El digito aparece", cantidad, "veces")
# %%
