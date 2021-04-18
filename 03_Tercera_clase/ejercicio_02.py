# Enunciado
# Escribe un programa Python que acepte 5 números decimales del usuario

import os
import sys


####################################################################################
#Funciones

def borrarPantalla(): #Funcion para limpiar pantalla detectando SO
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def comprobarDigitosFloat(valorComprobar): #comprobacion de los valores ingresados por el usuario
    validado = True # Interruptor para salir de la funcion además de valor a devolver
    indice = 0 # Para comprobar cuando se ingrese el guion, si es para un numero negativo
    #chequeo que la cadena sean componentes de float
    for i in valorComprobar:
        if (i != '0') and (i != '1') and (i != '2') and (i != '3') and (i != '4') and (i != '5') and (i != '6') and (i != '7') and (i != '8') and (i != '9') and (i != '-') and (i !='.'):
            validado = False
        if (i == '-') and (indice != 0):
            validado = False
        indice += 1
    return validado #Si lo ingresado son componentes de un float devuelve TRUE


def pedirIngreso(datoMostrar, posicion):  # Para pedir al usuario ingreso de data, recibe "texto"
    datosListos = False # Para usar de interruptor para salir de la funcion
    while datosListos == False: # Mientras no este todo ok que siga pidiendo
        valor = input(f"Ingrese el valor para {datoMostrar} en posición {posicion}:") # Pide en pantalla mostrando "texto"
        if (comprobarDigitosFloat(valor) == True): # si la comprobacion esta OK
            float(valor) # Convertimos a float los numeros
            datosListos = True # habilitamos salir de la funcion
    return valor # Devolvemos lo escrito por el usuario, comprobado y convertido a float


def cargarDecimales(cantidad, numerosDecimales):
    indice = 0
    while indice != cantidad:
        numerosDecimales.append(pedirIngreso('Guardar', indice+1))
        indice += 1
    return numerosDecimales


def mostrarCargados(texto, numerosDecimales):
    indice = 1
    print(f"{texto} cargados: ")
    for i in numerosDecimales:
        print(f'Número {indice}: {i}')
        indice += 1


####################################################################################
# Codigo principal

borrarPantalla()
numerosDecimales = [ ]

numerosDecimales = cargarDecimales(5, numerosDecimales)

mostrarCargados('Números', numerosDecimales)

sys.exit()





