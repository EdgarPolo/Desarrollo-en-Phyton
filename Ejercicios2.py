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

# Ejercicio # 2
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

# Ejercicio # 3
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

# Ejercicio # 4
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

# EJERCICIO 5
Costo_comercial = float(input("Digite el valor del automóvil o terreno: "))
Porcentaje1 = float(input("Digite el % devaluado del automovil en 3 años: "))
Porcentaje2 = float(input("Digite el % Avaluado del terreno en 3 años: "))
Costo_Devaluo = Porcentaje1 / 100
Valor_Devaluo1 = Costo_comercial * Costo_Devaluo
Valor_Avaluo = Porcentaje2 / 100
Valor_Avaluo1 = Costo_comercial * Valor_Avaluo
Valor_Total_Avaluo = Valor_Avaluo1 / 2
if (Valor_Devaluo1 > Valor_Total_Avaluo):
    print("Debe comprar el auotomóvil")
else:
    print("Debe comprar el terreno")

# Ejercicio # 6
Cantidad = float(input("Digite la cantidad total de computadoras compradas: "))
Valor = Cantidad * 11000
Descuento1 = Valor * 0.10
Valor_Dcto1 = Valor - Descuento1
Descuento2 = Valor * 0.20
Valor_Dcto2 = Valor - Descuento2
Descuento3 = Valor * 0.40
Valor_Dcto3 = Valor - Descuento3
if (Cantidad < 5):
    print("Valor a pagar con descuento del 10% es: ")
    print(Valor_Dcto1)
elif (Cantidad > 10):
    print("Valor a pagar con descuento del 20% es: ")
    print(Valor_Dcto2)
else:
    print("Valor a pagar con descuento del 40% es: ")
    print(Valor_Dcto3)

# Ejercicio # 7

precio_Prod = int(input('Ingrese el precio del producto : '))
marca = input('Ingrese la marca del producto: ')
if precio_Prod >= 2000 and marca == 'nosy':
    total_dcto = precio_Prod - (precio_Prod * 0.10) - (precio_Prod * 0.05)
    total_con_iva = total_dcto + (precio_Prod * 0.16)
    print(f' Total: {total_con_iva}')
elif precio_Prod >= 2000:
    total_dcto = precio_Prod - (precio_Prod * 0.10)
    total_con_iva = total_dcto + (precio_Prod * 0.16)
    print(f' Total: {total_con_iva}')
elif marca == 'nosy':
    total_dcto = precio_Prod - (precio_Prod * 0.005)
    total_con_iva = total_dcto + (precio_Prod * 0.16)
    print(f' Total: {total_con_iva}')

# Ejercicio # 8
monto = int(input('Ingrese el monto : '))
if monto > 500000:
    dineroPropio = (monto*0.55)
    prestamoBanco = (monto * 0.30)
    prestamofabricante = (monto * 0.15)
    intereses = prestamofabricante * 0.20
    print(f' Cantidad a invertir: {dineroPropio}')
    print(f' Valor del prestamo : {prestamoBanco}')
    print(f' Valor del crédito : {prestamofabricante}')
    print(f' Intereses : {intereses}')
elif monto <= 500000:
    dineroPropio = (monto*0.70)
    prestamofabricante = (monto * 0.30)
    intereses = (prestamofabricante * 0.20)
    print(f' Cantidad a invertir: {dineroPropio}')
    print(f' Valor del crédito : {prestamofabricante}')
    print(f' Intereses : {intereses}')

# Ejercicio # 9
Recoletar_n1 = float(input('Digite el primer número : '))
Recoletar_n2 = float(input('Digite el segundo número : '))
if Recoletar_n1 == Recoletar_n2:
    Resultado1 = Recoletar_n1 * Recoletar_n2
    print(f' Total: {Resultado1}')
elif Recoletar_n1 > Recoletar_n2:
    Resultado2 = Recoletar_n1 - Recoletar_n2
    print(f' Total: {Resultado2}')
elif Recoletar_n1 < Recoletar_n2:
    Resultado3 = Recoletar_n1 + Recoletar_n2
    print(f' Total: {Resultado3}')

# Ejercicio # 10
num1 = int(input('Ingrese un número : '))
num2 = int(input('Ingrese un número : '))
num3 = int(input('Ingrese un número : '))
if num1 > num2 and num1 > num3:
    print(f'El mayor numero es el : {num1}')
elif num2 > num1 and num2 > num3:
    print(f'El mayor numero es el : {num2}')
elif num3 > num1 and num3 > num2:
    print(f'El mayor numero es el : {num3}')
