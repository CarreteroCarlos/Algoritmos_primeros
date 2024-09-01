# @Autor: Carlos Andrés Carretero
# @Fecha: 28-08-24
# @Desc: 

# Realizar un algoritmo para realizar la suma de valores
# ingresados por teclado
# El algoritmo termina cuando el usuario responde con una
# respuesta (o palabra / letra) "n" o "N"
# el algoritmo debe mostrar el número de valores ingresados.
# El algoritmo debe validar la respuesta con letras "s, S" y "n, N"
# De lo contrario debe solicitar una nueva respuesta
# El algoritmo debe validar los valores ingresados
# ---El programa también valida los valores ingresados---


total = 0
conteo_valores = 0
respuesta = input("¿desea ingresar valores? [S/N] ")

while respuesta.upper() != 'N' and respuesta.upper() != 'S':
    print("Sólo se debe ingresar S o N")
    respuesta = input("¿desea ingresar valores? [S/N] ")
    
while respuesta.upper() != 'N':
    
    while True:
        vlr = input("Ingrese un valor: ")
        try:
            vlr = int(vlr)
            break
        except ValueError:
            print("Sólo debe ingresar valores enteros ...")
        
    total += vlr
    conteo_valores += 1
    
    respuesta = input("¿desea ingresar valores? [S/N] ")
    while respuesta.upper() != 'N' and respuesta.upper() != 'S':
        print("Sólo se debe ingresar S o N")
        respuesta = input("¿desea ingresar valores? [S/N] ")

print(f"""El total de los valores es: {total}
      El número de valores ingresados es {conteo_valores}""")