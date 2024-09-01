# @Autor: Carlos Andrés Carretero
#@Fecha: 17-08-24
#    @descripción: Diseñe un algoritmo que permita solicitar tanto el nombre
#    como la edad de una persona, y posteriormente indicar si esa
#    persona es mayor o menor de edad, según la info indicada.
#    Una persona se considera mayor de edad después de sus 18 añitos

import math

edad = float(input("Ingrese su edad: "))
nombre = input("Ingrese su nombre: ")

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")