# @Autor: Carlos Carretero
# Fecha: 17-08-24
# Descripción: 

# Diseñe un algoritmo para determinar si un numero real se encuentra dentro
# del rango abierto - cerrado (3.5, 7.8] = 3.5 < x <= 7.8

import math

numero = float(input("Ingrese su numero: "))
if numero > 3.5:
    if numero <= 7.8:
     print("su intervalo pertenece al rango abierto - cerrado")
else:
    print("Su numero no pertenece al intervalo abierto - cerrado")
if numero > 7.8:
    print("Su numero no pertenece al intervalo abierto - cerrado")