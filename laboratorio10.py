# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:59:07 2020

@author: david
"""

# En esta parte se solicitan los valores a y b.
a = int(input('Ingrese el valor a: '))
b = int(input('Ingrese el valor b: '))

# Se crea la función para calcular el valor a elevado en el valor b.
# Si a = 0 se termina el ciclo y la función.
def a_power_b(a, b):
    cont = 0
    contImpar = 0
    contPar = 0
    while a != 0:
        acu = 1
        for i in range (0, b, 1):
            potencia = acu*a
            acu = potencia
        print('El resultado del valor a, elevado a el valor b es: ' + str(acu))
        if acu%2==0:
            contPar = contPar +1
        else:
            contImpar = contImpar + 1            
        a = int(input('Ingrese el valor a: '))
        b = int(input('Ingrese el valor b: '))
        cont +=1
    else:
        print('\nEl valor a es 0.')
    print('\nSe calcularon ' + str(cont) + ' potencias.')
    print('Se calcularon ' + str(contImpar) + ' potencias impares.')
    print('Se calcularon ' + str(contPar) + ' potencias pares.')
    
# Se ejecuta la función anteriormente creada.
a_power_b(a, b)