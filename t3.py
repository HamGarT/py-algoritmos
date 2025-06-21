
laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [ 3,  0, 0, 1, 0, 1, 0, 0, 1],
    [ 1,  1, 0, 1, 1, 1, 1, 0, 1],
    [ 0,  1, 0, 1, 0, 0, 1, 0, 1],
    [ 1,  1, 1, 1, 1, 1, 3, 1, 1],
    [ 3,  0, 1, 0, 0, 0, 1, 0, 1],
    [ 1,  1, 1, 1, 3, 1, 1, 1, 1],
    [ 1,  0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

filas = 9
columnas = 9
puntos_necesarios = 23
solucion = [] 

def mostrar_laberinto(matriz):
    print("   0 1 2 3 4 5 6 7 8")
    for i in range(filas):
        print(f"{i}:", end=" ")
        for j in range(columnas):
            print(f"{matriz[i][j]}", end=" ")
        print()

def puedo_mover(fila, col, visitado):
    if fila < 0 or fila >= filas or col < 0 or col >= columnas:
        return False
    
    if visitado[fila][col]:
        return False

    if laberinto[fila][col] == 0:
        return False
    
    return True

def obtener_puntos(fila, col):
    casilla = laberinto[fila][col]
    if casilla == 3:
        return 3
    elif casilla == 4:
        return 4
    else:  
        return 0


def resolver_laberinto(fila, col, visitado, puntos, camino):

    #print(f"Visitando posición ({fila},{col}) - Puntos acumulados: {puntos}")
    if laberinto[fila][col] == 'F':
        if puntos >= puntos_necesarios:
            
            solucion.extend(camino)
            return True
        else:
            return False
    
    direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    nombres = ["arriba", "derecha", "abajo", "izquierda"]
    
    for i in range(4):
        nueva_fila = fila + direcciones[i][0]
        nueva_col = col + direcciones[i][1]
        
        if puedo_mover(nueva_fila, nueva_col, visitado):
           
            visitado[nueva_fila][nueva_col] = True
            
            puntos_casilla = obtener_puntos(nueva_fila, nueva_col)
            nuevos_puntos = puntos + puntos_casilla
            camino.append((nueva_fila, nueva_col))
            
            if resolver_laberinto(nueva_fila, nueva_col, visitado, nuevos_puntos, camino):
                return True
            
            visitado[nueva_fila][nueva_col] = False
            camino.pop()
    
    return False


def mostrar_camino():
    matriz_solucion = [[' ' for _ in range(columnas)] for _ in range(filas)]
    for fila, col in solucion:
        if laberinto[fila][col] == 'I':
            matriz_solucion[fila][col] = 'I'
        elif laberinto[fila][col] == 'F':
            matriz_solucion[fila][col] = 'F'
        else:
            matriz_solucion[fila][col] = '1'
    print("")
    print("Camino de solución:")
    mostrar_laberinto(matriz_solucion)
    puntos_total = 0
    for fila, col in solucion:
        puntos_total += obtener_puntos(fila, col)
    print("")
    print(f"Puntos obtenidos: {puntos_total}")
    print(f"Puntos necesarios: {puntos_necesarios}")


print("SOLUCIONADOR DE LABERINTO")
print("El ratón debe ir de 'I' a 'F' sumando al menos 23 puntos")
print("")
print("Laberinto original:")
mostrar_laberinto(laberinto)
    
  
inicio_fila = 8 
inicio_col = 0   
    
   
visitado = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(False)
    visitado.append(fila)

visitado[inicio_fila][inicio_col] = True
    
   
camino = [(inicio_fila, inicio_col)]

print("")    
print("Buscando solución...")
  
if resolver_laberinto(inicio_fila, inicio_col, visitado, 0, camino):
    print("Se encontró un camino válido")
    mostrar_camino()
else:
    print("No se pudo encontrar un camino que sume 23 o más puntos")

