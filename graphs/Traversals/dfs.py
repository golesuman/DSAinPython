class Graph:
    def __init__(self,gdict=None) -> None:
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def dfs(self, vertex):
        stack = [vertex]
        visited = [vertex]
        while stack:
            deVertex = stack.pop()
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

if __name__ == '__main__':
    content = { 'a':['b','d'],
                'b':['a','c'],
                'c':['b','g'],
                'd':['a','e'],
                'e':['d','f'],
                'f':['e','g'],
                'g':['c','f']
    }
    graph = Graph(content)
    graph.dfs('a')
    


