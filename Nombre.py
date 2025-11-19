# Capturar 5 nombres
nombres = []

for i in range(5):
    nombre = input(f"Ingresa el nombre {i+1}: ")
    nombres.append(nombre)

# Mostrar resultados
print("\nLista original:", nombres)
print("Primer elemento:", nombres[0])
print("Último elemento:", nombres[-1])
print("Lista ordenada:", sorted(nombres))
