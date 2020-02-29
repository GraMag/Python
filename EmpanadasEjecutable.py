#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk



empanadas = []

# Ingresa el precio
def unitPrice():
	while True:
		price = input ("Precio por unidad: $")
		try:
			price = float(price)
			return price
			break
		except:
			print("Error. No es un valor valido. Intentelo nuevamente.")
	
# Ingresa el nombre del usuario
def user():
	name = input("Tu nombre: ")
	print("")
	print("Hola", name)
	return name
	
# Pide al usuario que ingrese un gusto
def message(s):
	while True:
		taste = input("Cuántas empanadas de " + s + " querés? ")
		try:
			taste = int(taste)
			return taste
			break
		except:
			print("Error. No es un numero. Intentalo nuevamente.")
		1


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
		print("")
		while True:
			cont = input("Desea ingresar otro usuario? S/N: ")
			print("")
			if (cont == "N"):
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




ventana = tk.Tk()

ventana.config(width = 400, heigh = 300)
ventana.title("Empanadas")

### Precio ###
cajaPrice = tk.Entry()
cajaPrice.place(x = 180, y = 50, height = 20, width = 90)

botonPrice = tk.Button(text = "Aceptar", command = unitPrice)
botonPrice.place ( x = 280, y = 50, width = 50, height = 20)

etiquetaPrice = tk.Label(text = "Ingresa precio por unidad: $")
etiquetaPrice.place (x =20, y = 50)

### Nombre ###
cajaName = tk.Entry()
cajaName.place(x = 180, y = 100, height = 20, width = 90)

botonName = tk.Button(text = "Aceptar" )
botonName.place ( x = 280, y = 100, width = 50, height = 20)

etiquetaName = tk.Label(text = "Ingresa tu nombre: ")
etiquetaName.place (x =20, y = 100)

### Gustos ###
cajaJyQ = tk.Entry()
cajaJyQ.place(x = 180, y = 125, height = 20, width = 90)

botonJyQ = tk.Button(text = "Aceptar")
botonJyQ.place ( x = 280, y = 125, width = 50, height = 20)

etiquetaJyQ = tk.Label(text = "Canditad de jamón y queso: ")
etiquetaJyQ.place (x =20, y = 125)

cajaCarne = tk.Entry()
cajaCarne.place(x = 180, y = 150, height = 20, width = 90)

botonCarne = tk.Button(text = "Aceptar" )
botonCarne.place ( x = 280, y = 150, width = 50, height = 20)

etiquetaCarne = tk.Label(text = "Cantidad de carne: ")
etiquetaCarne.place (x =20, y = 150)

cajaHum = tk.Entry()
cajaHum.place(x = 180, y = 175, height = 20, width = 90)

botonHum = tk.Button(text = "Aceptar" )
botonHum.place ( x = 280, y = 175, width = 50, height = 20)

etiquetaHum = tk.Label(text = "Cantidad de humita: ")
etiquetaHum.place (x =20, y = 175)

cajaAtun = tk.Entry()
cajaAtun.place(x = 180, y = 200, height = 20, width = 90)

botonAtun = tk.Button(text = "Aceptar" )
botonAtun.place ( x = 280, y = 200, width = 50, height = 20)

etiquetaAtun = tk.Label(text = "cantidad de atún: ")
etiquetaAtun.place (x =20, y = 200)


###Menu###
botonMenu = tk.Button(text = "Aceptar" )
botonMenu.place ( x = 280, y = 250, width = 50, height = 20)

etiquetaMenu = tk.Label(text = "Seleciona una opción: ")
etiquetaMenu.place (x =20, y = 250)

"""
lista_desplegable = ttk.ComboBox(
	values=[
		"Dividir la cuenta en partes iguales",
		"Cada uno paga lo suyo",
		"Mostrar lista",
		"SALIR"
		]
	)
lista_desplegable.place(x=10, y=10)
"""

#################


ventana.mainloop()


############
##PROGRAMA##
############

price = unitPrice()
order()
menu(total(price), empanadas)



