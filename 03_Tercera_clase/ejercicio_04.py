# Enunciado
# Dada una lista (lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]),
# iterarla y mostrar números divisibles por cinco, y si encuentra un 
# número mayor que 150, detenga la iteración del bucle

import os
import sys

####################################################################################
#Funciones

def borrarPantalla(): #Funcion para limpiar pantalla detectando SO
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def iterarLista(lista1):
    menorA150 = True

    for i in lista1:
        if i > 150:
            break
        if i%5 == 0:
            print(f'{i} es divisible por 5.')

####################################################################################
# Codigo principal
borrarPantalla()
lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
iterarLista(lista1)
sys.exit()