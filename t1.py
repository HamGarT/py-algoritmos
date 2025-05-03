import random

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

equipo1 = Equipo("Equipo1")
equipo2 = Equipo("Equipo2")

def RegistraSet(equipo : int):
    
    if( equipo == 1):
        equipo1.setGanados += 1
    else:
        equipo2.setGanados += 1

    if equipo1.setGanados == 3:
        equipo1.partidosGanados += 1
        equipo2.partidosPerdidos += 1
        #equipo1.setGanados = 0
        #equipo2.setGanados = 0
    elif equipo2.setGanados == 3:
        equipo2.partidosGanados += 1
        equipo1.partidosPerdidos += 1
        #equipo1.setGanados = 0
        #equipo2.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido():
    while equipo1.setGanados < 3 and equipo2.setGanados < 3:
        p1 = Puntos()
        p2 = Puntos()
        if p1 >= 25 or p2 >= 25:
            if p1 > p2 and p1 >= 25:
                RegistraSet(1)
                ganador = equipo1.nombre
            elif p2 > p1 and p2 >= 25:
                RegistraSet(2)
                ganador = equipo2.nombre
            else:
                extra1 = PuntosExtras()
                extra2 = PuntosExtras()
                p1 += extra1
                p2 += extra2
                if p1 > p2 and p1 >= 25:
                    RegistraSet(1)
                    ganador = equipo1.nombre
                elif p2 > p1 and p2 >= 25:
                    RegistraSet(2)
                    ganador = equipo2.nombre
                else:
                    continue 
        else:
            extra1 = PuntosExtras()
            extra2 = PuntosExtras()
            p1 += extra1
            p2 += extra2
            if p1 > p2 and p1 >= 25:
                RegistraSet(1)
                ganador = equipo1.nombre
            elif p2 > p1 and p2 >= 25:
                RegistraSet(2)
                ganador = equipo2.nombre
            else:
                continue

        print(f"Set ganado por {ganador}: {p1} - {p2}")
    print(f"Fin del partido: {equipo1.nombre} {equipo1.setGanados} - {equipo2.setGanados} {equipo2.nombre}")
    equipo1.setGanados = 0
    equipo2.setGanados = 0

def ResultadoTorneo():
    print(f"{equipo1.nombre}: {equipo1.partidosGanados} partidos ganados, {equipo1.partidosPerdidos} partidos perdidos")
    print(f"{equipo2.nombre}: {equipo2.partidosGanados} partidos ganados, {equipo2.partidosPerdidos} partidos perdidos")

n = int(input("¿Cuántos partidos jugarán ambos equipos? ->"))
for i in range(n):
    print("")
    print(f"--- Partido {i+1} ---")
    JugarPartido()
print()
print("=== Resultado del Torneo ===")
ResultadoTorneo()