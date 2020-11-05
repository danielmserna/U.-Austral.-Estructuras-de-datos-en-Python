a_list = [3, 7.5, 'Hola', 7j + 5, [1, 2]]

a_list[0]
a_list[2]
a_list[-1]

#Slicing
a_list[1:]
a_list[1:2]
a_list[1:3]
a_list[:2]
a_list[:]

#Devuelve la cantidad de elementos de una lista
len(a_list)

#Agrega un elemento al final de la lista
a_list.append(2)

#Extiende los elementos con los elementos de otra lista
a_list.extend([3, 4])

#Inserta un elemento en una posición determinada.
a_list.insert(4 ,'Intercalado')
a_list.insert(12, 'Fuera de rango')
a_list.insert(-1, 'Hacia atrás')

#Cuenta cuantos elementos hay que coincidan con el argumento
a_list.count(3)

#Elimina el primer elemento que encuentra pasado como parámetro.
a_list.remove(3)

#Hace una copia superficial de la lista
a_list_copy = a_list.copy()

#Saca el último elemento y lo devuelve.
a_list.pop()

#Saca el último elemento y lo devuelve.
a_list.pop(3)

#Saca el último elemento y lo devuelve.
a_list.clear()