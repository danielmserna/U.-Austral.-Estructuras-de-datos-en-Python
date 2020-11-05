#Lista de cuadros
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)

#Lista por comprensión
cuadrados_2 = [ x**2 for x in range(10)]

#Cuadrados utilizando la función map
cuadrados_3 = list(map(lambda x: x**2, range(10)))
a_list = [-4, -2, 0, 2, 4]

# Lista por comprensión con los números positivos de a_list
positivos = [x for x in a_list if x >= 0]

#Lista con los números positivos de a_list utilizando la función filter
positivos_2 = list(filter(lambda x: x>0 , a_list))

#Pares número y su cuadrado
[(x, x**2) for x in range(6)]

#Lista de pares combinados
pares = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

#Equivale a
pares_2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            pares_2.append((x,y))