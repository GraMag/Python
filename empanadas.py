#!/usr/bin/env python
# -*- coding: utf-8 -*-

empanadas = []

# Ingresa el precio
def unitPrice():
	price = float(input ("Precio por unidad: $"))
	print("")
	return price
	
# Ingresa el nombre del usuario
def user():
	name = input("Tu nombre: ")
	print("")
	print("Hola", name)
	return name
	
# Pide al usuario que ingrese un gusto
def message(s):
	taste = int(input("Cuántas empanadas de " + s + " querés? "))
	return taste
	
# Añadir usuarios
def continuar():
	print("")
	cont = input("Desea ingresar otro usuario? S/N: ")
	print("")
	return cont

# Añade a la lista cada perfil
def order():
	while True:
		name = user()
		# Input de gustos
		auxj = message("jamon y queso")
		auxc = message("carne") 
		auxh = message("humita") 
		auxa = message("atún") 
		
		# Añade el nombre de usuario y la cantidad de gustos seleccionados al final del array
		empanadas.append([name, auxj, auxc, auxh, auxa])
		
		# Variable controladora para salir del While
		if (continuar() == "N"):
			break

#Muestra el detalle del pedido.
def total(price):
	jyq = 0
	carne = 0
	humita = 0
	atun = 0
	
	for i in empanadas:
		jyq = jyq + i[1]
		carne = carne + i[2]
		humita = humita + i[3]
		atun = atun + i[4]
	totalEmpanadas = int(jyq + carne + humita + atun )
	amount = price * totalEmpanadas
	
	print("")
	print("El total de empanadas es:" , totalEmpanadas , ". De las cuales: ")
	print("Jamon y queso: " , jyq)
	print("Carne: " , carne)
	print("Humita: " , humita)
	print("Atún: " , atun)
	print("El total a pagar es: $" , (amount))
	print("")
	return amount

# Divide los gastos de modo proporcional o individual, muestra la lista, termina el programa.	
def menu(amount, empanadas):
	titulos = [["Nombre","J","C","H","A"]]
	while True:	
	
		print("""Ingrese una opción:
		1- Dividir la cuenta en partes iguales
		2- Cada uno paga lo suyo
		3- Mostrar lista
		4- SALIR
		""")

		option = int(input("... "))
		if option == 1:
			print("Cada uno debe pagar: $" , (amount/len(empanadas)) )
		if option == 2:
			for i in empanadas:
				suma = i[1] + i[2] + i[3] + i[4]
				print(i[0], "pidio: ", suma, "empanadas. Le corresponde pagar: $", (price*suma) )
				suma = 0
		if option == 3:
			for i in titulos:
				print(i)
			for taste in empanadas:
				print(taste)
		if option == 4:
			print("Buen provecho.")
			break


############
##PROGRAMA##
############


price = unitPrice()
order()
menu(total(price), empanadas)
