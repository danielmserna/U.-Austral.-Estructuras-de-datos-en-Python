a_file = open('c:/Users/Natalia/Desktop/CourseraPython/2/archivo.txt','r')

a_file.read()

a_file.close()

with open('c:/Users/Natalia/Desktop/CourseraPython/2/archivo.txt','r') as a_file:
    a_file.read()