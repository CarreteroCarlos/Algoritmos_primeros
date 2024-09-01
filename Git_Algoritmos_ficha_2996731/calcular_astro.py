# @Author: Carlos Andrés Carretero
# @Fecha: 16-08-24
# Descripción:

# Programa que muestra un mensaje de acuerdo con la circunferencia de un astro esférico con respecto al sol.
# Se solicitará el radio del astro por teclado.
# El mensaje se mostrará solamente si la circunferencia del astro es mayor que la circunferencia del sol


import math 

radio_astro = float(input("Ingrese el radio del astro: "))

circunferencia_astro = 2 * math.pi * radio_astro

radio_sol = 696340
diametro_sol = 2 * radio_sol
circunferencia_sol = 2 * math.pi * radio_sol

if circunferencia_astro > circunferencia_sol:
    print(f"""
        ¡Su astro tiene una circunferencia mayor a la del sol!,
        y su valor sería: {circunferencia_astro}
        El sol tiene una circunferencia de: {circunferencia_sol}""")