# Enunciado
# Escribe un programa en Python que acepte una cadena de caracteres y cuente 
# el tamaño de la cadena y cuantas veces aparece la letra A 
# (mayuscula y minúscula)

largoCadena = 0
aMayuscula = 0
aMinuscula = 0
cadena = input("Ingrese la cadena a procesar: ")

for i in cadena:
    largoCadena += 1
    if i == 'A':
        aMayuscula += 1
    if i == "a":
        aMinuscula += 1

