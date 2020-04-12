# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:01:08 2020

@author: david
"""


import numpy as np

#------Se pide el número de parejas de valores que serán ingresados-----#
long = int(input('Ingrese la cantidad de potencias que calculará: '))

#--------------------Función para calcular la potencia-------------------#
def a_power_b(a, b):
    acu = 1
    n = 0
    if b%2==0:
        while b>n:
            potencia = acu*a
            acu = potencia
            n+=1
    else:
        acu = a**b
    return acu

#-------------------------Función de la solución-------------------------#
def solucion(long):
    cont = 0
    contImpar = 0
    contPar = 0
    n=0
    #--------Se crean las listas que guardarán los números-------#
    lisA = []
    lisB = []
    while long>n:
        acu = 1
        a = int(input('Ingrese el valor a: '))
        #--------Usando append se guarda el dato en la lista--------#
        lisA.append(a)
        b = int(input('Ingrese el valor b: '))
        lisB.append(b)
        n+=1
        acu = a_power_b(a, b)
        print(' El resultado del valor a elevado a el valor b es: ' + str(acu))
        #------Se crea un condicional para guardar los contadores----#
        if acu%2==0:
            contPar = contPar +1
        else:
            contImpar = contImpar + 1
        cont +=1
    else:
        print('\nSe calcularon todas las potencias.')
    print('\nSe calcularon ' + str(cont) + ' potencias.')
    print('Se calcularon ' + str(contImpar) + ' potencias impares.')
    print('Se calcularon ' + str(contPar) + ' potencias pares.')
    #------------Se crean los arreglos para ambos valores-----------#
    listaA = np.array(lisA)
    listaB = np.array(lisB)
    print('\nValores a ingresados: ' + str(listaA))
    print('Valores b ingresados: ' + str(listaB))
    l = listaA
    #-Calculan los promedios y desviación de los arreglos llamandolos "l"-#
    promA = mean_arreglo (l, long)
    print('\nEl promedio de los valores a ingresados es: ' + 
          str(round(promA, 2)))
    prom = promA
    desv = std_arreglo(l, long, prom)
    print('La desviación estandar de los valores a ingresados es: '
          + str(round(desv, 2)))
    listaNorA = norm_arreglo(l, prom, desv, long)
    print('La normalización de los valores a ingresados es: '
          + str(listaNorA))
    l = listaNorA
    promNorA = mean_arreglo (l, long)
    print('El promedio de los valores a normalizados es: '
          + str(round(promNorA)))
    prom = promNorA
    desvNorA = std_arreglo(l, long, prom)
    print('La desviación estandar de los valores a ingresados es: '
          + str(round(desvNorA)))
    l = listaB
    promB = mean_arreglo (l, long)
    print('\nEl promedio de los valores b ingresados es: ' + 
          str(round(promB, 2)))
    prom = promB
    desv = std_arreglo(l, long, prom)
    print('La desviación estandar de los valores b ingresados es: '
          + str(round(desv, 2)))
    listaNorB = norm_arreglo(l, prom, desv, long)
    print('La normalización de los valores b ingresados es: '
          + str(listaNorB))
    l = listaNorB
    promNorB = mean_arreglo (l, long)
    print('El promedio de los valores b normalizados es: '
          + str(round(promNorB)))
    prom = promNorB
    desvNorB = std_arreglo(l, long, prom)
    print('La desviación estandar de los valores b ingresados es: '
          + str(round(desvNorB)))
    a = promA
    b = promB
    #--Se calcula la potencia de los promedios con la función ya creada--#
    acu = a_power_b(a,b)
    print('\nEl resultado del promedio de los valores a ingresados'
          ', elevado al promedio de los valores b ingresados es: ' 
          + str(round(acu, 2)))

#---------------Función que calcula el promedio de un arreglo------------#
def mean_arreglo (l, long):
    n = 0
    suma = 0
    prom = 0
    while long>n:
        suma = suma + l[n]
        prom = float(suma/long)
        n += 1
    return prom

#-------Función que calcula la desviación estándar de un arreglo--------#
def std_arreglo(l, long, prom):
    n=0
    suma=0
    while long>n:
        suma = suma + (l[n]-prom)**2
        n+=1
    desv = (suma/long)**(1/2)
    return desv

#----------Función que calcula la estandarización de arreglos------------#
def norm_arreglo(l, prom, desv, long):
    n = 0
    lis = []
    while long>n:
        dato = l[n] - prom
        estan = round(dato/desv, 2)
        lis.append(estan)
        n+=1
    lista = np.array(lis)
    return lista

# Se ejecuta la solución
solucion(long)