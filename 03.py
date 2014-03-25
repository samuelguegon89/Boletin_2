from calendar import weekday

fecha=str(raw_input("Introduce tu fecha de nacimiento en el siguiente formato DD-MM-YYYY: "))

a1=int(fecha[:2])
a2=int(fecha[3:5])
a3=int(fecha[6:10])
a4=int(fecha[:2]+fecha[3:5]+fecha[6:10])
diasemana=["Lunes","Martes","Miercoles","Jueves","Viernes","sabado","domingo"]

if a1<32 and a1>00:
	if a2<13 and a2>00:
		if a3>0000 and a3<3000:
			print "Tu naciste un",diasemana[weekday(a3,a2,a1)]
		else:
			print "El numero del year no esta entre 0000 y 3000"
			exit()
	else:
		print "El numero del mes no esta entre 1 y 12"
else:
	print "El numero del dia no esta entre 1 y 31"

	

