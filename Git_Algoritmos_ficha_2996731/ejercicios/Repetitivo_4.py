# @Autor: Carlos Andrés Carretero
# @Fecha: 21-08-24
# @Desc: 

# Realizar un algoritmo para calcular el salario y la prima extrlgal
# los datos ingresados son:
# identificacion, nombres, salario base.
# La prima extralegal se calcula deacuerdo con el salario neto
# si el salario neto es menor que 1200000 tiene una prima extralegal de
# 16% y si es mayor será del 7%
# Se debe imprimir para cada empleado:
# La identificacion, los nombres, el salario base, la deduccion por salud(4%)
# la deduccion por pensión(4.5%), el salario neto y la prima extralegal
# El primer empleado deben ser sus datos reales 




for i in range(1, 6):
    
    identificacion = input("Ingrese la identificación del trabajador: ")
    nombre = input("Ingrese el nombre del empleado: ")
    salario_base = float(input("Ingrese el salario base del empleado: "))
    
    salud = salario_base * 0.045
    pension = salario_base * 0.04
    salario_neto = salario_base - (salud + pension)
    
    if salario_neto < 1200000:
        prima = salario_neto * 0.16
    else:
        prima = salario_neto * 0.07

    print(f"El emlpeado identificado como {identificacion}, llamado {nombre}, y con un salario de {salario_base}")
    print(f"Tiene una deducción de salud de: {salud}")
    print(f"Su deducción de pensión sería de: {pension}")
    print(f"Su salario base sería de: {salario_neto}")
    print(f"Su prima extralegal sería de: {prima}")