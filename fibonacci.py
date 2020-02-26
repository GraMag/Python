#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Fibonacci
#Crear un programa que tenga una funcion que se llame Fibo que reciba un unico argumento y ese argumento sea la cantidad de elementos que tenga la sucecion. (Trabajar con listas)

lista = [0, 1]

def fibo(n):
	i = 0
	while (i < n-2):
		lista.append(lista[-1]+lista[-2])
		i = i + 1
	
	print (lista)


fibo(10)
