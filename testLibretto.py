from voto.modello import Libretto, Voto
from scuola import Student

Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri",
                casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")

myLib = Libretto(Harry, voti=[])

v1 = Voto(materia = "Difesa contro le arti oscure", punteggio= 21, data="2022 - 05 - 24", lode= False)
v2 = Voto("Babbanologia", 30,"2022 - 02 - 17", True)
v3 = Voto("Trasfigurazione", 30,"2022 - 02 - 17", False)
myLib.append(v1)
myLib.append(v2)

print("------------------------------------------------------------")
print("Calcola media")
myLib.append(Voto("Pozioni", 21, "2022 - 04 - 15", False))
print(myLib.calcolaMedia())

print("------------------------------------------------------------")
print("Cerca materie con voto")
votiFiltrati = myLib.getVotiByPunti(21, False)
print(votiFiltrati) #stampando la lista
#print(votiFiltrati[0]) #stampando il singolo oggetto


print("------------------------------------------------------------")
print("Cerca voto con nome")
print(myLib.getVotoByName("Pozioni"))

votoTrasfiguarzione = myLib.getVotoByName("Trasfigurazione")
if votoTrasfiguarzione is None:
    print("Voto non trovato")
else:
    print(votoTrasfiguarzione.materia)

print("------------------------------------------------------------")
print("Il voto è già nel libretto?")
print(myLib.hasVoto(v1))
print(myLib.hasVoto(Voto("Aritmanzia", 30, "2023-07-10", False)))
print(myLib.hasVoto(Voto("Difesa contro le arti oscure", punteggio= 23, data="2022 - 05 - 24", lode= False)))

print("------------------------------------------------------------")
print("C'è conflitto?")
print(myLib.hasConflitto(Voto("Difesa contro le arti oscure", punteggio= 22, data="2022 - 05 - 24", lode= False)))

print("------------------------------------------------------------")
print("Test append modificato")
myLib.append(Voto("Aritmanzia", 30, "2023-07-10", False))
myLib.append(Voto("Difesa contro le arti oscure", punteggio= 22, data="2022 - 05 - 24", lode= False)) # darà errore per cpnflitto

myLib.append(Voto("Divinazione", 27, "2021-02-08", False))
myLib.append(Voto("Cura delle creature magiche", 26, "2021-06-13", False))

print("------------------------------------------------------------")
print("Libretto originario")
print(myLib)

print("Libretto migliorato")
print(myLib.creaMigliorato())

print(myLib)

print("------------------------------------------------------------")
print("Libretto stampato in ordine di materia")
ordinato = myLib.creaLibOrdinatoMateria()
print(ordinato)

print("------------------------------------------------------------")
print("Libretto stampato in ordine di voto")
ordinato2 = myLib.creaLibOrdinatoVoto()
print(ordinato2)

print("------------------------------------------------------------")
print("Libretto senza voti inferiori a 24")
ordinato2.cancellaInferiori(24)
print(ordinato2)