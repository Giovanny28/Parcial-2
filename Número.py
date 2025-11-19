# Capturar número
num = int(input("Ingresa un número: "))

# Determinar si es positivo, negativo o cero
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Determinar si es par o impar
if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
