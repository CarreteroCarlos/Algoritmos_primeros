#
#
#

# Realizar un algoritmo para calcular el factorial de un número
# entero n, n debe ser ingresado por teclado

# Análisis: n! = 1 * 2 * 3 * ... * n 

n = int(input("Ingrese su valor aquí: "))
factorial = 1
for i in range (1, n + 1):
    factorial *= i
print(f"El resultado de su factorial sería: {factorial}")



