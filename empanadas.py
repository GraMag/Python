#!/usr/bin/env python
# -*- coding: utf-8 -*-


empanadas = []
titulos = [["User","J","C","H","A"]]
jyq = 0
carne = 0
humita = 0
atun = 0
auxj = 0
auxc = 0
auxh = 0
auxa = 0
totalEmpanadas = 0


price = float(input ("Precio por unidad: $"))
print("")

while True:
	name = input("Tu nombre: ")
	print("")
	print("Hola", name)
	# Input de gustos
	auxj= int(input("Cuántas empanadas de jamon y queso querés? "))
	jyq = jyq + auxj
	auxc = int(input("Cuántas empanadas de carne querés? "))
	carne = carne + auxc
	auxh = int(input("Cuántas empanadas de humita querés? "))
	humita = humita + auxh
	auxa = int(input("Cuántas empanadas de atún querés? "))
	atun = atun + auxa
	
	# Añade el nombre de usuario y la cantidad de gustos seleccionados al final del array
	empanadas.append([name, auxj, auxc, auxh, auxa])
	
	# Variable controladora para salir del While
	print("")
	cont = input("Desea ingresar otro usuario? S/N: ")
	print("")
	
	if (cont == "N"):
		break	


totalEmpanadas = jyq + carne + humita + atun
importe = price*totalEmpanadas

# Imprime el detalle del pedido.
print("")
print("El total de empanadas es:" , totalEmpanadas , ". De las cuales: ")
print("Jamon y queso: " , jyq)
print("Carne: " , carne)
print("Humita: " , humita)
print("Atún: " , atun)
print("El total a pagar es: $" , (importe))
print("")

# Divide los gastos de modo proporcional o individual, muestra la lista, termina el programa.
while True:	
	
	print("""Ingrese una opción:
	1- Dividir la cuenta en partes iguales
	2- Cada uno paga lo suyo
	3- Mostrar lista
	4- SALIR
	""")

	opcion = int(input("... "))
	if opcion == 1:
		print("Cada uno debe pagar: $" , (importe/len(empanadas)) )
	if opcion == 2:
		for i in empanadas:
			suma = i[1] + i[2] + i[3] + i[4]
			print(i[0], "pidio: ", suma, "empanadas. Le corresponde pagar: $", (price*suma) )
			suma = 0
	if opcion == 3:
		for i in titulos:
			print(i)
		for gustos in empanadas:
			print(gustos)
	if opcion == 4:
		print("Buen provecho.")
		break

