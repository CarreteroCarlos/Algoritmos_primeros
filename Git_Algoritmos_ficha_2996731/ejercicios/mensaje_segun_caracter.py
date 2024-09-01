# @Autor: Carlos Andrés Carretero
# Fecha: 17-08-24
# Descripción:

# Realice un algoritmo que permita mostrar un mensaje según
# un caratcer ingresado por teclado, independientemente de si es
# ingresado en mayúsculas o minúsculas

import math
valor_ingresado = input("Ingrese su caracter: ")

if valor_ingresado.lower() == 'a':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Angola 🗺️                    │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'b':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Brasil 🗺️                    │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'c':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Colombia 🗺️                  │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'd':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Dinamarca 🗺️                 │
          └─────────────────────┴─────────────────────────────┘""")
    
elif valor_ingresado.lower() == 'e':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ España 🗺️                    │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'f':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Finlandia 🗺️                 │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'g':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Guatepeor 🗺️                 │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'h':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Honduras 🗺️                  │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'i':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Inglaterra 🗺️                │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'j':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Japón 🗺️                     │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'k':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Kazajistan 🗺️                │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'l':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ lituania 🗺️                  │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'm':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ México 🗺️                    │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'n':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Noruega 🗺️                   │
          └─────────────────────┴─────────────────────────────┘""")

elif valor_ingresado.lower() == 'ñ':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ ñame 🤣                      │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'o':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Oman 🗺️                      │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'p':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Perú 🗺️                      │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'q':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Qatar 🗺️                     │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'r':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Rusia 🗺️                     │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 's':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Sri lanka 🗺️                 │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 't':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Trinidad y tobago 🗺️         │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'u':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Uruguay 🗺️                   │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'v':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Vietnam 🗺️                   │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'w':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ wallis y futuna 🗺️           │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'x':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Xinaloa 🗺️                   │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'y':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ yemen 🗺️                     │
          └─────────────────────┴─────────────────────────────┘""")
elif valor_ingresado.lower() == 'z':
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Zambia 🗺️                   │
          └─────────────────────┴─────────────────────────────┘""")
else:
    print("Su valor no se encuentra disponible")
    print("Ingrese un valor que pertenezca a una letra del abecedario")
    print(f"""
          ┌─────────────────────┬─────────────────────────────┐
          │Valor ingresado:     │ Resultado:                  │
          ├─────────────────────┼─────────────────────────────┘
          │{valor_ingresado:<21}│ Syntaxis error 🚫            │
          └─────────────────────┴─────────────────────────────┘""")

