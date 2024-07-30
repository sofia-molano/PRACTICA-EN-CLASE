#Manuel Alejandro Velasco Marinez
#Ejercicio 1

def promedio():
    arreglo = [1,2,3,4,5]
    promedio = sum(arreglo)/len(arreglo)
    print("El promedio es:",promedio)
promedio()

#Ejercicio 2
def producto ():
    v = [1,4,7]
    w = [1,7,9]
    producto = 0
    if len(v) == len(w):
        for v, w in zip(v, w): #Zip es un iterador de tuplas
         producto += v * w
    print("El producto es:", producto)
producto()

#Ejercicio 3
def directo():
    v = [1,4,7]
    w = [1,7,9]
    if len(v) == len(w):
        directo = [v * w for v, w in zip(v, w)]
    print("El producto directo es:", directo)
directo()
