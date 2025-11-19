def datos_usuario():
    n = input("Nombre: "); e = input("Edad: "); c = input("Carrera: ")
    print(f"Hola {n}, estudias {c} y tienes {e} años.")

def evaluar_numero():
    try:
        x = float(input("Número: "))
        print("Positivo" if x>0 else "Negativo" if x<0 else "Cero")
        print("Par" if x%2==0 else "Impar")
    except: print("Inválido")

def suma_promedio():
    try:
        n = int(input("¿Cuántos?: "))
        nums = [float(input("> ")) for _ in range(n)]
        print("Cantidad:", n, "Suma:", sum(nums), "Promedio:", sum(nums)/n)
    except: print("Inválido")

def lista_estudiantes():
    l = [input(f"Nombre {i+1}: ") for i in range(5)]
    print("Original:", l, "\nPrimero:", l[0], "\nÚltimo:", l[-1], "\nOrdenada:", sorted(l))

def area_rectangulo():
    try:
        b = float(input("Base: ")); a = float(input("Altura: "))
        print("Área:", b*a)
    except: print("Inválido")

def info_alumno():
    n=input("Nombre: "); m=input("Matrícula: "); c=input("Carrera: ")
    try:
        p=float(input("Promedio: "))
        print(f"Alumno: {n} ({m})\nCarrera: {c}\nPromedio: {p}\nEstado:", "Aprobado" if p>=7 else "Reprobado")
    except: print("Inválido")

def mostrar_todo():
    print("Mostrar todo (personalizable).")

def menu():
    while True:
        print("\n=== MENÚ ===\n1.Datos\n2.Evaluar\n3.Suma\n4.Lista\n5.Rectángulo\n6.Alumno\n7.Todo\n0.Salir")
        op = input("> ")
        if   op=="1": datos_usuario()
        elif op=="2": evaluar_numero()
        elif op=="3": suma_promedio()
        elif op=="4": lista_estudiantes()
        elif op=="5": area_rectangulo()
        elif op=="6": info_alumno()
        elif op=="7": mostrar_todo()
        elif op=="0": break
        else: print("Inválido")

menu()
