# @Autor: Carlos Andrés Carretero
# Fecha: 17-08-24
# Descripción:

# Diseñe un algoritmo que permita determinar el mayor de dos numeros enteros
# el algoritmo debe solicitar los numeros

numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))



if numero1 > numero2:
    print(f"""{numero1} Es mayor que {numero2}""")
else:
    print(f"""{numero2} Es mayor que {numero1}""")