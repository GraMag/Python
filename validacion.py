#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
	edad = input ("Ingresa tu edad: ")
	try:                        
		edad = int(edad)
		break
	except ValueError:
		print ("Error, ingrese un dato valido!")
		
if edad >= 18:
	print ("Mayor de edad")
else:
	print ("Menor de edad")

