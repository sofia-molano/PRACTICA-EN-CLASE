#arreglos y modulos
#Sergio Melendez
#29/07/2024

#Ejercicio 1 Promedio

enteros = [2, 5, 7, 23, 2, 9]

def calcular_promedio (enteros):
    
    sumar = sum(enteros)
    promedio = sumar / len(enteros)
    return promedio

promedio = calcular_promedio (enteros)
print ("el promedio de la tupla es: ", promedio)


#ejercicio 2
#Producto punto de dos arreglos

arreglo1001 = [1, 2, 3, 4, 5]
arreglo1002 = [6, 7, 8, 9, 10]

def producto_punto (arreglo1001, arreglo1002):

    producto = 0

    if len(arreglo1001) == len(arreglo1002):

        for i in range(len(arreglo1001)):
            producto += arreglo1001[i] * arreglo1002[i]
            return producto

resultado = producto_punto (arreglo1001, arreglo1002)
print("El producto punto es: ", resultado)



#ejercicio 3
#Producto directo de dos arreglos

directo1 = [4, 6, 2, 8, 10, 202]
directo2 = [6, 4, 23, 44, 1, 202]

def producto_directo (directo1, directo2):

    directo = [0] * len[directo1]
    print (directo)

    if len(directo1) == len(directo2):

        for i in range(len(directo1)):
            directo [i] = directo1[i] * directo2[i]
            return directo

directo = producto_directo (directo1, directo2)
print ("El producto punto de los arreglos es: ", directo)
