# @Autor: Carlos Andrés Carretero
# @Fecha: 30-08-24
# @Desc: 

#


i = int(input("Ingrese el número de terminos a calcular "))
x = float(input("Ingrese el valor X: "))

total = 0

for k in range (0, i):
    
    factorial = 1
    for j in range(1, (2* k + 1)):
        factorial = factorial * j
    
    termino_k = ((-1)**k * (x**(2*k+1)))/factorial
    total = total + termino_k
    
print(f"El total es {total}")
        



