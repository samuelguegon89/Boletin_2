from calendar import weekday 

fecha=raw_input("Introduce tu fecha de nacimiento en el siguiente formato DD-MM-YYYY: ").split("-")

diasemana=["Lunes","Martes","Miercoles","Jueves","Viernes","sabado","domingo"]


print "Naciste en", diasemana[weekday(int(fecha[2]),int(fecha[1]),int(fecha[0]))]
