def ladron_casas(lista_casas):
    n = len(lista_casas)
    
    if n == 0:
        return 0, []
    if n == 1:
        return lista_casas[0], [0]

    botin_maximo = [0] * n
    
    botin_maximo[0] = lista_casas[0]
    
    if lista_casas[1] > lista_casas[0]:
        botin_maximo[1] = lista_casas[1]
    else:
        botin_maximo[1] = lista_casas[0]
    
    for i in range(2, n):
        opcion1 = botin_maximo[i-1]
        opcion2 = botin_maximo[i-2] + lista_casas[i]
        
        if opcion2 > opcion1:
            botin_maximo[i] = opcion2
        else:
            botin_maximo[i] = opcion1
    
    casas_vistas = []
    i = n - 1
    
    while i >= 0:
        if i == 0:
            casas_vistas.append(i)
            break
        elif i == 1:
            if lista_casas[1] > lista_casas[0]:
                casas_vistas.append(1)
            else:
                casas_vistas.append(0)
            break
        else:
            if botin_maximo[i-2] + lista_casas[i] > botin_maximo[i-1]:
                casas_vistas.append(i)
                i -= 2
            else:
                i -= 1
            
    casas_vistas.reverse()
    return botin_maximo[-1], casas_vistas


casas = [3, 4, 8,0, -1, 9]
botin, vistas = ladron_casas(casas)
print("Casas con sus respectivos botines:",casas )
print("El botín máximo que se puede robar es:", botin)
resultado = []
for i in vistas:
    if casas[i] > 0:
        texto = "Botín: " + str(casas[i])
        indice = "Índice: " + str(i)
        resultado.append((texto, indice))
print("Botines robados:")
for botin in resultado:
    print(botin)



