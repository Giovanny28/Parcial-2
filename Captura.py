# Pedir cuántos números se van a capturar
n = int(input("¿Cuántos números quieres ingresar? "))

suma = 0  # Acumulará la suma de todos los números

# Capturar n números
for i in range(n):
    num = float(input(f"Ingresa el número {i+1}: "))
    suma += num

# Calcular promedio
promedio = suma / n if n > 0 else 0

# Mostrar resultados
print("\nCantidad ingresada:", n)
print("Suma total:", suma)
print("Promedio:", promedio)
