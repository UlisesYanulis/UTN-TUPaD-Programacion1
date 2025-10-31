# Práctico 7: Estructuras de datos complejas

# %% Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# %% Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800


# %% Ejercicio 3
frutas = list(precios_frutas.keys())

# %% Ejercicio 4
agenda = {}

for i in range(5):
    nombre = input(f"Ingresar nombre #{i+1}: ")
    numero = input(f"Ingresar número #{i+1}: ")
    agenda[nombre] = numero

consulta = input("Buscar nombre: ")
if consulta in agenda:
    print(f"Nombre: {consulta} | Número: {agenda[consulta]}")


# %% Ejercicio 5
frase = input("Ingresá una frase: ")

palabras = frase.split()

unicas = set(palabras)

frecuencias = {}
for p in palabras:
    if p in frecuencias:
        frecuencias[p] += 1
    else:
        frecuencias[p] = 1

print("Resultado:")
print("Palabras únicas (set):", unicas)
print("Frecuencias (diccionario):", frecuencias)


# %% Ejercicio 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno #{i+1}: ")
    n1 = float(input("Ingresá nota 1: "))
    n2 = float(input("Ingresá nota 2: "))
    n3 = float(input("Ingresá nota 3: "))
    alumnos[nombre] = (n1, n2, n3)  # tupla

print("Resultado:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre} Promedio: {promedio}")


# %% Ejercicio 7
# Sets de números
parcial1 = {101, 102, 105, 110, 115}
parcial2 = {102, 106, 110, 120}

ambos = parcial1 & parcial2              # intersección
solo_uno = parcial1 ^ parcial2           # sólo uno (diferencia simétrica)
al_menos_uno = parcial1 | parcial2       # unión (sin repetir)

print("Resultado:")
print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)


# %% Ejercicio 8
stock = {
    "arroz": 10,
    "fideos": 6,
    "leche": 12,
    "azucar": 8,
    "aceite": 4
}

producto = input("Ingresá nombre del producto: ")

if producto in stock:
    print(f"Stock actual de '{producto}': {stock[producto]}")
    agregar = int(input("Ingresá unidades a agregar: "))
    stock[producto] += agregar
else:
    print("El producto no existe.")
    unidades = int(input("Ingresá stock inicial para agregar el producto: "))
    stock[producto] = unidades

print("Resultado:")
print(f"Producto: {producto} | Stock: {stock[producto]}")

# Mostrar stock completo
print("\nStock completo:")
for nombre, cantidad in stock.items():
    print(f"- {nombre}: {cantidad}")


# %% Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "14:30"): "Gimnasio",
    ("Viernes", "09:00"): "Clases"
}

dia = input("Ingresá el día (ej: Lunes): ")
hora = input("Ingresá la hora (formato HH:MM, ej: 10:00): ")

evento = agenda.get((dia, hora))

print("Resultado:")
if evento:
    print(f"({dia}, {hora}) -> {evento}")
else:
    print(f"({dia}, {hora}) -> No hay actividad registrada")

# %% Ejercicio 10
# Diccionario dado: país -> capital
pais_a_capital = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Construir el nuevo diccionario: capital -> país
capital_a_pais = {}
for pais, capital in pais_a_capital.items():
    capital_a_pais[capital] = pais

print("Resultado:")
print("Original (país -> capital):", pais_a_capital)
print("Invertido (capital -> país):", capital_a_pais)

# %%