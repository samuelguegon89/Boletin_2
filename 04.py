dir_ipv4 =map(int,raw_input("Dame una direccion IPv4 publica: ").split('.'))
print 'La parte de red 6to4 correspondiente es: 2002: %x%x:%x%x' % (dir_ipv4[0],dir_ipv4[1],dir_ipv4[2],dir_ipv4[3])