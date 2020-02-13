#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ordenar pedido de delivery
Ingresar pedido 1 (cuantas de jyq, cuantas de carne, cuantas de atun, cuantas de humita)
continuar
repeat
Informar costo total y cuantas empanadas de cada una
todas las empanadas valen lo mismo
"""

jyq = 0
carne = 0
atun = 0
humita = 0
empanadas = 0
aux = 0

precio = float(input("Ingrese precio de la empanada: "))

while True:
	aux = int(input("Cuantas empanadas de jamon y queso queres? "))
	jyq = jyq + aux
	aux = int(input("Cuantas empanadas de carne queres? "))
	carne = carne + aux
	aux = int(input("Cuantas empanadas de atùn queres? "))
	atun = atun + aux
	aux = int(input("Cuantas empanadas de humita queres? "))
	humita = humita + aux
	
	
	continuar = input("Desea continuar? S/N ")
	if continuar == "N":
		break

print("")
empanadas = jyq + carne + humita + atun
print ("Son ", empanadas, "empanadas, de las cuales: ")
print(jyq, "son de jamon y queso")
print(carne, "son de carne")
print(atun, "son de atún")
print( humita, "son de humita.")
print("Total: $", (precio*empanadas))
