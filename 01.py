cadena1=raw_input("Escribe una cadena larga: ").lower()
cadena2=raw_input("Escribe una palabra: ").lower()

if cadena1.find(cadena2) >= 0:
	print "La segunda cadena SI es una subcadena de la primera"
else:
	print "La segunda cadena NO es una subcadena de la primera"
