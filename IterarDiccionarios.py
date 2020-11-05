
precios = {'manzana':3.5, 'banana':4.5, 'kiwi':6.0, 'pera':3.75}

precios['melon'] = 5.5

#Iteración de los diccionarios
for fruta,precio in precios.items():
    print("Precio de ", fruta, ": $", precio)
