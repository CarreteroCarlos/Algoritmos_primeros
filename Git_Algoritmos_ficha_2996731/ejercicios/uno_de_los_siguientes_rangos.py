#
#
#

# Diseñe un algoritmo para determinar si un número real se encuentra dentro de uno
# de los siguientes rangos: (3.5, 7.8], [9.3, 14.5) y [23.4, 45.3]

numero = float(input("Ingrese su número aquí: "))

if (numero > 3.5) and (numero <= 7.8) or (numero >= 9.3) and (numero < 14.5) or (numero >= 23.4) and (numero <= 45.3):
    print("Su valor está en alguno de los intervalos")
else:
    print("Su valor no está en alguno de los intervalos")










# ---------------------------------------------------------------    
# if numero <= 3.5:
#    print("Su valor no está dentro de uno de los intervalos")
# elif numero > 7.8:
#     print("Su valor no está dentro de uno de los intervalos")
#
# if numero < 9.3:
#    print("Su valor no está dentro de uno de los intervalos")
# elif numero >= 14.5:
#    print("Su valor no está dentro de uno de los intervalos")
    
# if numero < 23.4:
#    print("Su valor no está dentro de uno de los intervalos")
#elif numero > 45.3:
#    print("Su valor no está dentro de uno de los intervalos")