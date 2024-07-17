import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # giulia
        self._listGenes = []
        self._gene = None
        self._localization = None
        self._listLocalizations = []
        # fine giulia

    def handle_graph(self, e):
        self._model.buildGraph()
        self._model.printGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici:{self._model.getNumNodi()}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi:{self._model.getNumArchi()}"))
        nmin, nmax = self._model.calcolaMinMax()
        self._view.txt_result.controls.append(ft.Text(f"Valore minimo {nmin} e massimo {nmax}"))
        self._view.update_page()
        #print(self._model.getNumArchi())

    def handle_countedges(self, e):
        soglia = self._view.txt_name.value
        try:
            sogliaIns = float(soglia)
        except ValueError:
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text(f"Il numero inserito non è valido"))
            self._view.update_page()
            return
        min, max = self._model.calcolaMinMax()
        if sogliaIns > min and sogliaIns < max:
            self._view.txt_result2.controls.clear()
            numMag, numMin = self._model.contaValoriSoglia(sogliaIns)
            self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {numMag}"))
            self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {numMin}"))
            self._view.update_page()
        else:
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text(f"Il numero inserito non rispetta il valore min e max"))
            self._view.update_page()
            return

    def handle_search(self, e):
        pass


# giulia
    def fillDDGenes(self):
        self._listGenes = self._model.getGenes()
        for s in self._listGenes:
            self._view.ddgenes.options.append(ft.dropdown.Option(s))
        self._view.update_page()
    # fine

    # giulia
    def read_genes(self, e):
        if e.control.value == "None":
            self._gene = None
        else:
            self._gene = e.control.value
        print(self._gene)
    # fine
        # giulia
    def fillDDLocalizations(self):
        self._listLocalizations = self._model.getLocalizations()
        for s in self._listLocalizations:
            self._view.ddlocalizations.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    # fine

    # giulia
    def read_localizations(self, e):
        if e.control.value == "None":
            self._localization = None
        else:
            self._localization = e.control.value
    # fine

#andrea
    def handle_controlloandrea(self, e):
        # NameStato = self._view.ddstate.value
        geneSel = self._gene
        if geneSel is None:
            self._view.create_alert("Gene non selezionato")
            return
        # controllo e gestione del valore soglia
        try:
            numeroandrea = int(self._view._txtNumeroAndrea.value)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Numero Andrea Non Inserito"))
            self._view.update_page()
            return


        self._view.txt_result.controls.append(ft.Text(geneSel))
        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato, num vertici {self._model.getNumNodi()} e numero archi {self._model.getNumArchi()}"))
        shortestPath = self._model.getShortestPath()
        for i in range(0, len(shortestPath)):
            self._view.txt_result.controls.append(ft.Text(shortestPath[i]))

        self._model.getDegrees()
        self._view.txt_result.controls.append(ft.Text("Prima"))
        iteratore = self._model.getAdj()
        self._view.txt_result.controls.append(ft.Text("Dopo"))
        self._view.txt_result.controls.append(ft.Text(iteratore))
        for nodo, vicini in iteratore:
            self._view.txt_result.controls.append(ft.Text(f"Nodo {nodo} ha i seguenti vicini"))
            #for vicino, attrs in vicini.items():
            #    self._view.txt_result.controls.append(ft.Text(f" - {vicino} con attributi {attrs}"))
        self._view.update_page()
    #fine andrea