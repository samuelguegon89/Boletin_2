Boletin_2
=========

Boletin 2 de ejercicios simples de Python.

1. Realiza un programa que pida un cadena. A continuación debe pedir otra cadena. El
programa debe buscar la segunda cadena en la primera (ignorando mayúsculas o minús-
culas) y podrá responder una de las siguientes opciones:
◦ La segunda cadena es una subcadena de la primera
◦ La segunda cadena no es una subcadena de la primera
Cadena 1: Java es un lenguaje de programacion
Cadena 2: LENGUAJE
Respuesta :
La segunda cadena es una subcadena de la primera

2. El módulo ra
ndom incluye la función random() que genera un número seudo-aleatorio
entre 0 y 1:
>>> from random import random
>>> random ()
0.51605767814317494

Crea un programa que pida al usuario un número n y genere una lista con n elementos
con valores aleatorios y muestre como salida:

◦ La lista de los n números aletaorios con una precisión de 3 decimales.
◦ La suma de todos los elementos con una precisión de 2 decimales.

Nota: Los valores deben redondearse a la precisión solicitada, no truncarse.
Dame un numero : 4
La lista de 4 numeros aleatorios es: (0.123 , 0.432 , 0.335 , 0.456)
La suma de estos 4 elementos es: 1.35

3. Escribe un programa que pida al usuario su fecha de nacimiento y le responda el día de
la semana correspondiente:
Introduce tu fecha de nacimiento (DD -MM -YYYY ): 29 -02 -1992
Naciste en sabado
para ello debes utilizar la función adecuada del módulo calendar.

4. Una dirección 6to4 es una dirección IPv6 reservada para equipos que tienen actual-
mente una dirección IPv4 pública. Un ejemplo de dirección 6to4 sería:
2002:503 b :198:0:219:66 ff:fea8:db3
El campo 2002: es fijo y el bloque importante para esta discusión es el que determina la
parte de red de la dirección, es decir, los campos 503b:198 que son la representación
hexadecimal de la dirección IPv4 correspondiente:
80.59.1.152 = 0x50 .0 x3b .0 x1 .0 x98 = 503b:198

el resto de campos se corresponden con la dirección de subred y la dirección de host, y
no son relevantes para este ejercicio.
Escribe un programa que pida una dirección IPv4 pública y nos dé la parte de red
correspondiente de la dirección 6to4 asociada:
Dame una dirección IPv4 publica : 85.135.34.12
La parte de red 6to4 correspondiente es: 2002:5587:220 c
Nota: Puedes verificar los resultados utilizando la calculadora 6to4 del sitio http://
waldner.netsons.org/f6-6to4.php.
