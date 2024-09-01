


# @Autor: Carlos Andrés Carretero.
# @fecha: 14-08-24
# @Descripción: Programa en python

#                    programa que permite adicionar una prima extralegal del 15% sobre el salario de una persona
#                    cuya edad sea mayor a 27 años.

nombre = input(" ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
salario = float(input("ingrese el salaio del empleado: "))

if edad > 27:
        prima_extralegal = salario * 0.15
        print("nombre: ", nombre)
        print("edad: ", edad)
        print("salario: ", salario)
        print("prima extralegal", prima_extralegal)
