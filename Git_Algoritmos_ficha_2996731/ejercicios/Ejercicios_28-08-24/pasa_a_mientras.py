# @Autor: Carlos Andrés Carretero
# @Fecha: 28-08-24
# @Desc: 

# Reescribir el algoritmo "Repetitivo_4.py" 
# (algoritmo de la nómina)
# Con un ciclo "mientras"
# - Validar la respuesta -
# - Validar el salario base -

# if salario_neto < 1200000:
#        prima = salario_neto * 0.16
#    else:
#        prima = salario_neto * 0.07


# respuesta = int(input("Ingrese su identificación"))
# while respuesta.upper() != 'N' and respuesta.upper() != 'S':

#salud = salario_base * 0.045
#            pension = salario_base * 0.04
#            salario_neto = salario_base - (salud + pension)
#    
#            if salario_neto < 1200000:
#                prima = salario_neto * 0.16
#            else:
#                prima = salario_neto * 0.07
#
#            print(f"El emlpeado identificado como {identificacion}, llamado {nombre}, y con un salario de {salario_base}")
#            print(f"Tiene una deducción de salud de: {salud}")
#            print(f"Su deducción de pensión sería de: {pension}")
#            print(f"Su salario base sería de: {salario_neto}")
#            print(f"Su prima extralegal sería de: {prima}")

#respuesta = input("¿desea ingresar valores? [S/N] ")
#    while respuesta.upper() != 'N' and respuesta.upper() != 'S':
#        print("Sólo se debe ingresar S o N")
#        respuesta = input("¿desea ingresar valores? [S/N] ")


respuesta = input("¿desea ingresar valores? [S/N] ")
while respuesta.upper() != 'N' and respuesta.upper() != 'S':
    print("Sólo se debe ingresar S o N ")
    respuesta = input("¿desea ingresar valores? [S/N] ")
while respuesta.upper() != 'N':
    
    while True:
        identificacion = input("Ingrese su identificación: ")
        try:
            identificacion = int(identificacion) #cambiar a caracter y que sea solo de numeros
            break
        except ValueError:
            print("Sólo debe ingresar valores númericos / enteros")
            
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.isalpha(): #colocar espacios
            print("El nombre ingresado es válido")
            break
        else:
            print("el nombre ingresado no puede tener caracteres especiales ")
            
    
    while True:
        salario_base = input("Ingrese el salario base del empleado: ")
        try:
            salario_base = float(salario_base)
            if salario_base <= 0:
                print("Su valor debe ser superior a 0 ")
            else:
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
            break
        except ValueError:
            print("Debe ingresar un valor numerico en realeas. ")
    
    while True:
        print("¿Deseas continuar? [S/N]: ")
        respuesta = input().upper()
        if respuesta == respuesta.upper() != 'N':
            print("Continuando... ")
            continue
        elif respuesta == respuesta.upper() != 'S':
            print("Saliendo... ")
            break
        else:
            print("Opción no válida, inténtalo de nuevo. ")
    
   

            
    
            
        
    