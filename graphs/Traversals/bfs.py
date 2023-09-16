class Graph:
    def __init__(self, gdict=None) -> None:
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def Bfs(self, vertex):
        queue = [vertex]
        visited = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjancentVertex in self.gdict[deVertex]:
                if adjancentVertex not in visited:
                    visited.append(adjancentVertex)
                    queue.append(adjancentVertex)


if __name__ == '__main__':
    content = {'a': ['b', 'd'],
               'b': ['a', 'c'],
               'c': ['b', 'g'],
               'd': ['a', 'e'],
               'e': ['d', 'f'],
               'f': ['e', 'g'],
               'g': ['c', 'f']
               }

graph = Graph(content)
graph.Bfs('a')
