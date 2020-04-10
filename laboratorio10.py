# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:59:07 2020

@author: david
"""

# En esta parte se solicitan los valores a y b.
a = int(input('Ingrese el valor a: '))
b = int(input('Ingrese el valor b: '))

# Se crea la función para calcular el valor a elevado en el valor b.
def a_power_b(a, b):
    acu = 1
    for i in range (0, b, 1):
        potencia = acu*a
        acu = potencia
    print('El resultado del valor a, elevado a el valor b es: ' + str(acu))

# Se ejecuta la función anteriormente creada.
a_power_b(a, b)