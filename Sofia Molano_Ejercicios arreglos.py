#EJERCICIO 1
#Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

arreglo=[1,0,2,0,3,5]

def promedio_arreglo(arreglo):
    suma=0
    for i in arreglo:
        suma+=i
        promedio=(suma/len(arreglo))
    return promedio

print (promedio_arreglo(arreglo))

#EJERCICIO 2
#Desarrollar un algoritmo que calcule el producto punto de dos arreglos
#de n ́umeros enteros (reales) de igual tama ̃no. Sean
#v = [v0, v1, . . . , vn−1] y w = [w0,w1, . . . ,wn−1] dos arreglos, el
#producto de v y w (notado v · w) es el n ́umero:
#v0 ∗ w0 + v1 ∗ w1 + · · · + vn−1 ∗ wn−1.

v=[1,7,6]
w=[-3,6,4]

def producto_arreglos(v,w):
    producto = 0
    if len(v)==len(w):
        for x in range(len(v)):
            producto += v[x] * w[x]
    
        return producto
        

print (producto_arreglos(v,w))

#EJERCICIO 3
#Desarrollar un algoritmo que calcule el producto directo de dos
#arreglos de n ́umeros reales de igual tama ̃no. Sean
#v = [v0, v1, . . . , vn−1] y w = [w0,w1, . . . ,wn−1] dos arreglos, el
#producto directo de v y w (notado v ∗ w) es el vector:
#[v0 ∗ w0, v1 ∗ w1, . . . , vn−1 ∗ wn−1].

v=[1,5,6]
w=[-8,6,4]

def producto_direc_arreglos(v,w):
    producto = [0] * len(v)
    print (producto)
    if len(v)==len(w):
        for x in range(len(v)):
            producto[x] = v[x] * w[x]

        return producto

print (producto_direc_arreglos(v,w))