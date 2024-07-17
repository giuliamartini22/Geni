import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._listChromosomes = []
        self._graph = nx.DiGraph()
        self._edges = []

        # andrea
        self.listGenes = []
        self._listLocalizations = []
        # fine andrea

    def buildGraph(self):
        self._listChromosomes = DAO.getAllChromosome()
        self._graph.add_nodes_from(self._listChromosomes)
        self._listCorr = DAO.getAllCorrelazioni()
        for c in self._listCorr:
            cr1 = c.c1
            cr2 = c.c2
            peso = c.corr
            if cr1 in self._graph and cr2 in self._graph:
                if self._graph.has_edge(cr1, cr2):
                    self._graph[cr1][cr2]['weight'] += peso
                else:
                    self._graph.add_edge(cr1, cr2, weight=peso)

    def calcolaMinMax(self):
        pesoMin = 0
        pesoMax = 0
        for a in self._graph.edges:
            peso = self.getEdgeWeight(a[0], a[1])
            if pesoMin == 0:
                pesoMin = peso
            else:
                if peso < pesoMin:
                    pesoMin = peso
            if pesoMax == 0:
                pesoMax = peso
            else:
                if peso > pesoMax:
                    pesoMax = peso
        return float(pesoMin), float(pesoMax)

    def contaValoriSoglia(self, soglia):
        numMaggiori = 0
        numMinori = 0
        for a in self._graph.edges:
            peso = self.getEdgeWeight(a[0], a[1])
            if peso > soglia:
                numMaggiori += 1
            else:
                numMinori += 1
        return numMaggiori, numMinori

    def getEdgeWeight(self, v1,v2):
        return self._graph[v1][v2]["weight"]


    def printGraph(self):
        for e in self._graph.edges:
            print(self._graph[e[0]][e[1]])
            #print(self._graph[e[0]])
    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)

# andrea
    def getGenes(self):
        self._listGenes = DAO.getAllGenes()
        return self._listGenes
    # fine andrea
    def getLocalizations(self):
        self._listLocalizations = DAO.getAllLocalizations()
        #self._listLocalizations = DAO.getTypes()
        #self._listLocalizations = DAO.getExprCorr()
        #self._listLocalizations = DAO.getAllChromosome()
        #self._listLocalizations = DAO.getFunction()
        #self._listLocalizations = DAO.getEssential()
        return self._listLocalizations
    # fine andrea

    def getShortestPath(self):
        shortest_path = nx.shortest_path(self._graph, source= 1, target=4)
        print(shortest_path)
        return shortest_path

    def getDegrees(self):
        degrees = dict(self._graph.degree())
        print(degrees)
        return degrees

    def getAdj(self):
        iteratore_adiacenti = self._graph.adjacency()
        for nodo, vicini in iteratore_adiacenti:
            print(f"Nodo {nodo} ha i seguenti vicini")
            for vicino, attrs in vicini.items():
                print(f" - {vicino} con attributi {attrs}")
        return iteratore_adiacenti

