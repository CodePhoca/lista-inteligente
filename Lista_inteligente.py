"""
Nombre del programa: Lista_inteligente.py
Objetivo: Crear una Lista de Compras Inteligente
Fecha: 15/06/2026
Programado por: PhocaDev
Modificado por: PhocaDev

"""

print("""
╔════════════════════════════════════════════════════╗
║      ¡Bienvenido a tu lista del supermercado!      ║
╚════════════════════════════════════════════════════╝

====================== MENÚ ======================

1. Salir
2. Ver cantidad de productos
""")

compras = []

while True:
    
    artículos  = input("¿Qué deseas comprar? ")
    
    if artículos  == "1":
        break
    elif artículos  == "2":
        productos = len(compras)
        print(f"Tienes {productos} en la lista por el momento")
    else: 
        compras.append(artículos)

#Ordena los productos de la A a la Z.
compras.sort()
print(f"Tienes que comprar {compras}")

print("===============================")
for i in compras:
    print(f"Hace falta {i}")

