#!/usr/bin/env python
# -*- coding: utf-8 -*-

notas = []

def menu():
	print("""Bienvenido. Seleccione una de las siguientes opciones:
	1- Ver la lista de alumnos.
	2- Añadir un alumno a la lista
	3- Mostrar Aprobados y Desaprobados
	4- Salir
	""")
	
def tryInt(string):
	while True: 
		lalala = input(string)
		try:
			lalala = int(lalala)
			return lalala
			break
		except:
			print("Error, opción invalida")
		
def prog():
	if (opcion == 1):
		print(notas)
		
	elif (opcion == 2):
		nombre = input("Ingresar nombre: ")
		notaUno = tryInt("Ingresar nota 1: ")
		notaDos = tryInt("Ingresar nota 2: ")
		notas.append([nombre, notaUno, notaDos])
	
	elif (opcion == 3):
		aprobados = []
		desaprobados = []
		for i in notas:
			prom = ((i[1] + i[2]) / 2)
			if prom >= 4:
				aprobados.append([i])
			else:
				desaprobados.append([i])
		print ("Aprobados")
		print (aprobados)
		print ("Desaprobados")
		print (desaprobados)
					
	elif opcion == 4:
		print ("Hasta luego.")
		break	

while True:
	menu()
	opcion = tryInt("")
	prog()
		
