#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

ventana = tk.Tk()
empanadas = []
	

def order():
	cajaResult.delete("1.0",tk.END)
	price = (cajaPrice.get())
	if (price != ""):
		try:
			price = float(price)
		except:
			messagebox.showerror(title="¡Error!", message="Precio invalido")
			price.delete(0,tk.END)
		cajaPrice.configure(state="disable")
	
	name = cajaName.get()
	if name != "":		
		try:
			auxj = int(cajaJyQ.get())
			auxc = int(cajaCarne.get())
			auxh = int(cajaHum.get())
			auxa = int(cajaAtun.get())
		except:
			messagebox.showerror(title="¡Error!", message="Cantidad invalida")
		empanadas.append([name, auxj, auxc, auxh, auxa])
		
	jyq = 0
	carne = 0
	humita = 0
	atun = 0
	
	for i in empanadas:
		jyq = jyq + i[1]
		carne = carne + i[2]
		humita = humita + i[3]
		atun = atun + i[4]
	
	total = "{0:.2f}".format(totalEmpanadas() * price)
	
	
	gustos = "Jamon y queso: " + str(jyq) + "\nCarne: " +  str(carne) + "\nHumita: " + str(humita) + "\nAtún: " + str(atun)
	
	cajaResult.insert(tk.END, gustos + "\n")
	cajaResult.insert(tk.END, "El total a pagar es:  " + str(total) + "\n")
	
	return price
	
def options():
	option = menu.get()
	if option == "Ingresar otro usuario":
		order()
		delete()
	if option == "Pago proporcional":
		price = order()
		delete()
		total = totalEmpanadas()
		cajaResult.insert(tk.END, ("\nCada uno debe pagar: $" + str("{0:.2f}".format(total*price/len(empanadas)))))
	if option == "Pago individual":
		price = order()
		delete()
		for i in empanadas:
			suma = i[1] + i[2] + i[3] + i[4]
			individual = ("\n" + str(i[0]) + " pidio: " + str(suma) + " empanadas. \nLe corresponde pagar: $" + str(price*suma) + "." )
			cajaResult.insert(tk.END, individual)
			suma = 0
	if option == "Mostrar lista":
		order()
		delete()
		for i in empanadas:
			name = i[0]
			jyq = i[1]
			carne = i[2]
			humita = i[3]
			atun = i[4]
			pedido = "\nNombre: " + name + ". \nJamon y queso: " + str(jyq) + "\nCarne: " + str(carne) + "\nHumita: " + str(humita) + "\nAtun: " + str(atun) + "\n\n"
			cajaResult.insert(tk.END,pedido)

def totalEmpanadas():
	jyq = 0
	carne = 0
	humita = 0
	atun = 0
	
	for i in empanadas:
		jyq = jyq + i[1]
		carne = carne + i[2]
		humita = humita + i[3]
		atun = atun + i[4]
	
	total = jyq + carne + humita + atun
	return total
			
def delete():
	cajaName.delete(0,tk.END)
	cajaJyQ.delete(0,tk.END)
	cajaCarne.delete(0,tk.END)
	cajaHum.delete(0,tk.END)
	cajaAtun.delete(0,tk.END)

ventana.config(width = 310, heigh = 600)
ventana.title("Empanadas")

### Precio ###
cajaPrice = tk.Entry()
cajaPrice.place(x = 180, y = 50, height = 20, width = 90)

etiquetaPrice = tk.Label(text = "Ingresa precio por unidad: $")
etiquetaPrice.place (x =20, y = 50)

### Nombre ###
cajaName = tk.Entry()
cajaName.place(x = 180, y = 100, height = 20, width = 90)

etiquetaName = tk.Label(text = "Ingresa tu nombre: ")
etiquetaName.place (x =20, y = 100)

### Gustos ###
cajaJyQ = tk.Entry()
cajaJyQ.place(x = 180, y = 125, height = 20, width = 90)

etiquetaJyQ = tk.Label(text = "Candidad de jamón y queso: ")
etiquetaJyQ.place (x =20, y = 125)

cajaCarne = tk.Entry()
cajaCarne.place(x = 180, y = 150, height = 20, width = 90)

etiquetaCarne = tk.Label(text = "Cantidad de carne: ")
etiquetaCarne.place (x =20, y = 150)

cajaHum = tk.Entry()
cajaHum.place(x = 180, y = 175, height = 20, width = 90)

etiquetaHum = tk.Label(text = "Cantidad de humita: ")
etiquetaHum.place (x =20, y = 175)

cajaAtun = tk.Entry()
cajaAtun.place(x = 180, y = 200, height = 20, width = 90)

etiquetaAtun = tk.Label(text = "Cantidad de atún: ")
etiquetaAtun.place (x =20, y = 200)


###Menu###


botonMenu = tk.Button(text = "Aceptar", command = options)
botonMenu.place ( x = 235, y = 280, width = 55, height = 25)

etiquetaMenu = tk.Label(text = "Seleciona una opción: ")
etiquetaMenu.place (x =20, y = 250)


menu = ttk.Combobox(values = ["Ingresar otro usuario", "Pago proporcional", "Pago individual", "Mostrar lista"])
menu.set("Ingresar otro usuario")
menu.place( x = 150, y = 250, width = 140, height = 20)


### Resultado ###

etiquetaResult = tk.Label(text = "Total: ")
etiquetaResult.place (x =20, y = 300)


cajaResult = tk.Text(ventana)
S = tk.Scrollbar(cajaResult)
S.pack(side=tk.RIGHT, fill=tk.Y)
cajaResult.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=cajaResult.yview)
cajaResult.config(yscrollcommand=S.set)
cajaResult.pack()
cajaResult.place(x = 30, y = 320, height = 250, width = 250)

### Visual ###

ventana.configure(background = "#228B22")
etiquetaMenu.configure(background = "#228B22", foreground = "#FFFFFF")
etiquetaPrice.configure(background = "#228B22", foreground = "#FFFFFF")
etiquetaName.configure(background = "#228B22", foreground = "#FFFFFF")
etiquetaJyQ.configure(background = "#228B22", foreground = "#FFFFFF")
etiquetaCarne.configure(background = "#228B22", foreground = "#FFFFFF")
etiquetaHum.configure(background = "#228B22", foreground = "#FFFFFF")
etiquetaAtun.configure(background = "#228B22", foreground = "#FFFFFF")
etiquetaResult.configure(background = "#228B22", foreground = "#FFFFFF")
botonMenu.configure(background = "#FF8C00", foreground = "#FFFFFF")
cajaPrice.configure(background = "#217C34", foreground = "#FFFFFF")
cajaName.configure(background = "#217C34", foreground = "#FFFFFF")
cajaJyQ.configure(background = "#217C34", foreground = "#FFFFFF")
cajaCarne.configure(background = "#217C34", foreground = "#FFFFFF")
cajaHum.configure(background = "#217C34", foreground = "#FFFFFF")
cajaAtun.configure(background = "#217C34", foreground = "#FFFFFF")




ventana.mainloop()
