from UI.view import View
from voto.modello import Libretto
from scuola import Student
import flet as ft

from voto.voto import Voto


class Controller:
    def __init__(self, v: View):
        self._view = v
        self._student = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri",
                casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
        self._model = Libretto(self._student, [])
        # self._fillLibretto()

    def handleAggiungi(self, e): #passo l'evento e
        # strIn = self._view._txtIn.value
        # if strIn == "":
        #     self._view._txtOut.value = "Errore: campo vuoto"
        #     self._view._page.update()
        #     return
        #
        # self._view._txtOut.value = strIn
        # self._view._page.update()

        # Raccoglie info per creare un nuovo voto
        # Crea un oggetto Voto
        # Fa append sul libretto
        nome = self._view._txtInNome.value
        if nome == "":
            self._view._txtOut.controls.append(ft.Text("Attenzione il campo nome non può essere vuoto",
                                               color = "red"))
            self._view._page.update()
            return

        punti = self._view._ddVoto.value
        if punti is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione selezionare un voto",
                                               color = "red"))
            self._view._page.update()
            return

        data = self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione selezionare una data",
                                               color="red"))
            self._view._page.update()
            return
        if punti == "30L":
            self._model.append(Voto(nome, 30, f"{data.year}-{data.month}-{data.day}", True))
        else:
            self._model.append(Voto(nome, int(punti), f"{data.year}-{data.month}-{data.day}", False))

        self._view._txtOut.controls.append(ft.Text("Voto correttamente aggiunto",
                                           color = "green"))
        self._view._page.update()


    def handleStampa(self, e):

        self._view._txtOut.controls.append(ft.Text(str(self._model),
                                           color = "black"))  # stampa del libretto definito nella classe Libretto
        self._view._page.update()

    def getStudent(self):
        """
        Restituisce informazioni dello studente usando il __str__ dell'oggetto Student
        :return:
        """
        return str(self._student)

    # def _fillLibretto(self):
    #     v1 = Voto(materia="Difesa contro le arti oscure", punteggio=21, data="2022 - 05 - 24", lode=False)
    #     v2 = Voto("Babbanologia", 30, "2022 - 02 - 17", True)
    #     v3 = Voto("Trasfigurazione", 30, "2022 - 02 - 17", False)
    #     self._model.append(v1)
    #     self._model.append(v2)
    #     self._model.append(v3)
    #     self._model.append(Voto("Pozioni", 21, "2022 - 04 - 15", False))
