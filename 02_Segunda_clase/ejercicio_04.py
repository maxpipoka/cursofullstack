# Enunciado
# Escribe un programa en Python que muestre la hora actual con una suma de 
# dos horas adicionales

from datetime import datetime

print("Este programa imprimirá la hora actual del sistema")
print("sumandole dos horas mas...")

actual = datetime.now()
print(f"La hora actual es {actual.hour}:{actual.minute}:{actual.second}")
print(f"La hora actual + 2 es {actual.hour + 2}:{actual.minute}:{actual.second}")