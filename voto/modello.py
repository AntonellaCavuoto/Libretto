import operator
from dataclasses import dataclass

from dao.dao import LibrettoDAO
from voto.voto import Voto


# costruisco un file indipendente che raccoglie tutte le informazioni relative al libretto e i voti
# posso usare i due metodi nel main importando from voto Voto e Libretto

@dataclass(order=True)  # dataclass prende i valori e ci crea i metodi init, repr, eq, hash
class Libretto:
    def __init__(self, proprietario, voti=[]):
        self.proprietario = proprietario
        self.voti = voti
        self.dao = LibrettoDAO()
        self.fillLibretto()

    def fillLibretto(self):
        allEsami = self.dao.getAllVoti()
        for e in allEsami:
            self.append(e)

    def append(self, voto):
        if (self.hasConflitto(voto) is False and self.hasVoto(voto) is False):
            self.voti.append(voto)
            if not self.dao.hasVoto(voto):
                self.dao.addVoto(voto)
        else:
            # raise ValueError("Il voto è già presente")
            print("Il voto è già presente")

    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario}"
        for v in self.voti:
            mystr += f"{v}\n"
        return mystr

    def __len__(self):
        return len(self.voti)

    def calcolaMedia(self):
        """
        restituisce la media dei voti
        :return: valore numerico della media oppure ValueError in caso la lista fosse vuota
        """
        # media = sommaVoti / numeroEsami
        # v = []
        # for v1 in self.voti:
        #     v.append(v1.punteggio)
        # numEsami = len(self.voti)
        if len(self.voti) == 0:
            raise ValueError("Attenzione, lista esami vuota")

        listaVoti = [v.punteggio for v in self.voti]  # scrivo in una sola riga il for
        return sum(listaVoti) / len(listaVoti)
        # return math.mean(listaVoti)

    def getVotiByPunti(self, punti, lode):
        """
        retitusice una lista di esami con un punteggio uguale a punti e lode se applicata
        :param punti: variabile di tipo intero che rappresenta il punteggio
        :param lode: booleano che indica se presente la lode
        :return: lista di voti
        """
        votifiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode:
                votifiltrati.append(v)
        return votifiltrati

    def getVotoByName(self, nome):
        """
        restituisce un oggetto voto il cui campo materia è uguale al nome
        :param nome: stringa che indica il nome della materia
        :return: oggetto di tipo voto oppure None in caso di voto non trovato
        """

        for v in self.voti:
            if v.materia == nome:
                return v

    def hasVoto(self, voto):
        """
        verifica se il libretto contiene già il voto.
        Due voti sono considerati uguali se hanno lo stesso campo materia e lo stesso campo punteggio.
        :param voto: istanza dell'oggetto di tipo voto
        :return: True se è già presente, False altriementi
        """
        for v in self.voti:
            # modo numero 1
            # if v == voto:
            # modo numero 2
            if (v.materia == voto.materia and v.punteggio == voto.punteggio and v.lode == voto.lode):
                return True
        return False

    # def __eq__(self, other): specializzato
    #     return (self.materia == other.materia and
    #             self.punteggio == other.punteggio and
    #             self.lode == other.lode)

    def hasConflitto(self, voto):
        """
        Questo metodo controla che il voto "voto" non rappresenti un conflitto con i voti già presenti nel libretto.
        Consideriamo due voti in conflitto quando hanno lo stesso campo materia, ma diverso voto
        :param voto: intanza della classe Voto
        :return: True se voto è in conflitto, False altrimenti
        """
        for v in self.voti:
            if (v.materia == voto.materia and not (v.punteggio == voto.punteggio and v.lode == voto.lode)):
                return True
        return False

    def copy(self):
        """
        Crea una nuovo copia del Libretto
        :return: istanza della classe Libretto
        """
        nuovo = Libretto(self.proprietario.copy(), [])  # metodo classe Student
        for v in self.voti:
            nuovo.append(v.copy())  # copy è un metodo della classe voto
        return nuovo

    def creaMigliorato(self):
        """
        crea un nuovo oggetto Libretto, in cui i voti sono migliorati con la seguente logica:
        se il voto è >= 18 e < 24 aggiungo +1
        se il voto è >= 24 e < 29 aggiungo +2
        seil voto è 29 aggiungo +1
        se il voto è 30 rimane 30
        :return: nuovo Libretto
        """
        # nuovo = Libretto(self.proprietario, self.voti.copy())
        # copy di una lista --> prende una lista e la copia
        # senza la copy, modificando i voti in nuovo, modificherei anche la lista del libretto vecchio,
        # però modificherò comunque i riferimenti

        # il proprietario non viene modificato

        # quindi creo lista vuota

        # nuovo = Libretto(self.proprietario, [])  # lista di voti vuota
        # for v in self.voti:
        #     nuovo.append(v.copy())  # copy è un metodo della classe voto

        nuovo = self.copy()  # metodo della classe libretto

        # modifico i voti in nuovo
        for v in nuovo.voti:
            if (v.punteggio >= 18 and v.punteggio < 24):
                v.punteggio += 1
            elif (v.punteggio < 29 and v.punteggio >= 24):
                v.punteggio += 2
            elif (v.punteggio == 29):
                v.punteggio += 1

        return nuovo

    def sortByMateria(self):
        # self.voti.sort(key = estraiMateria)
        self.voti.sort(key=operator.attrgetter("materia"))  # !!!!!!!!!!!!!!!!!

    # opzione 1: creo due metodi di stampa che prima ordinano e poi stampano
    # con questa opzione mischio logiche
    # opzione 2:creo due metodi che ordinano la lista di self e poi un unico metodo di stampa
    # opzione 3: creo due metodi che si fanno uan copia autonoma della lista, la ordinano e la restituiscono,
    # poi un altro metodo si occuperà di stampare le nuove liste
    # più versatile
    # opzione 4: creo una shallow copy di self.voti e ordino quella

    def creaLibOrdinatoMateria(self):
        """
        Crea un uovo oggetto Libretto e lo ordina per materia
        :return: nuova istanza dell'oggetto Libretto
        """
        nuovo = self.copy()
        nuovo.sortByMateria()
        return nuovo

    def creaLibOrdinatoVoto(self):  # metodo 2
        """
        Crea un nuovo oggetto Libretto e lo ordina per voto
        :return: nuova istanza dell'oggetto libretto
        """
        nuovo = self.copy()
        # nuovo.sort(key=operator.attrgetter("punteggio"))
        # con lambda definisico una funziona che uso solo una volta (sarebbe come EstraiMateria)
        nuovo.voti.sort(key=lambda v: (v.punteggio, v.lode),
                        reverse=True)  # il sort così viene fatto anche seguendo la lode
        # il sort viene fatto su tuple con True > False
        # reverse = True per ordine decrescente
        return nuovo

    def cancellaInferiori(self, punteggio):
        """
        Questo metodo agisce sul libretto corrente eliminando tutti i voti inferiori al parametro punteggio
        :param punteggio: intero indicante il valore minimo accettato
        :return:
        """

        # modo 1
        # for i in range(len(self.voti)):
        #     if self.voti[i].punteggio < punteggio:
        #         self.voti.pop(i)

        # T=0 -- [18 18 18 26 27 28]
        # con i = 1 tolgo il secondo 18 T=1 -- [18 18 26 27 28]
        # con i = 2 tolgo il terzo 18 T=2 -- [18 26 27 28]
        # sto iterando la stessa lista che sto modificando

        # modo 2
        # for v in self.voti:
        #     if v.punteggio < punteggio:
        #         self.voti.remove(v)
        # sto iterando la stessa lista che sto modificando

        # modo 3:
        # nuovo = [] # aggiungo alla lista i voti ammissibili
        #
        # for v in self.voti:
        #     if v.punteggio >= punteggio:
        #         nuovo.append(v)

        nuovo = [v for v in self.voti if v.punteggio >= punteggio]  # compatta
        self.voti = nuovo  # modifico libretto attuale

        return (self.voti)


def estraiMateria(voto):  # funzione stand alone
    """
    Questo emtodo restituisce il campo materia dell'oggetto voto
    :param voto: istanza della classe Voto
    :return: stringa con nome della materia
    """
    return voto.materia


def testVoto():
    # se name =="__main__" vuol dire che lo sto usando da solo, non lo sto importando, e quindi lo testo
    v1 = Voto(materia="Trasfigurazione", punteggio=24, data="2022 - 03 - 14", lode=False)
    v2 = Voto(materia="Pozioni", punteggio=30, data="2022 - 02 - 13", lode=True)
    v3 = Voto(materia="Difesa contro le arti oscure", punteggio=27, data="2022 - 05 - 24", lode=True)
    print(v1)

    myLib = Libretto(proprietario=None, voti=[v1, v2])
    print(myLib)
    myLib.append(v3)

    print(myLib)


if __name__ == "__main__":
    testVoto()
