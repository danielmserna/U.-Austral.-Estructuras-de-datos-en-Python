#Las listas son mutables, mientras que las cadenas de texto, no.

nombre = 'Daniel'

lista = list(nombre)

nombre[0]
lista[0]

nombre[:4]
lista[:4]

len(nombre)
len(lista)

'D' in nombre
'D' in lista

'z' not in nombre
'z' not in lista

#Los Strings se pueden recorrer con un for
for letra in nombre:
    print(letra)

#Los Strings son inmutables
lista[2] = 'o'
nombre[2] = 'o' #TypeError

'Hola ' + nombre
nombre + ' !'
nombre[:2] + 'o' + nombre[3:]