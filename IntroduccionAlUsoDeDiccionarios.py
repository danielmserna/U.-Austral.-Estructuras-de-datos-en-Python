#Formas de definir un diccionario

precios = {'manzana':3.5, 'banana':4.5, 'kiwi':6.0, 'pera':3.75}

precios_2 = dict(manzana=3.5, banana=4.5, kiwi=6.0, pera=3.75)

precios_3 = dict([('manzana',3.5), ('banana',4.5), ('kiwi',6.0), ('pera',3.75)])

#Acceso a los elementos por claves
precios['manzana']
precios['banana']
precios['kiwi']
precios['pera']
precios['melon']

#Agregar un elemento (clave-valor)
precios['melon'] = 5.75

#Actualizar un elemento (clave-valor)
precios['manzana'] = 3.0

#Borrar un elemento (clave-valor)
del precios ['manzana']

#Pertenencia
'banana' in precios
'sandia' not in precios