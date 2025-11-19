# Crear diccionario del alumno
alumno = {}

# Capturar datos
alumno["nombre"] = input("Nombre del alumno: ")
alumno["matricula"] = input("Matrícula: ")
alumno["carrera"] = input("Carrera: ")
alumno["promedio"] = float(input("Promedio: "))

# Determinar estado
estado = "Aprobado" if alumno["promedio"] >= 7 else "Reprobado"

# Mostrar resultados
print(f"\nAlumno: {alumno['nombre']} ({alumno['matricula']})")
print(f"Carrera: {alumno['carrera']}")
print(f"Promedio: {alumno['promedio']}")
print(f"Estado: {estado}")
