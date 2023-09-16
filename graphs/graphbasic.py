class Graph:
    def __init__(self, gdict=None) -> None:
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


contentDict = {'A': ['B', 'C'],
               'B': ['A', 'D', 'E'],
               'C': ['A', 'E'],
               'D': ['B', 'E', 'F'],
               'E': ['C', 'D', 'F'],
               'F': ['D', 'E']}

graph = Graph(contentDict)
graph.addEdge('F', 'O')
graph.addEdge('F', 'S')
print(graph.gdict)
