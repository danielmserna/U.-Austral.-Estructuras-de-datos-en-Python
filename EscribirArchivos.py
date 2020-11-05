with open('c:/Users/Natalia/Desktop/CourseraPython/2/archivoparaescribir.txt','w') as a_file:
    a_file.write('Hola mundo!')

with open('c:/Users/Natalia/Desktop/CourseraPython/2/archivoparaescribir.txt','w') as a_file:
    a_file.writelines(['Linea 1.\n','Linea 2.\n','Linea 3.\n'])

with open('c:/Users/Natalia/Desktop/CourseraPython/2/archivoparaescribir.txt','a') as a_file:
    a_file.write("Hola mundo!")
