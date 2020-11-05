name = 'Daniel'
"Hola %s" % name
"El número es %d" %5
"El número es %02d" %5
"El decimal es %f" %6.5
"Hola %(name)s" % {'name':name}

"Hola {}" .format(name)
"La suma de 1 + 2 es {0}" .format(1+2)

' '.join({"Hola", name})
' '.join(["1", "2", "3", "4"])