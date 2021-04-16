# Enunciado
# Escribe un programa Python que acepte 5 números decimales del usuario

####################################################################################
#Funciones
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


def pedirIngreso(datoMostrar):  # Para pedir al usuario ingreso de data, recibe "texto"
    datosListos = False # Para usar de interruptor para salir de la funcion
    while datosListos == False: # Mientras no este todo ok que siga pidiendo
        valor = input(f"Ingrese el valor para {datoMostrar}:") # Pide en pantalla mostrando "texto"
        if (comprobarDigitosFloat(valor) == True): # si la comprobacion esta OK
            float(valor) # Convertimos a float los numeros
            datosListos = True # habilitamos salir de la funcion
    return valor # Devolvemos lo escrito por el usuario, comprobado y convertido a float



# Codigo principal