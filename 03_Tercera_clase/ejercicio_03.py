# Enunciado
# Escribe un programa en Python que reciba 5 números enteros del usuario 
# y los guarde en una lista. Luego recorrer la lista y mostrar los números 
# por pantalla.

import os
import sys

####################################################################################
#Funciones

def borrarPantalla(): #Funcion para limpiar pantalla detectando SO
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def comprobarDigitosEnteros(valorComprobar): #comprobacion de los valores ingresados por el usuario
    validado = True # Interruptor para salir de la funcion además de valor a devolver
    indice = 0 # Para comprobar cuando se ingrese el guion, si es para un numero negativo
    #chequeo que la cadena sean componentes de entero
    for i in valorComprobar:
        if (i != '0') and (i != '1') and (i != '2') and (i != '3') and (i != '4') and (i != '5') and (i != '6') and (i != '7') and (i != '8') and (i != '9') and (i != '-'):
            validado = False
        if (i == '-') and (indice != 0):
            validado = False
        indice += 1
    return validado #Si lo ingresado son componentes de un entero devuelve TRUE


def pedirIngreso(datoMostrar, posicion):  # Para pedir al usuario ingreso de data, recibe "texto"
    datosListos = False # Para usar de interruptor para salir de la funcion
    while datosListos == False: # Mientras no este todo ok que siga pidiendo
        valor = input(f"Ingrese el valor para {datoMostrar} en posición {posicion}:") # Pide en pantalla mostrando "texto"
        if (comprobarDigitosEnteros(valor) == True): # si la comprobacion esta OK
            int(valor) # Convertimos a enteros los numeros
            datosListos = True # habilitamos salir de la funcion
    return valor # Devolvemos lo escrito por el usuario, comprobado y convertido a float


def cargarEnteros(cantidad, numerosEnteros):
    indice = 0
    while indice != cantidad:
        numerosEnteros.append(pedirIngreso('Guardar', indice+1))
        indice += 1
    return numerosEnteros


def mostrarCargados(texto, numerosEnteros):
    indice = 1
    print(f"{texto} cargados: ")
    for i in numerosEnteros:
        print(f'Número {indice}: {i}')
        indice += 1

####################################################################################
# Codigo principal
borrarPantalla()
numerosEnteros = [ ]
numerosEnteros = cargarEnteros(5, numerosEnteros)
mostrarCargados('Números', numerosEnteros)
sys.exit()