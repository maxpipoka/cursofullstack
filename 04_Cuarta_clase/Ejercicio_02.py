# Enunciado
# Crea una clase Minibus que herede de la clase Vehiculo. Debes poder tener 
# un método capacidad() que defina por defecto la capacidad de 6 asientos. 
# Luego crea una clase Pasajero que puedas ir agregando a una instancia de 
# Minibus. Esa instancia no deberá permitir mas de 50 pasajeros únicos (no 
# se permiten pasajeros repetidos).

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



### Main #######################