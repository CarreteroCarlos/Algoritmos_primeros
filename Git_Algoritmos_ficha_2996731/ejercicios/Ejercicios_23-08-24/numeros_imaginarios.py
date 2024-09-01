#
#
#

# - Realizar un algoritmo para calcular la suma, resta, multiplicación y división de 
#  números imaginarios.  Los números imaginarios deben ser ingresados por teclado.
#  Se deben realizar las operaciones para 5 pares de números imaginarios.

# Análisis: un número imaginario es un numero de la forma a ± bi ó (a, b)
# suma: (a ± bi) ± (c ± di) = (a ± c) ± (b ± d)i

# a + bj
for i in range(1, 5):
    n = int(input("Ingrese su primer valor real aquí: "))
    n2 = int(input("Ingrese su primer valor imaginario aquí: "))
    n3 = int(input("Ingrese su segundo valor real aquí: "))
    n4 = int(input("Ingrese su segundo valor imaginario aquí: "))


    valor_1_suma = complex(n, n2)
    valor_2_suma = complex(n3, n4)
    
    valor_total_suma = complex(valor_1_suma + valor_2_suma)
    valor_total_resta = complex(valor_1_suma - valor_2_suma)
    valor_total_mult = complex(valor_1_suma * valor_2_suma)
    valor_total_div = complex(valor_1_suma / valor_2_suma)

    print(f"{valor_total_suma} es su resultado de suma.")
    print(f"{valor_total_resta} es su resultado de suma.")
    print(f"{valor_total_mult} es su resultado de suma.")
    print(f"{valor_total_div} es su resultado de suma.")
# resta:

