#Práctico 5: Listas

# %% Ejercicio 1
# Lista de estudiantes
notas = [7, 8, 5, 9, 6, 10, 4, 8, 7, 6]

# Mostrar la lista
print("Lista completa de notas:")
for n in notas:
    print(n)

# Calcular y mostrar el promedio
promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

# Indicar nota más alta y más baja
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

# %% Ejercicio 2
# Pedir al usuario que cargue 5 productos
productos = []
for i in range(5):
    p = input(f"Ingrese el producto {i+1}: ")
    productos.append(p)

# Mostrar la lista ordenada alfabéticamente
ordenada = sorted(productos)

print("Lista ordenada alfabéticamente:")
for item in ordenada:
    print(item)

# Preguntar qué producto desea eliminar y actualizar lista
a_eliminar = input("Producto a eliminar: ")
if a_eliminar in productos:
    productos.remove(a_eliminar)
    # Volver a mostrar la lista
    ordenada_actualizada = sorted(productos)
    print("Lista actualizada:")
    for item in ordenada_actualizada:
        print(item)

# %% Ejercicio 3
import random

# Generar una lista con 15 números al azar entre 1 y 100
numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

# Crear una lista con los pares y otra con los impares
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

# Mostrar cuántos números tiene cada lista
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

# %% Ejercicio 4
# Lista con valores repetidos
valores = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Crear nueva lista sin elementos repetidos
sin_repetidos = []
for v in valores:
    if v not in sin_repetidos:
        sin_repetidos.append(v)

# Mostrar el resultado
for x in sin_repetidos:
    print(x)

# %% Ejercicio 5
# Lista con 8 estudiantes
estudiantes = ["Ana", "Bruno", "Camila", "Diego", "Elena", "Felipe", "Giselle", "Hugo"]

# Mostrar lista
print("Estudiantes presentes:")
for n in estudiantes:
    print(n)

# Agregar o eliminar
accion = input("¿Desea agregar (A) o eliminar (E) un estudiante? ").strip().upper()

if accion == "A":
    nuevo = input("Nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)
elif accion == "E":
    borrar = input("Nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)

# Mostrar lista
print("Lista final actualizada:")
for n in estudiantes:
    print(n)

# %% Ejercicio 6
# Lista
numeros = [3, 5, 8, 2, 9, 1, 4]

# Rotar una posición hacia la derecha (el último pasa a ser el primero)
ultimo = numeros.pop()
numeros.insert(0, ultimo)

# Mostrar lista
for n in numeros:
    print(n)

# %% Ejercicio 7
# Matriz 7x2 con mínima y máxima de cada día de la semana
temperaturas = [
    [12, 20],
    [10, 18],
    [9, 16],
    [11, 19],
    [8, 17],
    [10, 21],
    [13, 22]
]

# Promedios
minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]
prom_min = sum(minimas) / len(minimas)
prom_max = sum(maximas) / len(maximas)

print("Promedio de mínimas:", prom_min)
print("Promedio de máximas:", prom_max)

# Día con mayor amplitud térmica
amplitudes = [maximas[i] - minimas[i] for i in range(7)]
dia_mayor_amplitud = amplitudes.index(max(amplitudes)) + 1
print("Día con mayor amplitud térmica:", dia_mayor_amplitud)

# %% Ejercicio 8
# Matriz 5x3 con notas de 5 estudiantes en 3 materias
notas = [
    [7, 8, 6],
    [5, 9, 7],
    [10, 6, 8],
    [4, 7, 6],
    [8, 9, 10]
]

# Promedio de cada estudiante (por fila)
print("Promedio de cada estudiante:")
for i in range(len(notas)):
    prom = sum(notas[i]) / len(notas[i])
    print(f"Estudiante {i+1}: {prom}")

# Promedio de cada materia (por columna)
print("Promedio de cada materia:")
num_est = len(notas)
num_mat = len(notas[0])
for j in range(num_mat):
    s = 0
    for i in range(num_est):
        s += notas[i][j]
    print(f"Materia {j+1}: {s / num_est}")

# %% Ejercicio 9
# Tablero Ta-Te-Ti
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Mostrar el tablero
def mostrar_tablero(t):
    for fila in t:
        print(" ".join(fila))

mostrar_tablero(tablero)

# Jugadas
for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno de {jugador}")
    fila = int(input("Ingrese fila (0-2): "))
    col = int(input("Ingrese columna (0-2): "))
    tablero[fila][col] = jugador

    # Mostrar el tablero después de cada jugada
    mostrar_tablero(tablero)

# %% Ejercicio 10
# Matriz 4x7 con ventas de 4 productos durante 7 días
ventas = [
    [5, 7, 3, 4, 6, 2, 5],   # Producto 1
    [2, 3, 4, 5, 3, 6, 7],   # Producto 2
    [8, 1, 2, 3, 4, 5, 6],   # Producto 3
    [1, 2, 3, 4, 5, 6, 7]    # Producto 4
]

# Total vendido por cada producto
print("Total por producto:")
totales_producto = []
for i in range(len(ventas)):
    total = sum(ventas[i])
    totales_producto.append(total)
    print(f"Producto {i+1}: {total}")

# Día con mayores ventas totales
totales_dia = []
for d in range(7):
    s = 0
    for p in range(4):
        s += ventas[p][d]
    totales_dia.append(s)

dia_max = totales_dia.index(max(totales_dia)) + 1
print("Día con mayores ventas totales:", dia_max)

# Producto más vendido en la semana
totales_producto = [sum(fila) for fila in ventas]
prod_max = totales_producto.index(max(totales_producto)) + 1
print("Producto más vendido en toda la semana:", prod_max)
# %%