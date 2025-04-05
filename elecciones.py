def contar_votos():
    votos = input("Ingrese la lista de votos: ")
    votos = list(map(int, votos.strip().split()))
    

    conteo = {1: 0, 2: 0, 3: 0, 4: 0}
    
    for voto in votos:
        if voto == 0:
            break
        if voto in conteo:
            conteo[voto] += 1
        else:
            print("Voto inválido: {voto}")

    total = sum(conteo.values())
    print("")
    print("Resultados:")
    for candidato in range(1, 5):
        porcentaje = (conteo[candidato] / total * 100) if total > 0 else 0
        print(f"Candidato {candidato}: {conteo[candidato]} votos - {porcentaje:.2f}%")

contar_votos()