# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 15:36:58 2021

@author: Edgar_Polo
"""
print('Ejercicios Taller 1')
# Punto numero 1 Empresa
Inversion_1 = float(input("Digite el valor a invertir: "))
Inversion_2 = float(input("Digite el valor a invertir: "))
Inversion_3 = float(input("Digite el valor a invertir: "))
Total = Inversion_1 + Inversion_2 + Inversion_3
print("Valor total de la Inversion es:")
print(Total)
total1 = Inversion_1 / Total
resultado1 = total1 * 100
print("Porcentaje del Inversionista 1")
print(resultado1)
total2 = Inversion_2 / Total
resultado2 = total2 * 100
print("Porcentaje del Inversionista 2")
print(resultado2)
total3 = Inversion_3 / Total
resultado3 = total3 * 100
print("Porcentaje del Inversionista 3")
print(resultado3)
# Punto numero 2
Sueldo_Basico = float(input("Digite el valor del sueldo Basico"))
No_Hijos = float(input("Digite el numero de hijos"))
Bonificacion_Hijo = No_Hijos * 80000
TotalSueldo = Bonificacion_Hijo + Sueldo_Basico
print("La Bonificacion que debe recibir es de: ")
print(Bonificacion_Hijo)
print("El sueldo total a recibir es de: ")
print(TotalSueldo)
# Punto numero 3
Saldo_Inicial = float(input("Digite el valor del saldo inicial"))
Resultado_Interes = Saldo_Inicial * 0.15
print("El valor del interes es de: ")
print(Resultado_Interes)
total = Resultado_Interes + Saldo_Inicial
print("El saldo final es de: ")
print(total)
# Punto numero 4
Metros_Cuadrados = float(input("Digite el total de metros cuadrados"))
Total_Valor = Metros_Cuadrados * 80000
print("El valor total de los metros cuadrados es de: ")
print(Total_Valor)
Cuota_inicial = Total_Valor * 0.35
print("El valor a pagar en la cuota inical es de: ")
print(Cuota_inicial)
Saldo_Restante = Total_Valor - Cuota_inicial
print("EL saldo restante a financiar es de: ")
print(Saldo_Restante)
print("El valor a pagar por cuotas mensuales es de: ")
Total_Cuotas = Saldo_Restante / 12
print(Total_Cuotas)
# Punto numero 5
Sueldo_Base = float(input("Digite el Sueldo Basico"))
Dcto_Ley = Sueldo_Base * 0.01
Dcto_Seguro_Social = Sueldo_Base * 0.04
Dcto_Seguro_Forzoso = Sueldo_Base * 0.005
Dcto_Caja = Sueldo_Base * 0.05
Descuento1 = Sueldo_Base - Dcto_Ley
Descuento2 = Descuento1 - Dcto_Seguro_Social
Descuento3 = Descuento2 - Dcto_Seguro_Forzoso
Descuento4 = Descuento3 - Dcto_Caja
print("El descuento a aplicar en Ley de Politica es de: ")
print(Dcto_Ley)
print("El descuento a aplicar en Seguro Social es de: ")
print(Dcto_Seguro_Social)
print("El descuento a aplicar en Seguro Forzoso es de: ")
print(Dcto_Seguro_Forzoso)
print("El descuento a aplicar en Caja de Ahorro es de: ")
print(Dcto_Caja)
print("El valor total recibido será de: ")
print(Descuento4)
# Punto numero 6
Numero_Palabras = float(input("Digite el numero de palabras"))
Numero_Centimetros = float(input("Digite el numero de centimetros"))
Numero_Colores = float(input("Digite el numero de colores"))
Costo_Palabras = Numero_Palabras * 20000
print("El valor a pagar por palabras es de")
print(Costo_Palabras)
Costo_Centimetros = Numero_Centimetros * 15000
print("El valor a pagar por Centimetros es de")
print(Costo_Centimetros)
Costo_Colores = Numero_Colores * 25000
print("El valor a pagar por Colores es de")
print(Costo_Colores)
Total_Periodico = Costo_Palabras + Costo_Centimetros + Costo_Colores
print("El valor total a pagar por el periodico es de: ")
print(Total_Periodico)

# Punto numero 7
Años_Trabajados = float(input("Digite el numero de Años trabajados"))
Valor_Trabajados = (Años_Trabajados * 120000) - 20000
Valor_Trabajado = 100000
if (Años_Trabajados >= 2):
    print(Valor_Trabajados)
else:
    print(Valor_Trabajado)

# Punto numero 8
Numero_Horas = float(input("Digite el Numero de Horas"))
Valor_Pagar = Numero_Horas * 20000
Dcto_Caja = Valor_Pagar * 0.05
Restante = Valor_Pagar - Dcto_Caja
print("EL valor del descuento es de: ")
print(Dcto_Caja)
print("El valor a cancelar es de: ")
print(Restante)

# Punto numero 9
Monto_Inicial = float(input("Digite el Monto inicial"))
Monto_Final = float(input("Digite el Monto Final"))
Monto_Consumido = Monto_Final - Monto_Inicial
total_costo = Monto_Consumido * 0.2
print("El valor del recargo es de: ")
print(total_costo)
Resultado = total_costo + Monto_Consumido
print("El valor total consumido es de: ")
print(Resultado)

# Punto numero 10
Numero_Fotos = float(input("Digite el numero de fotos"))
Valor_Fotos = Numero_Fotos * 1500
Porcentaje = Valor_Fotos * 0.16
print("EL valor del iva es de: ")
print(Porcentaje)
total_pagar = Valor_Fotos + Porcentaje
print("El valor total a pagar es de: ")
print(total_pagar)

# Punto numero 11
Monto_Presupuestal = float(input("Digite el monto presupuestal"))
Monto_Ginecologia = Monto_Presupuestal * 0.4
print("El monto para Ginecologia será de: ")
print(Monto_Ginecologia)
Monto_Traumatologia = Monto_Presupuestal * 0.3
print("El monto para Traumatologia será de: ")
print(Monto_Traumatologia)
Monto_Pediatria = Monto_Presupuestal * 0.3
print("El monto para Pediatria será de: ")
print(Monto_Pediatria)

# Punto numero 12
No_Peliculas = float(input("Digite el total de peliculas"))
No_Dias = float(input("Digite el total de Dias"))
Transcurso_Dp = No_Peliculas * No_Dias
Valor_Peliculas = Transcurso_Dp * 1500
Valor_Total = Valor_Peliculas - 1500
print("El valor a pagar es de: ")
print(Valor_Total)

# Punto numero 13
No_Personas = float(input("Digite el numero de personas"))
No_Dias = float(input("Digite el numero de Dias"))
Viaje = No_Personas * No_Dias
Valor_viaje = Viaje * 25000
Porcentaje = Valor_viaje * 0.12
print("El valor del iva es de: ")
print(Porcentaje)
Valor_total = Porcentaje + Valor_viaje
print("El valor total a pagar es de: ")
print(Valor_total)

# Punto numero 14
Dias_habitacion = float(input("Digite el numero de días de habitación"))
Valor_dias = (Dias_habitacion * 200000) - 100000
Valor_dia = 100000
if (Dias_habitacion >= 2):
    print(Valor_dias)
else:
    print(Valor_dia)

# Punto numero 15
Valor_Prestamo = float(input("Digite el monto del prestamo"))
interes = Valor_Prestamo * 0.24
Valor_total_pagar = Valor_Prestamo + interes
print("El valor total a pagar es de: ")
print(Valor_total_pagar)
Cuota_media = Valor_total_pagar / 2
Cuota_Especial = Cuota_media / 4
print("las cuotas especiales son de un valor de: ")
print(Cuota_Especial)
Cuota_Mensual = Cuota_media / 20
print("Las cuotas a pagar mensuales seran de un valor de: ")
print(Cuota_Mensual)

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