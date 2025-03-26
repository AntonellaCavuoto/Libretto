import voto

v1 = voto.Voto(materia = "Trasfigurazione", punteggio= 24, data="2022 - 03 - 14", lode= False)
v2 = voto.Voto(materia = "Pozioni", punteggio= 30, data="2022 - 02 - 13", lode= True)
v3 = voto.Voto(materia = "Difesa contro le arti oscure", punteggio= 27, data="2022 - 05 - 24", lode= True)
print(v1)

myLib = voto.Libretto(proprietario= None, voti = [v1, v2])
print(myLib)
myLib.append(v3)

print(myLib)