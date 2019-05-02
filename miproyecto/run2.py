"""
	file: run2.py
	autor: @David

"""

from misvariables import *

# Pedimos las notas

nota = input ("Ingrese la nota 1: \n")
nota2 = input ("Ingrese la nota 2: \n ")

# Transformamos las notas a enteros
nota = int(nota)
nota2 = int(nota2)

# Evaluamos las notas
if nota >= 18:
	print ("%s su valor de nota es  %d" % (mensaje, nota))
else:
	print ("%s su valor de nota es %d" % (mensaje2, nota))	

if nota2 >= 18:
	print ("%s su valor de nota es %d" % (mensaje, nota2))
else:
	print ("%s su valor de nota es %d" % (mensaje2, nota2))




