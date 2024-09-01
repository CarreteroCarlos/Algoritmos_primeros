# @Author: Carlos Andrés Carretero
# @Fecha: 16-08-24
# Descripción:

	#Diseñe un algoritmo que reciba el nombre de un estudiante, el nombre de la asignatura y las 3 notas parciales entre 0.0 y 2.0
	#el algoritmo debe:
	#- Mostrar nombre del estudiante y asignatura
	#- Calcular y mostrar la nota definitiva
	#- Un mensaje si el estudiante gana el cursio (Si obtiene una nota definitiva mayor a 3.5
	#caracteres aski / código aski

import math

nombre = input("ingrese el nombre del estudiante: ")
asignatura = input("Ingrese el nombre de la asignatura: ")
nota1 = float(input("ingrese la nota parcial 1: "))
nota2 = float(input("Ingrese la nota parcial 2: "))
nota3 = float(input("Ingrese la nota parcial 3: "))

nota_definitiva = (nota1 + nota2 + nota3) / 3

if nota_definitiva >= 3.5:
    aprobo = "Si"
else:
    aprobo = "Si"

if nota_definitiva < 3.5:
    aprobo2 = "No"
else:
    aprobo2 = "No"


if nota_definitiva > 5:
    print("La nota es mayor a 5, no puede agregar valores superiores a 5")
else:
     if nota_definitiva > 3.5:
        print(f""" 
            ┌──────────────────┬──────────────────────┬──────┬──────┬──────┬───────────┬───────┬───────────┐
	      │{"NOMBRE":<18}│{"ASIGNATURA":<20}│{"NOTA 1":<6}│{"NOTA 2":<6}│{"NOTA3":<6}│{"DEFINITIVO":<11}│{"APROBÓ":<7}│{"NO APROBÓ":<10}│
	      ├──────────────────┼────────────────────┼──────┼──────┼──────┼───────────┼───────────────────────│
	      │{nombre:<18}│{asignatura:<20}│{nota1:<6}│{nota2:<6}│{nota3:<6}│{nota_definitiva:<11}│{aprobo:<7}│{aprobo2:<10}│
	      └──────────────────┴────────────────────┴──────┴──────┴──────┴───────────┴───────────┴───────────┘""")
     else:
         print("Su nota es inferior a 3.5 por ende perdió el año")
         print(f"""
          ┌──────────────────┬──────────────────────┬──────┬──────┬──────┬───────────┬───────┬───────────┐
	      │{"NOMBRE":<18}│{"ASIGNATURA":<20}│{"NOTA 1":<6}│{"NOTA 2":<6}│{"NOTA3":<6}│{"DEFINITIVO":<11}│{"APROBÓ":<7}│{"NO APROBÓ":<10}│
	      ├──────────────────┼────────────────────┼──────┼──────┼──────┼───────────┼───────────────────────│
	      │{nombre:<18}│{asignatura:<20}│{nota1:<6}│{nota2:<6}│{nota3:<6}│{nota_definitiva:<11}│{aprobo:<7}│{aprobo2:<10}│
	      └──────────────────┴────────────────────┴──────┴──────┴──────┴───────────┴───────────┴───────────┘""")