import math

# Enunciado:
# Escribe un programa Python que acepte el radio de un círculo del 
# usuario y calcule el área

# Debo agregarle los procesos de control aún

radio = float(input("Ingrese el radio a calcular: "))

area = (radio * radio) * math.pi

print(f"Para el radio {radio} el área es {area}")