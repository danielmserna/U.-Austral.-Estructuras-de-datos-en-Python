t = 1/0

try:
    t = 1/0
except ZeroDivisionError:
    print("División por cero")

def find(elemento,lista):
    index = 0
    while True:
        try:
            if lista[index] == elemento:
                return index
        except IndexError:
            return -1
        index +=1

find(4,[2,3,4,5])
find(1,[2,3,4,5])

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("División por cero")
    else:
        print("El resultado es", result)
    finally:
        print("Ejecutando la cláusula finally")

divide(2,1)
divide(2,0)