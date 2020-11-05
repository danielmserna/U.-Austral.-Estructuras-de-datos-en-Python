a_list = [1,2,3,4,5]

#Devuelve el índice
a_list.index(4)

#Lanza una excepción del tipo ValueError
a_list.index(6)

#Opciones indicando una sublista
a_list.index(4, 1)
a_list.index(4, 0, 2)
a_list.index(4, 1, 4)