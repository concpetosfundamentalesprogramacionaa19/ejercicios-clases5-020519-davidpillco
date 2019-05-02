"""
	file: run3.py
	autor: @David

"""

from misvariables import *

# Uso de condicional simple

# Pidiendo la nota

nota = input ("Ingrese la nota : \n")

# Transformamos la nota a entero
nota = int(nota)

# Evaluacion de la nota

if (nota >= 18):
	print ("%s - nota %d" % ("Sobresaliente", nota))
else:	
	if (nota >= 16) & (nota <= 18):
		print ("%s - nota %d" % ("Muy buena", nota))
	else:	
		if (nota >= 13) & (nota <= 16):
			print ("%s - nota %d" % ("Buena", nota))
		else:	
			print ("%s - nota %d" % ("Insuficiente", nota))


