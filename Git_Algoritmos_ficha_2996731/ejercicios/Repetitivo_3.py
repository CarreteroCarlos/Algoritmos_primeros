# @Autor: Carlos Andrés Carretero
# @Fecha: 21-08-24
# @Desc: 

# Realizar un algoritmo que realice la sumatoria de los números
	# entre 1 y n
	# n debe ser ingresado por el teclado.
 
 
n = int(input("Ingrese un valor: "))

# primera forma: utilizando un condicional

for i in range( 1, n + 1):
     if i % 8 == 0:
         print(f"{i} es multiplo de 8")
         
