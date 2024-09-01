#
#
#

# Realizar un algoritmo para calcular los n primeros términos de la serie de
# Fibonacci, n es un número entero mayor que 4 y debe ser ingresado por teclado

n = int(input("Ingrese su valor aquí: "))
if n < 4:
    print("El valor debe ser mayor a 4")
elif n < 0:
    print("Su valor debe ser un número positivo")
else:
    print("0")
    print("1")
    a, b = 0, 1
    for i in range(n - 2):
        a, b = b, a + b
        print(f"Su valor sería: {b}")