"""
	file: run4.py
	autor: @David

"""
# Pidiendo los datos 

modalidad = input ("Ingrese su modalidad \n")
edad = input ("Ingrese su edad \n")

# Inicializando viables

prec_ciclo = 1200
seguro = 0
ciclo = 0
valor_seguro = 0

edad = int(edad)

# Evaluamos la edad del estudiante

if (edad <= 20):
	seguro = 100
else:
	seguro = 150	

# Evaluamos la modalidad del estudiante

if (modalidad == "distancia"):
	ciclo = 10 
	valor_seguro  = seguro * ciclo
	valor_carrera = valor_seguro + (prec_ciclo * ciclo)
else: 	
	ciclo = 8 
	valor_seguro  = seguro * ciclo
	valor_carrera = valor_seguro + (prec_ciclo * ciclo)

#Presentamos el precio final de la carrera	

print (" El precio de su carrera es de %d" % valor_carrera)
