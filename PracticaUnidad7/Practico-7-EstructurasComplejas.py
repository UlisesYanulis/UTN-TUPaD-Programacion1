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

for _ in range(5):
    nombre = input("Ingresar nombre: ")
    numero = input("Ingresar número: ")
    agenda[nombre] = numero

consulta = input("Buscar nombre: ")
if consulta in agenda:
    print(f"Nombre: {consulta}  Número: {agenda[consulta]}")

# %% Ejercicio 5


# %% Ejercicio 6


# %% Ejercicio 7


# %% Ejercicio 8


# %% Ejercicio 9


# %% Ejercicio 10
