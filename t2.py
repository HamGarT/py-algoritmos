import random
import math


def crearCoordenadas(cuantas):
    lista = []
    for i in range(cuantas):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        lista.append([x, y])
    return lista


def calcularDistancia(punto):
    x = punto[0]
    y = punto[1]
    return math.sqrt(x*x + y*y)


def buscarCoordenadaAlejada(lista):
    if len(lista) == 0:
        return None
    if len(lista) == 1:
        x = lista[0][0]
        y = lista[0][1]
        if x > 0 and y < 0:
            return lista[0]
        else:
            return None
        
    mitad = len(lista) // 2
    izquierda = buscarCoordenadaAlejada(lista[:mitad])
    derecha = buscarCoordenadaAlejada(lista[mitad:])

    if izquierda and derecha:
        if calcularDistancia(izquierda) > calcularDistancia(derecha):
            return izquierda
        else:
            return derecha
    elif izquierda:
        return izquierda
    else:
        return derecha



cantidad = int(input("Ingrese cantidad de coordenadas: "))
coordenadas = crearCoordenadas(cantidad)
print("")
print("Coordenadas generadas:")
for c in coordenadas:
    print(c)

resultado = buscarCoordenadaAlejada(coordenadas)

if resultado:
    print("La coordenada más alejada en X positivo y Y negativo es:", resultado)
    print("")
    print("Distancia al origen:", calcularDistancia(resultado))
else:
    print("")
    print("No se encontró ninguna coordenada con X positivo y Y negativo.")


