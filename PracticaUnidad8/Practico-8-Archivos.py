# Práctico 8: Archivos

#%%

import os

# 1) Crear archivo inicial con tres productos
if not os.path.exists("productos.txt"):
    with open("productos.txt", "w") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,950.0,15\n")
        f.write("Goma,80.0,50\n")

# 4) Cargar productos en una lista de diccionarios al leer el archivo
productos = []
with open("productos.txt", "r") as f:
    for linea in f:
        linea = linea.strip()
        if linea == "":
            continue
        partes = linea.split(",")
        nombre = partes[0]
        precio = float(partes[1])
        cantidad = int(partes[2])
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

# 2) Mostrar productos
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# 3) Agregar uno o más productos
while True:
    print("\nIngresá un nuevo producto:")
    nuevo_nombre = input("Nombre: ")
    nuevo_precio = float(input("Precio: "))
    nueva_cantidad = int(input("Cantidad: "))

    # Se agrega al archivo
    with open("productos.txt", "a") as f:
        f.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")

    # Se agrega a la lista
    productos.append({"nombre": nuevo_nombre, "precio": nuevo_precio, "cantidad": nueva_cantidad})

    seguir = input("¿Agregar otro? (s/n): ").strip().lower()
    if seguir != "s":
        break

# 5) Buscar producto por nombre
buscado = input("\nIngresá el nombre de un producto para buscar: ")
encontrado = None
for p in productos:
    if p["nombre"].lower() == buscado.lower():
        encontrado = p
        break

if encontrado is not None:
    print(f"Producto encontrado -> Producto: {encontrado['nombre']} | Precio: ${encontrado['precio']} | Cantidad: {encontrado['cantidad']}")
else:
    print("Error: el producto no existe.")

# 6) Guardar los productos sobrescribiendo el archivo
with open("productos.txt", "w") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

# %%
