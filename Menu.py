# ====== FUNCIONES DE LOS EJERCICIOS ======

def datos_usuario():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    print(f"Usuario: {nombre}, Edad: {edad}")

def evaluar_numero():
    try:
        n = float(input("Ingresa un número: "))
        if n > 0:
            print("Es positivo")
        elif n < 0:
            print("Es negativo")
        else:
            print("Es cero")
    except:
        print("Entrada inválida.")

def suma_promedio():
    try:
        nums = input("Ingresa números separados por espacio: ").split()
        nums = [float(x) for x in nums]
        print(f"Suma: {sum(nums)}, Promedio: {sum(nums)/len(nums)}")
    except:
        print("Entrada inválida.")

def lista_estudiantes():
    alumnos = []
    print("Escribe nombres (ENTER para terminar):")
    while True:
        n = input("> ")
        if n == "":
            break
        alumnos.append(n)
    print("Lista final:", alumnos)

def area_rectangulo():
    try:
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("Área =", base * altura)
    except:
        print("Entrada inválida.")

def info_alumno():
    nombre = input("Nombre del alumno: ")
    carrera = input("Carrera: ")
    semestre = input("Semestre: ")
    print(f"Alumno: {nombre}, {carrera}, Semestre {semestre}")

def mostrar_todos():
    print("Aquí irían todos los datos almacenados (si los guardas en variables globales).")
    print("Demostración: función llamada correctamente.")

# ====== MENÚ PRINCIPAL ======

def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Datos del usuario")
        print("2. Evaluar número")
        print("3. Suma y promedio")
        print("4. Lista de estudiantes")
        print("5. Área de rectángulo")
        print("6. Información del alumno")
        print("7. Mostrar todos los datos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1": datos_usuario()
        elif opcion == "2": evaluar_numero()
        elif opcion == "3": suma_promedio()
        elif opcion == "4": lista_estudiantes()
        elif opcion == "5": area_rectangulo()
        elif opcion == "6": info_alumno()
        elif opcion == "7": mostrar_todos()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar menú
menu()
