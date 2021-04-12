
# Enunciado
# Escribe un programa Python que acepte un número entero (n) 
# y calcule el valor de n + nn + nnn

def comprobacion(numero):
    validado = True
    indice = 0

    #chequeo que la cadena sean componentes de entero
    for i in numero:
        if (i != '0') and (i != '1') and (i != '2') and (i != '3') and (i != '4') and (i != '5') and (i != '6') and (i != '7') and (i != '8') and (i != '9') and (i != '-'):
            validado = False
        if (i == '-') and (indice != 0):
            validado = False
        indice += 1
   
    #print(f"Validacion funcion {validado}")
    return validado

validado = False

while validado != True:
    numero = input("Ingrese el numero entero para hacer los cálculos: ")
    validado = comprobacion(numero)
    #print(validado)

n = int(numero)
nn = (n * n)
nnn = (n * n) * n
total = n + (nn) + (nnn)

print(f"El resultado es: N= {n}, NN= {nn}, NNN= {nnn}, total= {total}")


        
            


