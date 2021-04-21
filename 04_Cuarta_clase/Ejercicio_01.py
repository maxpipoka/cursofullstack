# Enunciado
# Escribe una clase de Python llamada Rectangulo que se define por una longitud y 
# un ancho y un método que calculará el área de un rectángulo.

### Imports #######################
import os
import sys

### Funciones #######################

def borrarPantalla(): #Funcion para limpiar pantalla detectando SO
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


### Clases #######################

class Rectangulo(self, longitud, ancho):

    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

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
    


        


### Main #######################

