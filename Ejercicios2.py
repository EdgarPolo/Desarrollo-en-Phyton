# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:18:38 2021

@author: Edgar_Polo
"""
# Taller numero 2
# Ejercicio # 1
Valor_Camisa = float(input("Digite el valor de la camisa"))
No_Camisa = float(input("Digite el numero de camisa"))
No_Valor = Valor_Camisa * No_Camisa
Descuento3 = No_Valor * 0.30
Descuento3_total = No_Valor - Descuento3
Descuento1 = No_Valor * 0.10
Descuento1_total = No_Valor - Descuento3
if (No_Camisa >= 3):
    print(Descuento3_total)
else:
    print(Descuento1_total)

# EJERCICIO 2
Numero_Azar = float(input("Inserte el número obtenido: "))
Valor = float(input("Inserte el valor de la compra: "))
Primer_Descuento = Valor * 0.15
Costo_1 = Valor - Primer_Descuento
Segundo_Descuento = Valor * 0.20
Costo_2 = Valor - Segundo_Descuento
print("Valor a pagar: ")
if (Numero_Azar >= 74):
    print(Costo_2)
else:
    print(Costo_1)

# EJERCICIO 3
Valor_Monto = float(input("Inserte el valor del monto asegurar: "))
Primer_porcentaje = Valor_Monto * 0.03
Costo_Valor1 = Valor_Monto + Primer_porcentaje
Segundo_porcentaje = Valor_Monto * 0.02
Costo_Valor2 = Valor_Monto + Segundo_porcentaje
print("Valor a pagar: ")
if (Valor_Monto < 50000):
    print(Costo_Valor1)
else:
    print(Costo_Valor2)

# EJERCICIO 4
Numero_Puntos = float(input("Inserte el número de puntos de contaminación: "))
Valor_Ganancia = float(input("Inserte el valor de ganancias de esta semana: "))
Total_Conteo = Numero_Puntos / 5
Con_Multa = Valor_Ganancia * 0.5
Total_1 = Valor_Ganancia - Con_Multa
Sin_Multa = Valor_Ganancia * 0
Total_2 = 0
if (Numero_Puntos > 170):
    print("Multa a pagar: ")
    print(Total_1)
else:
    print("Multa a pagar: ")
    print(Total_2)
    