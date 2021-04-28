# Enunciado
# Escribe una clase de Python llamada Rectangulo que se define por una longitud y 
# un ancho y un método que calculará el área de un rectángulo.

### Imports #######################
import os
import sys

### Funciones #######################

###### Funcion para limpiar pantalla detectando SO
def borrarPantalla(): 
    if os.name == "posix":      #Si es unix o linux
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":    #Si es windows
        os.system ("cls")

###### Comprobacion de los valores ingresados por el usuario, recibe "valor" como "valorComprobar"
def comprobarDigitosFloat(valorComprobar): 
    validado = True     #Interruptor para finalizar funcion
    indice = 0      #Para comprobar si el primer caracter es un guion
    digitosFloat = ['0', '1', '2', '3', '4', '5', '6', '8', '9', '0', '-', '.']
    for i in valorComprobar:    #chequeo que la cadena sean componentes de float
        if i not in digitosFloat:
            validado = False
        if (i == '-') and (indice != 0):    #Si es un guion y no es el primer caracter
            validado = False
        indice += 1
    return validado     #Si lo ingresado son componentes de un float devuelve TRUE


###### Para pedir al usuario ingreso de data, recibe "texto"
def pedirIngreso(texto):
    datosListos = False     #Interruptor para salir de la funcion
    while datosListos == False:     #Mientras no este todo ok que siga pidiendo
        valor = input(f"Ingrese el valor para {texto}: ") # Pide en pantalla mostrando "texto"
        if (comprobarDigitosFloat(valor) == True): # si la comprobacion esta OK
            float(valor) # Convertimos a float los numeros
            datosListos = True # habilitamos salir de la funcion
    return valor # Devolvemos lo escrito por el usuario, comprobado y convertido a float

### Clases #######################

class Rectangulo:

    def __init__(self, longitud, ancho):
        self.longitud = float(longitud)
        self.ancho = float(ancho)

    def __str__(self):
        return f'Longitud: {self.longitud}, Ancho: {self.ancho}'

    def getLongitud(self):
        return self.longitud

    def getAncho(self):
        return self.ancho

    def setLongitud(self, longitud):
        self.longitud = longitud

    def setAncho(self, ancho):
        self.ancho = ancho

    def calcularArea(self):
        return (self.longitud) * (self.ancho)
    

### Main #######################
borrarPantalla()

l = pedirIngreso('Longitud')
a = pedirIngreso('Ancho')

nR = Rectangulo(l,a)
area = nR.calcularArea()
print(f'El area del rectangulo es de: {area}')
