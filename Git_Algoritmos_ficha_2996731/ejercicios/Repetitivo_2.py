# @Autor: Carlos Andrés Carretero
# @Fecha: 21-08-24
# @Desc: 

# Realizar un algoritmo que realice la sumatoria de los números
	# entre 1 y n
	# n debe ser ingresado por el teclado.
 
total = 0
n = int(input("Ingrese un valor entero positivo mayor a 1: "))

for i in range(1, n + 1):
    total += i
    
print(f"La sumatoria de los numeros enteros entre 1 y {n} es {total}")