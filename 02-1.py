from random import random

total_num = int( raw_input (" Dame un numero : "))
lista = []

for i in range ( total_num ):
    lista . append ( random ())
print 'La lista de %d numeros aleatorios es: (' % total_num ,
for i in range ( total_num ):
    print ' %.3f' % round ( lista [i],3),
    if i != ( total_num - 1): print ",",
print ')'
print 'La suma de estos %d elementos es: %.2f' % (total_num , round (sum( lista ) ,2))
