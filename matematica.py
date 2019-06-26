import random

def fatorial(n):
	f = 1
	for C in range(1, n+1):
		f *= C
	return f
	
def multiplicar(n):
	mt = n/2
	p = mt*2
	
	resultado = p*3
	return resultado
	
def triplo(n):
	return n*3

def quaduplo(n):
	return n * 4
	
def quinplo(n):
	return n * 5

def taxa(n):
	tx = n/5
	txh = tx*2
	return txh
	
def potencia(b, e):
	a = b*e
	c = a*e
	return c*e
